const puppeteer = require('puppeteer');

(async () => {
  // 1. 啟動無界面 Chrome
  const browser = await puppeteer.launch({ headless: true });

  // 2. 開啟新分頁
  const page = await browser.newPage();

  // 3. 導到 Google
  await page.goto('https://www.google.com');

  // 4. 全頁截圖
  await page.screenshot({
    path: 'module-01-setup/screenshots/puppeteer_google.png',
    fullPage: true
  });

  // 5. 關閉瀏覽器
  await browser.close();
})();
