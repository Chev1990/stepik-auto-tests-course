import document as document
from selenium import webdriver
import math
import time
#from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element_by_class_name("trollface.btn.btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_css_selector("#input_value")
x = int(x_element.text)
y=str(math.log((abs(12*math.sin(x)))))

z_element = browser.find_element_by_id("answer")
z_element.send_keys(y)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

time.sleep(10)
browser.quit()
