import time
from selenium import webdriver

list = []
list2 = []

driver = webdriver.Chrome(executable_path="/Users/szsouvikzs/Selenium/chromedriver")

driver.implicitly_wait(5) # wait until 5 secnds if object is not displayed # Global wait # do not waste extra time

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

# //div[@class='product-action']/button/parent::div/parent::div/h4

for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

veggis = driver.find_elements_by_css_selector("p.product-name")

for veg in veggis:
    list2.append(veg.text)

print(list2)

#assert list == list2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text


driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

discountedAmount = driver.find_element_by_css_selector(".discountAmt").text

#assert float(discountedAmount) < int(originalAmount)

print(driver.find_element_by_class_name("promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

sum = 0
for amount in amounts:
    sum = sum + int(amount.text)

print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum == totalAmount



