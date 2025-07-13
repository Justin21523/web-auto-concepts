const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto('https://example.com/modal');

  // 1. 點擊開啟
  await page.click('#open-modal');
  // 2. 等待 modal
  const modal = await page.waitForSelector('.modal-content');

  // 3. 填寫並提交
  await modal.fill('textarea[name="feedback"]', '這是我的回饋意見。');
  await modal.click('button.submit');

  // 4. 點擊關閉
  await page.click('button.close');

  await browser.close();
})();
