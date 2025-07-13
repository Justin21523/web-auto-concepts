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
