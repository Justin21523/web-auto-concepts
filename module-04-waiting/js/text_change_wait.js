const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page    = await browser.newPage();
  await page.goto("https://example.com/status");

  // 1. 等待 #status 文字變成 Completed
  await page.waitForFunction(
    () => document.querySelector('#status').textContent.includes('Completed'),
    null,
    { timeout: 10000 }
  );

  // 2. 取文字並印出
  const text = await page.textContent('#status');
  console.log('New status text:', text);

  await browser.close();
})();
