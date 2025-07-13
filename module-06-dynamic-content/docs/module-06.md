🔹 模組六：動態內容深度抓取

📘 **Concept**
本模組聚焦於攔截並解析瀏覽器與後端 API 間的網路通訊，包含 XHR/Fetch 請求、GraphQL 呼叫與 WebSocket 訊息。透過這些技術，我們能直接獲取 JSON 資料，避免僅靠 DOM 解析而漏抓或重複渲染。

🌍 **Scenario**
假設一個社群網站「評論串」無限捲動載入與即時 WebSocket 更新評論，我們要：

1. 攔截所有 XHR 請求，將回傳的 JSON 存檔
2. 監聽 WebSocket 訊息，解析即時更新的評論

---

## 🧪 Code (Python: Selenium + Selenium‑Wire)

```python
from seleniumwire import webdriver
import json
import time

# 1. 安裝：pip install selenium-wire
# 2. 啟動並攔截
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 只攔截包含 api/comments 的請求
seleniumwire_options = {'scopes': ['.*api/comments.*']}
driver = webdriver.Chrome(
    seleniumwire_options=seleniumwire_options,
    options=options
)

driver.get('https://example.com/comments')
# 等待初始資料載入
time.sleep(3)

# 3. 取得所有攔截到的 XHR 回應
for request in driver.requests:
    if request.response and 'api/comments' in request.url:
        body = request.response.body.decode('utf-8')
        data = json.loads(body)
        print('Comments batch:', data)
        # 可寫入檔案:
        # with open('comments.json', 'a') as f:
        #     json.dump(data, f, ensure_ascii=False)

# 4. 模擬捲動並攔截新一批
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)
for request in driver.requests[-5:]:  # 只看最近幾筆
    if request.response and 'api/comments' in request.url:
        print('New batch:', json.loads(request.response.body.decode('utf-8')))

driver.quit()
```

🔍 **Explanation (Python)**

1. **selenium-wire**：在 Selenium 之上攔截所有網路請求、回應物件。
2. `scopes`：只截取符合正規表達式的 URL 範圍，降低記憶體使用。
3. `driver.requests`：回傳全部請求清單，包含每個 request/response 的 headers 與 body。
4. 解析 JSON 並列印或儲存，避免透過 DOM 去重複渲染後解析。

---

## 🧪 Code (JavaScript: Playwright)

```javascript
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
```

🔍 **Explanation (JavaScript)**

1. `page.on('response')`：攔截所有 HTTP 回應，篩選含 `/api/comments` 的 JSON。
2. `page.on('websocket')`：取得 WebSocket 連線，並對 `framereceived` 事件做 JSON 解析。
3. infinite scroll：模擬使用者下拉，觸發新的 XHR，並由事件監聽器即時攔截。

---

🎯 **Expected Result**

* Terminal 中依序列印出初次 XHR 與後續每次捲動載入的 JSON 資料
* 監聽到 WebSocket 的 `new_comment` 訊息並印出

🛠 **Common Pitfalls**

* **selenium-wire 記憶體大量使用**：攔截範圍過寬，建議只留 `scopes`。
* **Playwright networkidle 無法涵蓋 WebSocket**：需搭配 `waitForTimeout` 或其他條件。
* **JSON 解析失敗**：部分回應非 JSON 或需先檢查 `response.status()`。

## 📂 File & Folder Structure

```
module-06-dynamic-content/
├── py/
│   └── dynamic_content_scrape.py   # Selenium-Wire XHR 抓取範例
├── js/
│   └── dynamic_content_scrape.js   # Playwright XHR & WebSocket 監聽
├── docs/
│   └── module-06.md
└── notes.md
```
