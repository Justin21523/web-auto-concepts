from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 啟動 Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=webdriver.ChromeOptions().add_argument("--headless")
)
driver.get("https://example.com/status")

# 2. 等待文字變成 "Completed"
wait = WebDriverWait(driver, 10)
status_elem = wait.until(
    EC.text_to_be_present_in_element((By.ID, "status"), "Completed")
)

# 3. 抓取並輸出
new_text = driver.find_element(By.ID, "status").text
print("New status text:", new_text)

driver.quit()
