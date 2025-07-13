const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto('https://example.com/ajax-data');

  // 1. 檢查條件函式
  async function dataLoaded() {
    const count = await page.$$eval('.data-item', els => els.length);
    return count >= 1;
  }

  // 2. 設定退避參數
  let delay       = 500;   // 毫秒
  const maxTrials = 4;

  // 3. 指數退避輪詢
  for (let i = 1; i <= maxTrials; i++) {
    if (await dataLoaded()) {
      console.log(`[JS] Data loaded after ${i} attempt(s)`);
      break;
    }
    console.log(`[JS] Attempt ${i} failed; sleeping ${delay}ms`);
    await page.waitForTimeout(delay);
    delay *= 2;  // 下一次等待時間 ×2
    if (i === maxTrials) {
      throw new Error("Data did not load within backoff attempts");
    }
  }

  // 4. 取得並輸出資料
  const items = await page.$$eval('.data-item', els => els.map(e => e.textContent));
  items.forEach((text, idx) => console.log(`Item ${idx+1}: ${text}`));

  await browser.close();
})();
