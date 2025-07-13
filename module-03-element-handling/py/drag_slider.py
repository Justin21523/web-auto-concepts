from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com/slider")

slider = driver.find_element(By.CSS_SELECTOR, ".slider-handle")
action = ActionChains(driver)

# 1. 按住並拖曳 100 像素
action.click_and_hold(slider).move_by_offset(100, 0).release().perform()

# 2. 讀取最終值
value = driver.find_element(By.ID, "slider-value").text
print("Slider value:", value)

driver.quit()
