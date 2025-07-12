🔹 模組一：自動化工具全貌與環境架設

📘 **Concept**
在瀏覽器自動化中，最常見的兩大底層技術是 **WebDriver**（透過驅動程式操控瀏覽器）與 **CDP（Chrome DevTools Protocol）**（直接透過 DevTools 協議與瀏覽器通訊）。WebDriver 通用、穩定，適合多瀏覽器；CDP 延遲低、功能強，能夠攔截網路請求或操作瀏覽器內部狀態。本模組先帶你了解這兩者差異，再示範四種主流工具的環境建置與「載入 Google 首頁並截圖」示範。

🌍 **Scenario**
假設你在 IT 團隊，需每天檢查「Google 首頁」是否正常可用，並自動截圖存檔，以利排程報表或若失敗時觸發告警。你會用 Python（Selenium、undetected-chromedriver）與 JavaScript（Playwright、Puppeteer）實現同樣任務，並比較它們的啟動速度與穩定性。

🧪 **Code (Python)**

```python
# 1. Selenium 範例
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 啟動 Chrome（headless 模式）
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
driver.save_screenshot("screenshots/selenium_google.png")
driver.quit()


# 2. undetected-chromedriver 範例
import undetected_chromedriver as uc

driver = uc.Chrome(headless=True)
driver.get("https://www.google.com")
driver.save_screenshot("screenshots/uc_google.png")
driver.quit()
```

🧪 **Code (JavaScript)**

```javascript
// 1. Puppeteer 範例
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://www.google.com');
  await page.screenshot({ path: 'screenshots/puppeteer_google.png', fullPage: true });
  await browser.close();
})();


// 2. Playwright 範例
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.google.com');
  await page.screenshot({ path: 'screenshots/playwright_google.png', fullPage: true });
  await browser.close();
})();
```

🔍 **Explanation**

* **Python + Selenium**：

  1. `Service(ChromeDriverManager().install())`：自動下載並安裝對應 ChromeDriver。
  2. `options.add_argument("--headless")`：設定瀏覽器無界面模式。
  3. `driver.get(...)`：瀏覽器導向指定網址。
  4. `save_screenshot(...)`：將畫面截圖並存檔到 `screenshots/`。
  5. `driver.quit()`：結束瀏覽器進程。

* **Python + undetected-chromedriver**：

  * `uc.Chrome(headless=True)`：啟動 stealth 化的 Chrome，強化反檢測效果。

* **JavaScript + Puppeteer**：

  1. `puppeteer.launch()`：啟動 Chrome。
  2. `newPage()`：開啟新分頁。
  3. `goto()`：導頁。
  4. `screenshot()`：截全頁畫面並存檔到 `screenshots/`。
  5. `browser.close()`：關閉瀏覽器。

* **JavaScript + Playwright**：

  1. `chromium.launch()`：啟動 Chromium。
  2. `newContext()` + `newPage()`：隔離 session。
  3. `goto()` / `screenshot()` / `browser.close()` 用法與 Puppeteer 類似。

🎯 **Expected Result**
執行後於 `module-01-setup/screenshots/` 目錄下會產生四張截圖：

* `selenium_google.png`
* `uc_google.png`
* `puppeteer_google.png`
* `playwright_google.png`

透過紀錄啟動時間，你可以比較各工具的速度及穩定性。

🛠 **Common Pitfalls**

* ChromeDriver 版本不匹配 → 使用 `webdriver_manager` 自動管理。
* undetected-chromedriver 與其他 chromedriver 套件衝突 → 建議在乾淨虛擬環境中安裝。
* Node.js 套件版本相依問題 → 確認 `package.json` 中版本一致。
* headless 模式渲染差異 → 如有問題，可移除 headless。
* Windows 路徑分隔符差異 → 建議使用相對路徑並於 `.gitignore` 忽略 OS 特定檔案。

📂 **File & Folder Structure**

```
project-root/
├── module-01-setup/                # 模組一工作目錄
│   ├── py/                         # Python 腳本
│   │   ├── selenium_google.py      # Selenium 載入 Google 並截圖
│   │   └── uc_google.py            # undetected-chromedriver 範例
│   ├── js/                         # JavaScript 腳本
│   │   ├── puppeteer_google.js     # Puppeteer 範例
│   │   └── playwright_google.js    # Playwright 範例
│   ├── screenshots/                # 執行後產生的截圖
│   │   ├── selenium_google.png
│   │   ├── uc_google.png
│   │   ├── puppeteer_google.png
│   │   └── playwright_google.png
│   ├── docs/                      # 文件與紀錄
│   │   └── module-01.md            # 環境設定與性能紀錄
│   ├── requirements.txt            # Python 相依套件
│   ├── package.json                # Node.js 相依套件
│   └── .gitignore                  # 忽略檔案設定
```

🧾 **Git Version Control Tips**

* **Branch**: `feature/module-01-setup`
* **Commit messages** (統一格式，請使用英文):

  * `chore(setup): initialize Python and Node.js environment`
  * `feat(module-01): add Selenium Google screenshot script`
  * `feat(module-01): add undetected-chromedriver Google screenshot script`
  * `feat(module-01): add Puppeteer Google screenshot script`
  * `feat(module-01): add Playwright Google screenshot script`
  * `docs(module-01): record environment setup and performance results`
