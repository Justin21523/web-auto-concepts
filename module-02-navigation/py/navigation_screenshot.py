# 範例：Selenium 多分頁 + 截圖
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3'
]

for idx, url in enumerate(urls, start=1):
    driver.execute_script('window.open()')           # 開新分頁
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, 'div > p:nth-of-type(2) > a')
    element.screenshot(f"screenshots/selenium_info_{idx}.png")

# 回到第一分頁
driver.switch_to.window(driver.window_handles[0])
driver.quit()
