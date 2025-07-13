const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto('https://example.com/infinite');

  const targetCount = 20;
  while (true) {
    const count = await page.$$eval('.item', els => els.length);
    if (count >= targetCount) break;
    await page.evaluate(() => window.scrollBy(0, document.body.scrollHeight));
    await page.waitForTimeout(1000);
  }

  const items = await page.$$eval('.item', els => els.map(e => e.textContent));
  console.log('Item 20 text:', items[targetCount-1]);

  await browser.close();
})();
