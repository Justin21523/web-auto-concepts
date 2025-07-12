const puppeteer = require('puppeteer');

(async () => {
  console.time('puppeteer');
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://www.google.com');
  await browser.close();
  console.timeEnd('puppeteer');
})();
