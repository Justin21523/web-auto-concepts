const { chromium } = require('playwright');

(async () => {
  // 1. 啟動 Chromium（headless）
  const browser = await chromium.launch({ headless: true });

  // 2. 建立隔離的 Context（session）
  const context = await browser.newContext();

  // 3. 開新頁
  const page = await context.newPage();

  // 4. 導頁並截圖
  await page.goto('https://www.google.com');
  await page.screenshot({
    path: 'module-01-setup/screenshots/playwright_google.png',
    fullPage: true
  });

  // 5. 關閉
  await browser.close();
})();
