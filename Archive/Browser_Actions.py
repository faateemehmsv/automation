from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(executable_path = 'c:\chromedriver.exe')
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#Browser Action 1 -> Open Web
driver.get("http://google.com")
sleep(2)
#Browser Action 2 -> title
#window_title = driver.title
print("window_title :", driver.title)
#Browser Action 3 -> Back
#driver.get("https://www.wikipedia.org/")
#sleep(4)
#driver.back()
#sleep(3)
#Browser Action 4 -> forward
#driver.forward()
#sleep(2)
#driver.find_element('name','q').send_keys("fatemeh")
#sleep(3)
#driver.quit()
#Browser Action 5 -> Refresh
#driver.refresh()
#Browser Action 6 -> Opern new window and switch to it (tab)
#driver.switch_to.new_window('tab')
#sleep(3)

#Browser Action 7 -> Opern new window and switch to it (window)
#driver.switch_to.new_window('window')
#driver.get('http://yahoo.com')
#sleep(3)

#Browser Action 8 -> current window
#yahoo_window = driver.current_window_handle
#print('yahoo handle' + str(yahoo_window))

#Browser Action 9 -> All windows or All handle
#all_handle = driver.window_handles
#print('all_handle' + str(all_handle))
#Browser Action  10 -> Switch
#driver.switch_to.window(all_handle[0])
#sleep(3)
#Browser Action  11 -> close Tab : close current urll
#driver.close()
#Browser Action  12 -> close Tab : close current urll
#driver.quit()

#Browser Action  13 -> windows size
window_size = driver.get_window_size() # {'width': 945, 'height': 1020}
print(window_size)
width = window_size['width']
print(width)
height = window_size['height']
print(height)


#Browser Action  14 -> set windows size
#driver.set_window_size(width=800, height=600)
#size = driver.get_window_size()
#assert size['width']== 800
#sleep(3)

#Browser Action  15 -> Chqnge window position
current_position = driver.get_window_position()
print(current_position)
sleep(3)

#Browser Action  16 -> set window position
driver.set_window_position(400,500)
sleep(3)
#assert driver.get_window_position()['x']==400

#Browser Action  17 ->  minimize window
driver.minimize_window()
sleep(2)
#Browser Action  18 -> maximize  window
driver.maximize_window()
sleep(2)

#Browser Action  19 -> Full screen  window
driver.fullscreen_window()
sleep(2)















