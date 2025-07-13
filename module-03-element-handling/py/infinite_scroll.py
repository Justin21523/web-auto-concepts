from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com/infinite")

target_count = 20
while True:
    items = driver.find_elements(By.CSS_SELECTOR, ".item")
    if len(items) >= target_count:
        break
    # 滾動到底部
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(1)

# 擷取第20筆文字
print("Item 20 text:", items[target_count-1].text)
driver.quit()
