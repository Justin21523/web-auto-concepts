from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 啟動瀏覽器
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=webdriver.ChromeOptions().add_argument('--headless')
)
driver.get('https://example.com/dynamic-products')

# 2. 隱式等待
# 設定後每次 find_element 都會等待最多 10 秒
driver.implicitly_wait(10)

# 3. 顯式等待: 等待特定 AJAX 載入完成
wait = WebDriverWait(driver, 15)
product_list = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-item'))
)
print(f"Loaded {len(product_list)} products.")

# 4. 自定義輪詢: 等到 "Load More" 按鈕可點擊
for _ in range(3):
    load_more = wait.until(
        EC.element_to_be_clickable((By.ID, 'load-more-btn'))
    )
    load_more.click()
    # 等待新一批 items 出現
    wait.until(
        EC.staleness_of(product_list[0])
    )
    product_list = driver.find_elements(By.CSS_SELECTOR, '.product-item')
    print(f"After click, total items: {len(product_list)}")

# 5. 清理
driver.quit()
