const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto("https://example.com/delay-element");

  // Playwright 沒隱式等待，但可模擬
  page.setDefaultTimeout(5000);

  // 測量「自動等待」的時間 (第一次 selector 錯誤時會重試)
  let t0 = Date.now();
  await page.$("#delayed");
  let t1 = Date.now();
  console.log(`Auto-wait took ${(t1-t0)/1000}s`);

  // 測量顯式等待
  await page.goto("https://example.com/delay-element"); // reload
  let t2 = Date.now();
  await page.waitForSelector("#delayed", { timeout: 5000 });
  let t3 = Date.now();
  console.log(`Explicit wait took ${(t3-t2)/1000}s`);

  await browser.close();
})();
