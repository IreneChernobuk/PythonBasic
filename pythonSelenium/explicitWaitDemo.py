import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)  # 5 seconds is max ti,e out... 2 seconds (3 seconds save)
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # list[]
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert sum > totalAfterDiscount

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
