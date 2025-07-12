🔹 模組二：核心操作入門—導航、分頁與截圖

📘 **Concept**
本模組將介紹如何透過瀏覽器自動化工具進行多分頁（multiple tabs）操作與特定區域截圖，並解析 HTTP 請求流程、DOM 結構與 Selector 理解的重要概念。

🌍 **Scenario**
假設你需要批量截取多個產品頁面的特定區域（如價格與名稱），並將它們依序儲存成圖片，以便後續報表生成與圖像比對。

🧪 **Code (Python)**

```python
# 範例：Selenium 多分頁 + 截圖
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3'
]

for idx, url in enumerate(urls, start=1):
    driver.execute_script('window.open()')           # 開新分頁
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, '.price')
    element.screenshot(f"screenshots/selenium_price_{idx}.png")

# 回到第一分頁
driver.switch_to.window(driver.window_handles[0])
driver.quit()
```

🧪 **Code (JavaScript)**

```javascript
// 範例：Playwright 多分頁 + 批量截圖
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3'
  ];

  for (let i = 0; i < urls.length; i++) {
    const page = await context.newPage();
    await page.goto(urls[i]);
    const price = await page.locator('.price');
    await price.screenshot({ path: `screenshots/playwright_price_${i+1}.png` });
    await page.close();
  }

  await browser.close();
})();
```

🔍 **Explanation**

* 使用 `window.open()` 或 `context.newPage()` 啟動新分頁／分頁上下文
* `driver.switch_to.window()` 或關閉 page 後自動回到前一分頁
* 利用 Locator 選取器擷取元素並針對該區域進行截圖

🎯 **Expected Result**
執行後，`module-02-navigation/screenshots/` 會生成：

* `selenium_price_1.png`、`selenium_price_2.png`、`selenium_price_3.png`
* `playwright_price_1.png`、`playwright_price_2.png`、`playwright_price_3.png`

🛠 **Common Pitfalls**

* 忘記 `switch_to.window()` 導致截到空白頁
* 選取器錯誤導致 `NoSuchElementException`
* headless 環境下元素未渲染完全，需等待或滾動至可視範圍

📂 **File & Folder Structure**

```
module-02-navigation/
├── py/
│   └── navigation_screenshot.py
├── js/
│   └── navigation_screenshot.js
├── screenshots/
│   ├── selenium_price_1.png
│   ├── selenium_price_2.png
│   └── selenium_price_3.png
├── docs/
│   └── module-02.md
└── notes.md
```
