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
