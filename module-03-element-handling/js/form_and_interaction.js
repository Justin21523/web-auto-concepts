const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  // 1. 導向登入頁
  await page.goto('https://example.com/login', { waitUntil: 'networkidle' });

  // 2. 填入帳號密碼
  await page.fill('input[name="username"]', 'my_user');
  await page.fill('input[name="password"]', 'my_password');

  // 3. 點擊登入
  await page.click('button[type="submit"]');
  await page.waitForNavigation({ waitUntil: 'load' });

  // 4. 操作下拉選單
  await page.click('#options');
  await page.selectOption('#options', 'value2');

  // 5. 滾動至底部
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));

  // 6. 擷取 footer 資訊
  const footer = await page.textContent('.footer-info');
  console.log('Footer info:', footer);

  await browser.close();
})();
