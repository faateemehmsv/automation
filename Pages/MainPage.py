from locators import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        #self.driver.find_element('class name', admin_class_name)
        self.driver.find_element('class name', clickAlphaPlan)

