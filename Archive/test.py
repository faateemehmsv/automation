from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
#chrome_option.add_argument("--incognito")
#chrome_option.add_argument("--headless")
driver = webdriver.Chrome(executable_path = 'c:\chromedriver.exe', chrome_options=chrome_option)
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_option) # with chrome option
#driver.get('https://www.wikipedia.org/')
# 1 > ID
#element1 = driver.find_element('id','searchInput')
#element1.send_keys("hello_word")
#print(element1)

#2 > Xpath
#element2 = driver.find_element('xpath', "//input[@type='search']")
#print(element2)
#assert element1 == element2

#element3 = driver.find_element('xpath',"//*[text()='Italiano']")
#element3.click()
# 3> tag
#element4 = driver.find_element('tag name', 'select')
#element4.click()
#sleep(3)

# 4 > link text or partional link text
#driver.find_element('partial link text', 'Download').click()

#5 > class name
#driver.find_element('class name','svg-search-icon').click()

#6 > css selector
#driver.find_element('css selector','.svg-search-icon').click()
#use id we have a #
#elemen5 = driver.find_element('css selector','#searchInput')
#elemen5.send_keys("fatemeh")
#sleep(5)

#driver.find_element('name', 'q')
#driver.execute_script("console.log('xx')")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#leep(2)

#current_path = Path(__file__).parent
#file_name = os.path.join(str(current_path), 'session2.png')
#driver.save_screenshot(file_name)
driver.get("http://192.168.2.183:8084/#/login")
driver.find_element('id', 'userRef').send_keys("aref@gmail.com")
driver.find_element('name', 'password').send_keys("123456")
driver.find_element('name', 'login').click()

