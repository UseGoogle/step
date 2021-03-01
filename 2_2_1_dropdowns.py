from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome("D:/drivers/chromedriver.exe")
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

num_1 = browser.find_element_by_id('num1').text
num_2 = browser.find_element_by_id('num2').text
summary = int(num_1) + int(num_2)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(summary))
submit_button = browser.find_element_by_class_name('btn')
submit_button.click()
