from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)  # 5 seconds is max ti,e out... 2 seconds (3 seconds save)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
# action.click_and_hold()
# action.double_click(driver.find_element(By.))
# action.drag_and_drop()
# action.move_to_element()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
