🔹 模組四：等待策略與同步處理

📘 **Concept**
本模組探討在自動化流程中如何使用隱式等待、顯式等待和自定義輪詢（polling）來穩定處理 AJAX 請求與 SPA（Single Page Application）路由變動，並掌握避免 TimeoutException 或無窮等待的技巧。

🌍 **Scenario**
在一個動態載入資料的商品列表頁面，透過 AJAX 載入更多商品項目，需等待指定元素出現後再擷取；同時在使用 Infinite Scroll 時保證當前頁面所有 AJAX 請求完成後才進行下一步操作。

---

## 🧪 Code (Python: Selenium)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 啟動瀏覽器
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=webdriver.ChromeOptions().add_argument('--headless')
)
driver.get('https://example.com/dynamic-products')

# 2. 隱式等待
# 設定後每次 find_element 都會等待最多 10 秒
driver.implicitly_wait(10)

# 3. 顯式等待: 等待特定 AJAX 載入完成
wait = WebDriverWait(driver, 15)
product_list = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-item'))
)
print(f"Loaded {len(product_list)} products.")

# 4. 自定義輪詢: 等到 "Load More" 按鈕可點擊
for _ in range(3):
    load_more = wait.until(
        EC.element_to_be_clickable((By.ID, 'load-more-btn'))
    )
    load_more.click()
    # 等待新一批 items 出現
    wait.until(
        EC.staleness_of(product_list[0])
    )
    product_list = driver.find_elements(By.CSS_SELECTOR, '.product-item')
    print(f"After click, total items: {len(product_list)}")

# 5. 清理
driver.quit()
```

### 原理拆解

1. **`implicitly_wait`**：設定全局等待，若元素未即時找到，會重試直到超時。
2. **顯式等待 (`WebDriverWait` + `ExpectedConditions`)**：針對特定條件 (presence, visibility, clickable, staleness) 定位與同步。
3. **`presence_of_all_elements_located`** vs **`element_to_be_clickable`**：前者只需 DOM 中存在；後者需可互動。
4. **`staleness_of`**：判斷舊元素不再附著於 DOM，可用於確認 AJAX 載入新內容。

---

## 🧪 Code (JavaScript: Playwright)

```javascript
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
```

### 原理拆解

* **`waitForSelector`**: 等待元素在 DOM 中存在並可見。
* **`page.$$(selector)`**: 一次取得 NodeList，並回傳陣列。
* **`waitForFunction`**: 可自定義 JS 條件，例如等待舊元素移除。

---

## 🎯 Expected Result

* 初次載入後列出商品數量 (e.g. 20)
* 每次點擊"Load More"後新增 10 項，總數遞增並列印

## 🛠 Common Pitfalls

* **隱式等待誤用**: 隱性等待與顯式等待混用可能延長整體執行時間。
* **超時設定不足**: 網速慢時需加大 timeout。
* **staleness\_of 條件失敗**: 元素未替換或 AJAX 回傳同一節點，需改用其它判斷。
* **Playwright waitForFunction 參考錯誤**: 傳遞 handle 時需使用第二參數。

## 📂 File & Folder Structure

```
module-04-waiting/
├── py/
│   └── waiting_strategies.py
├── js/
│   └── waiting_strategies.js
├── docs/
│   └── module-04.md
└── notes.md
```
