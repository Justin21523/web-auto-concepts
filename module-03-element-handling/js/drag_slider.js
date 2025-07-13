const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page    = await browser.newPage();
  await page.goto('https://example.com/slider');

  // 1. 定位 handle 位置
  const handle = await page.$('.slider-handle');
  const box    = await handle.boundingBox();

  // 2. 模擬拖曳
  await page.mouse.move(box.x + box.width/2, box.y + box.height/2);
  await page.mouse.down();
  await page.mouse.move(box.x + box.width/2 + 100, box.y + box.height/2);
  await page.mouse.up();

  // 3. 讀取值
  const value = await page.textContent('#slider-value');
  console.log('Slider value:', value);

  await browser.close();
})();
