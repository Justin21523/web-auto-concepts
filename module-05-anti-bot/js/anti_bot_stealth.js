const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const RecaptchaPlugin = require('puppeteer-extra-plugin-recaptcha');

puppeteer.use(StealthPlugin());
puppeteer.use(
  RecaptchaPlugin({
    provider: { id: '2captcha', token: 'YOUR_2CAPTCHA_API_KEY' },
    visualFeedback: true
  })
);

(async () => {
  const uaList = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...'
  ];
  const ua = uaList[Math.floor(Math.random() * uaList.length)];
  const proxy = 'http://user:pass@proxy1:8000';

  const browser = await puppeteer.launch({
    headless: true,
    args: [
      `--proxy-server=${proxy}`,
      `--user-agent=${ua}`
    ]
  });
  const page = await browser.newPage();

  await page.goto('https://target.example.com');

  // 自動偵測並破解 reCAPTCHA
  await page.solveRecaptchas();

  // 抓取商品標題
  const titles = await page.$$eval('.product-title', els => els.map(e => e.textContent));
  console.log(titles);

  await browser.close();
})();
