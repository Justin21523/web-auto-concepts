from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 啟動 headless Chrome
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# 1. 導向聯絡表單頁面
driver.get("https://example.com/contact")

# 2. 定位欄位並填入資料
driver.find_element(By.NAME, "name").send_keys("張三")
driver.find_element(By.NAME, "email").send_keys("zhang3@example.com")
driver.find_element(By.NAME, "message").send_keys("您好，我想詢問產品資訊。")

# 3. 點擊送出按鈕
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# 4. 等待提示訊息出現
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.visibility_of_element_located((By.ID, "contact-alert")))

# 5. 擷取並輸出提示文字
print("Alert text:", alert.text)

driver.quit()
