from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=webdriver.ChromeOptions().add_argument("--headless")
)
driver.get("https://example.com/table-ajax")

# 1. 自訂輪詢直到 <tr> 數量 >= 15
target = 15
start = time.time()
while True:
    rows = driver.find_elements(By.CSS_SELECTOR, "#data tr")
    if len(rows) >= target:
        break
    time.sleep(0.5)  # 每 0.5 秒再檢查一次
    if time.time() - start > 20:  # 最多等 20 秒
        raise TimeoutError("Table rows did not reach target in time")

# 2. 輸出
print(f"Total rows loaded: {len(rows)}")
driver.quit()
