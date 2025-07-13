🔹 模組三：元素操作與互動進階

📘 **Concept**
本模組聚焦於瀏覽器 DOM 事件傳遞與動態變化的機制，透過模擬使用者滑鼠與鍵盤操作，自動完成表單填寫、選單點擊與頁面滾動，並解說底層如何呼叫瀏覽器 API 執行相應行為。

🌍 **Scenario**
假設你要自動化執行「登入 demo 網站」、填入帳號密碼並提交，接著操作下拉選單選擇項目，最後滾動至頁面底部擷取特定內容。

---

## 🧪 Code (Python: Selenium + ActionChains & execute\_script)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 1. 瀏覽器與 Driver 設定
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions().add_argument('--headless'))
driver.get('https://example.com/login')

# 2. 填寫表單
element_user = driver.find_element(By.NAME, 'username')
element_pass = driver.find_element(By.NAME, 'password')
element_user.send_keys('my_user')      # 模擬鍵盤輸入
element_pass.send_keys('my_password')

# 3. 按下登入按鈕
element_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
element_button.click()                # 模擬滑鼠點擊

# 4. 等待轉跳後，操作下拉選單
# a. 找到下拉選單元素
dropdown = driver.find_element(By.ID, 'options')
# b. 執行 JavaScript 展開下拉
driver.execute_script('arguments[0].click();', dropdown)
# c. 選擇特定選項
option = driver.find_element(By.XPATH, '//option[@value="value2"]')
option.click()

# 5. 滾動至頁面底部
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# 6. 擷取特定文字
time.sleep(1)
target = driver.find_element(By.CLASS_NAME, 'footer-info').text
print('Footer info:', target)

driver.quit()
```

### 原理與拆解

1. `send_keys()`：WebDriver 透過底層 DevTools Protocol 傳送鍵盤事件到瀏覽器。
2. `click()`：模擬滑鼠點擊 DOM 元素，底層觸發 `MouseEvent`。
3. `execute_script()`：直接執行指定的 JavaScript，繞過 WebDriver 行為限制。
4. `ActionChains`（未示範）：可串連複雜動作，如拖曳、雙擊等。
5. `window.scrollTo()`：操作瀏覽器內建 API，驅動頁面滾動行為。
6. 加入 `time.sleep()` 確保內容載入完畢，避免抓取空值。

---

## 🧪 Code (JavaScript: Playwright / Puppeteer)

```javascript
// 以 Playwright 為例
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  // 1. 導向登入頁
  await page.goto('https://example.com/login', { waitUntil: 'networkidle' });

  // 2. 填入帳號密碼
  await page.fill('input[name="username"]', 'my_user');
  await page.fill('input[name="password"]', 'my_password');

  // 3. 點擊登入
  await page.click('button[type="submit"]');
  await page.waitForNavigation({ waitUntil: 'load' });

  // 4. 操作下拉選單
  await page.click('#options');
  await page.selectOption('#options', 'value2');

  // 5. 滾動至底部
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));

  // 6. 擷取 footer 資訊
  const footer = await page.textContent('.footer-info');
  console.log('Footer info:', footer);

  await browser.close();
})();
```

### 原理與拆解

* `page.fill()`：封裝了 `focus()`, `click()`, `type()` 三步，確保定位後輸入。
* `click() + waitForNavigation()`：同步等待導頁完成。
* `page.selectOption()`：直接設定 `<select>` value 屬性並觸發 `change` 事件。
* `page.evaluate()`：在瀏覽器上下文執行 arbitrary JS。

---

## 🎯 Expected Result

1. 成功登入 demo 網站
2. 下拉選單顯示且正確選取第二項
3. 頁面自動滾到最底，並在 console/terminal 顯示 `Footer info: ...` 字串

## 🛠 Common Pitfalls

* **元素尚未載入** → 使用 `WebDriverWait` / `page.waitForSelector()` 等顯式等待。
* **click() 目標被遮蔽** → 改用 `execute_script('arguments[0].click()')` 或 `force: true` 參數。
* **下拉選單無法選取** → 確認 `<select>` 元素是否隱藏，需要先展開。
* **滾動後元素仍不可見** → 使用 `scrollIntoViewIfNeeded()` / `scrollIntoView()` 把元素拉到可視範圍。

## 📂 File & Folder Structure

```
module-03-element-handling/
├── py/
│   └── form_and_interaction.py    # Selenium 元素互動範例
├── js/
│   └── form_and_interaction.js    # Playwright/Puppeteer 範例
├── docs/
│   └── module-03.md               # 本檔
└── notes.md                       # 進階筆記與排錯紀錄
```
