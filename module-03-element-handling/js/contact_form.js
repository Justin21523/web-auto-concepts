const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page    = await browser.newPage();

  // 1. 導向聯絡表單頁
  await page.goto('https://example.com/contact', { waitUntil: 'networkidle' });

  // 2. 填寫欄位
  await page.fill('input[name="name"]', '張三');
  await page.fill('input[name="email"]', 'zhang3@example.com');
  await page.fill('textarea[name="message"]', '您好，我想詢問產品資訊。');

  // 3. 點擊送出
  await page.click('button[type="submit"]');

  // 4. 等待提示元素並讀取文字
  const alert = await page.waitForSelector('#contact-alert', { timeout: 10000 });
  console.log('Alert text:', await alert.textContent());

  await browser.close();
})();
