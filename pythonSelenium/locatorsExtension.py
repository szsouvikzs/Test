from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.maximize_window()

driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Souvik")
driver.find_element_by_id("password").send_keys("bkqkdjqkdj")
driver.find_element_by_id("password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()

# //tagname[text()='xxx']

# driver.find_element_by_xpath("//[text()='Cancel']").click()

driver.find_element_by_name("cancel").click()

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)

print(driver.find_element_by_xpath("//form[@name='login']/label[1]").text)



#driver.close()




