from selenium import webdriver

# every browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")    # get method to hit url on browser

print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/#/consulting")

driver.back()
driver.refresh()

driver.close()



