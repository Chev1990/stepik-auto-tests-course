import document as document
from selenium import webdriver
import time
import os
#from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
inputname = browser.find_element_by_name("firstname")
inputname.send_keys("Ivan")
inputlastname = browser.find_element_by_name("lastname")
inputlastname.send_keys("Petrov")
inputmail = browser.find_element_by_name("email")
inputmail.send_keys("test@mail.ru")
browser.execute_script("window.scrollBy(0, 100);")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_id("file")
element.send_keys(file_path)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()
