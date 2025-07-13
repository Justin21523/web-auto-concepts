import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
driver.implicitly_wait(5)  # 隱式等待 5 秒
driver.get("https://example.com/delay-element")

# 測量隱式等待搜尋時間
t0 = time.time()
driver.find_element(By.ID, "delayed")  # 若元素未現，隱式等待
t1 = time.time()
print(f"Implicit wait took {t1-t0:.2f} seconds")

# 測量顯式等待搜尋時間
driver.refresh()  # 重載頁面
t2 = time.time()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "delayed")))
t3 = time.time()
print(f"Explicit wait took {t3-t2:.2f} seconds")

driver.quit()
