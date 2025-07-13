from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com/modal")

# 1. 點擊按鈕開啟 modal
driver.find_element(By.ID, "open-modal").click()

# 2. 等待 modal 可見
wait = WebDriverWait(driver, 10)
modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

# 3. 在 modal 內填寫表單
modal.find_element(By.NAME, "feedback").send_keys("這是我的回饋意見。")
modal.find_element(By.CSS_SELECTOR, "button.submit").click()

# 4. 關閉 modal
driver.find_element(By.CSS_SELECTOR, "button.close").click()
driver.quit()
