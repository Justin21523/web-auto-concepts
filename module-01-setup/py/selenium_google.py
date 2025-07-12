from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. 自動下載並啟動對應版本的 ChromeDriver
service = Service(ChromeDriverManager().install())

# 2. 設定 ChromeOptions：開啟 headless（無介面）模式
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# 3. 建立 WebDriver 實例
driver = webdriver.Chrome(service=service, options=options)

# 4. 導向 Google 首頁
driver.get("https://www.google.com")

# 5. 截圖並存到 module-01-setup/screenshots/
driver.save_screenshot("module-01-setup/screenshots/selenium_google.png")

# 6. 關閉瀏覽器
driver.quit()
