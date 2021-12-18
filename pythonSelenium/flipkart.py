from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.maximize_window()

driver.get("https://www.duolingo.com/")

driver.find_element_by_xpath("//span[contains(text(),'I ALREADY HAVE AN ACCOUNT')]").click()

driver.find_element_by_xpath("//body/div[@id='overlays']/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/div[1]/input[1]").send_keys("szsouvikzs@gmail.com")

driver.find_element_by_xpath("//body/div[@id='overlays']/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/label[1]/div[1]/input[1]").send_keys("SZA#du37")

driver.find_element_by_xpath("//body/div[@id='overlays']/div[5]/div[1]/div[1]/form[1]/div[1]/button[1]").click()