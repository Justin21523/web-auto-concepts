// 範例：Playwright 多分頁 + 批量截圖
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3'
  ];

  for (let i = 0; i < urls.length; i++) {
    const page = await context.newPage();
    await page.goto(urls[i]);
    const info = await page.locator('div > p:nth-of-type(2) > a');
    await info.screenshot({ path: `screenshots/playwright_info_${i+1}.png` });
    await page.close();
  }

  await browser.close();
})();
