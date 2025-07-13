from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://example.com/form-options")

# 1. 點擊 radio 與 checkbox
radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='opt1']")
checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='chk2']")
radio.click()
checkbox.click()

# 2. 驗證屬性
assert radio.is_selected(), "Radio not selected!"
assert checkbox.is_selected(), "Checkbox not selected!"

print("Radio selected:", radio.is_selected())
print("Checkbox selected:", checkbox.is_selected())

driver.quit()
