const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page    = await context.newPage();

  // 1. 監聽 XHR/Fetch 回應
  page.on('response', async response => {
    const url = response.url();
    if (url.includes('/api/comments')) {
      const data = await response.json();
      console.log('Comments batch:', data);
    }
  });

  // 2. 監聽 WebSocket 訊息
  page.on('websocket', ws => {
    ws.on('framereceived', frame => {
      try {
        const msg = JSON.parse(frame.payload);
        if (msg.type === 'new_comment') console.log('WS new comment:', msg);
      } catch {}
    });
  });

  await page.goto('https://example.com/comments', { waitUntil: 'networkidle' });

  // 3. 模擬 infinite scroll
  for (let i = 0; i < 3; i++) {
    await page.evaluate(() => window.scrollBy(0, document.body.scrollHeight));
    await page.waitForTimeout(2000);
  }

  await browser.close();
})();
