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
