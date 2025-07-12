import time
import undetected_chromedriver as uc

start = time.time()

# 1. 啟動 stealth 模式的 Chrome（headless）
driver = uc.Chrome(headless=True)

# 2. 導向 Google 首頁
driver.get("https://www.google.com")

# 4. 關閉
driver.quit()

elapsed = time.time() - start
print(f"undetected_chromedriver launch+load time: {elapsed:.2f} seconds")
