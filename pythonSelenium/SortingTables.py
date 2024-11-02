from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect add veggie names -> BrowserSortedVeggiesList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this veggieList => newSortedList
browserSortedVeggies.sort()

# veggieList == newSortedList
assert browserSortedVeggies == originalBrowserSortedList
