🔹 模組五：反爬機制原理與突破策略

📘 **Concept**
本模組深入探討常見反爬機制：UA（User-Agent）檢測、IP 封鎖／Rate Limit、指紋識別、Cloudflare 挑戰與 CAPTCHA。學習如何透過 UA 隨機化、Proxy 旋轉、瀏覽器隱身（stealth）插件，以及第三方 CAPTCHA 服務（例如 2Captcha）來突破這些機制。

🌍 **Scenario**
目標網站部署 Cloudflare，並根據 UA 與 IP 設置封鎖，請設計一支自動化腳本：

1. 隨機選取常見桌面 UA 並套用
2. 動態切換 HTTP Proxy
3. 使用 stealth 化技術隱藏自動化痕跡
4. 必要時整合 2Captcha API 自動破解圖片 CAPTCHA

---

## 🧪 Code (Python: undetected-chromedriver + Proxy + 2Captcha)

```python
import time
import random
import undetected_chromedriver as uc
import requests

# 1. 常見桌面 UA 列表
UA_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...',
    # ... 更多 UA
]

# 2. 2Captcha 設定
API_KEY = 'YOUR_2CAPTCHA_API_KEY'
CAPTCHA_URL = 'https://2captcha.com/in.php'
RES_URL     = 'https://2captcha.com/res.php'

# 3. 隨機選 UA 與 Proxy
ua = random.choice(UA_LIST)
proxy = random.choice([
    'http://user:pass@proxy1:8000',
    'http://user:pass@proxy2:8000',
])

options = uc.ChromeOptions()
options.add_argument(f'--user-agent={ua}')
options.add_argument(f'--proxy-server={proxy}')

# 4. 啟動 stealth 瀏覽器
driver = uc.Chrome(options=options, headless=True)

driver.get('https://target.example.com')

# 5. 若遇 CAPTCHA
if 'captcha' in driver.page_source.lower():
    # 5.1 截圖 CAPTCHA 圖片
    captcha_img = driver.find_element_by_css_selector('img.captcha').screenshot_as_png
    # 5.2 上傳到 2Captcha
    resp = requests.post(CAPTCHA_URL, files={'file': ('captcha.png', captcha_img)}, data={'key':API_KEY, 'method':'post'})
    captcha_id = resp.text.split('|')[1]
    # 5.3 輪詢結果
    time.sleep(20)
    res = requests.get(RES_URL, params={'key':API_KEY, 'action':'get', 'id':captcha_id})
    code = res.text.split('|')[1]
    # 5.4 填入並提交
    driver.find_element_by_name('captcha_input').send_keys(code)
    driver.find_element_by_css_selector('button.submit').click()

# 6. 正常抓取所需資料
elements = driver.find_elements_by_css_selector('.product-title')
for e in elements:
    print(e.text)

driver.quit()
```

### 原理拆解

1. **UA 隨機化**：避免單一 UA 被封鎖或識別爲機器人。
2. **Proxy 旋轉**：更換 IP，繞過 Rate Limit 與地理封鎖。
3. **undetected-chromedriver**：內建 stealth 技術，隱藏 WebDriver 屬性。
4. **2Captcha API**：自動上傳 CAPTCHA 圖片並取得解答，實現自動破解。

---

## 🧪 Code (JavaScript: Puppeteer Extra + Stealth + Proxy)

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const RecaptchaPlugin = require('puppeteer-extra-plugin-recaptcha');

puppeteer.use(StealthPlugin());
puppeteer.use(
  RecaptchaPlugin({
    provider: { id: '2captcha', token: 'YOUR_2CAPTCHA_API_KEY' },
    visualFeedback: true
  })
);

(async () => {
  const uaList = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...'
  ];
  const ua = uaList[Math.floor(Math.random() * uaList.length)];
  const proxy = 'http://user:pass@proxy1:8000';

  const browser = await puppeteer.launch({
    headless: true,
    args: [
      `--proxy-server=${proxy}`,
      `--user-agent=${ua}`
    ]
  });
  const page = await browser.newPage();

  await page.goto('https://target.example.com');

  // 自動偵測並破解 reCAPTCHA
  await page.solveRecaptchas();

  // 抓取商品標題
  const titles = await page.$$eval('.product-title', els => els.map(e => e.textContent));
  console.log(titles);

  await browser.close();
})();
```

### 原理拆解

* `puppeteer-extra-plugin-stealth`：修改瀏覽器指紋、移除自動化痕跡。
* `puppeteer-extra-plugin-recaptcha`：整合 2Captcha，自動識別並填寫 Google reCAPTCHA。
* `--proxy-server` 與 `--user-agent`：結合代理與 UA 隨機化。

---

## 🎯 Expected Result

能成功繞過 Cloudflare、CAPTCHA 驗證，並列出 `'.product-title'` 文字列表。

## 🛠 Common Pitfalls

* **Proxy 掛掉或驗證失敗**：確保代理可用且帳密正確。
* **2Captcha 時延**：API 回傳慢，需調整等待時間。
* **Stealth 插件版本相依**：套件版本需與 Puppeteer 相容。
* **CAPTCHA 類型不支援**：部分圖形或滑塊 CAPTCHA 需自訂處理。

## 📂 File & Folder Structure

```
module-05-anti-bot/
├── py/
│   └── anti_bot_stealth.py
├── js/
│   └── anti_bot_stealth.js
├── docs/
│   └── module-05.md
└── notes.md
```
