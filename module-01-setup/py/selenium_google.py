import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

start = time.time()

# 1. 自動下載並啟動對應版本的 ChromeDriver
service = Service(ChromeDriverManager().install())

# 2. 設定 ChromeOptions：開啟 headless（無介面）模式
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# 3. 建立 WebDriver 實例
driver = webdriver.Chrome(service=service, options=options)

# 4. 導向 Google 首頁
driver.get("https://www.google.com")

driver.quit()

elapsed = time.time() - start
print(f"Selenium launch+load time: {elapsed:.2f} seconds")
