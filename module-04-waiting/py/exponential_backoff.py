import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. 啟動 headless Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=webdriver.ChromeOptions().add_argument("--headless")
)
driver.get("https://example.com/ajax-data")

# 2. 定義檢查條件函式：判斷所需資料是否已加載
def data_loaded():
    # 假設 AJAX 會生成 .data-item 元素
    items = driver.find_elements(By.CSS_SELECTOR, ".data-item")
    return len(items) >= 1

# 3. 設定退避參數
initial_delay = 0.5     # 秒
max_attempts = 4        # 最多重試次數
delay = initial_delay

# 4. 指數退避輪詢
for attempt in range(1, max_attempts + 1):
    if data_loaded():
        print(f"[Python] Data loaded after {attempt} attempt(s)")
        break
    print(f"[Python] Attempt {attempt} failed; sleeping {delay}s before retry")
    time.sleep(delay)
    delay *= 2            # 延長等待時間（2 的指數）
else:
    raise TimeoutError("Data did not load within backoff attempts")

# 5. 成功後擷取資料
elements = driver.find_elements(By.CSS_SELECTOR, ".data-item")
for idx, el in enumerate(elements, 1):
    print(f"Item {idx}: {el.text}")

driver.quit()
