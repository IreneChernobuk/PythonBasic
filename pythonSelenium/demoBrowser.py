import time

from selenium import webdriver

# Chrome driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)




#time.sleep(3)