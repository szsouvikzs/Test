from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

#       driver.find_element_by_name("name").send_keys("Souvik Ghosh")

driver.find_element_by_css_selector("input[name='name']").send_keys("Souvik")

driver.find_element_by_name("email").send_keys("szsouvikzs@gmail.com")

driver.find_element_by_id("exampleCheck1").click()

#        select class provide the methods to handle the options in dropdown

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#   dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#   dropdown.select_by_value("M")






driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message







#   //*[contains(@class,'alert-sucess')] --xpath
#   [class*='alert-success'] --css

#   driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()



