const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page    = await browser.newPage();
  await page.goto('https://example.com/dynamic-products');

  // 1. 顯式等待: 全部 product-item 出現
  await page.waitForSelector('.product-item', { timeout: 15000 });
  let items = await page.$$('.product-item');
  console.log(`Loaded ${items.length} products.`);

  // 2. 自定義輪詢: 點擊 Load More 並等待新內容
  for (let i = 0; i < 3; i++) {
    // 等到按鈕可點擊
    await page.waitForSelector('#load-more-btn:enabled');
    await page.click('#load-more-btn');

    // 等到舊第一項不見
    const first = items[0];
    await page.waitForFunction(
      (el) => !document.body.contains(el),
      first
    );
    // 更新 items
    items = await page.$$('.product-item');
    console.log(`After click, total items: ${items.length}`);
  }

  await browser.close();
})();
