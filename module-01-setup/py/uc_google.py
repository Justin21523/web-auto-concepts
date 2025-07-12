import undetected_chromedriver as uc

# 1. 啟動 stealth 模式的 Chrome（headless）
driver = uc.Chrome(headless=True)

# 2. 導向 Google 首頁
driver.get("https://www.google.com")

# 3. 截圖
driver.save_screenshot("module-01-setup/screenshots/uc_google.png")

# 4. 關閉
driver.quit()
