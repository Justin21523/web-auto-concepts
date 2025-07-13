const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto("https://example.com/table-ajax");

  // 1. 自訂輪詢
  const target = 15;
  const start  = Date.now();
  while (true) {
    const count = await page.$$eval("#data tr", els => els.length);
    if (count >= target) break;
    if (Date.now() - start > 20000) {
      throw new Error("Timeout: table rows did not reach target");
    }
    await page.waitForTimeout(500);
  }

  // 2. 輸出
  const finalCount = await page.$$eval("#data tr", els => els.length);
  console.log(`Total rows loaded: ${finalCount}`);

  await browser.close();
})();
