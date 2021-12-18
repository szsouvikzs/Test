import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Souvik")

driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()

driver.find_element_by_css_selector("#name").send_keys("Ghosh")

driver.find_element_by_id("confirmbtn").click()
#alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.dismiss()

