const { chromium } = require('playwright');

(async () => {
  console.time('playwright');
  // 1. 啟動 Chromium（headless）
  const browser = await chromium.launch({ headless: true });

  // 2. 建立隔離的 Context（session）
  const context = await browser.newContext();

  // 3. 開新頁
  const page = await context.newPage();

  await page.goto('https://www.google.com');

  // 5. 關閉
  await browser.close();
  console.timeEnd('playwright');
})();
