from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

driver.find_element_by_xpath("//input[@value='radio3']").click()

#   radiobuttons = driver.find_element_by_name("radioButton")
#   radiobuttons[2].click()
#   assert radiobuttons[2].is_selected()





