from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from Pages.MainPage import MainPage
from Pages.Login import Login
from Pages.AlphaPlan import AlphaPlan
import unittest


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_option = Options()
        #cls.driver = Service(executable_path='c:\chromedriver.exe')
        cls.driver = webdriver.Chrome(executable_path='c:\chromedriver.exe', chrome_options=cls.chrome_option)
        cls.action = ActionChains(cls.driver)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("http://192.168.2.183:8084/#/login")
        # create obj1 that name Login and object2 that name MainPage
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        alpha_plan = AlphaPlan(driver=self.driver)
        login.enter_username("aref@gmail.com")
        login.enter_password("123456")
        login.click_on_login_button()
        main_page.check_main_page()
        alpha_plan.click_to_AlphaPlan()

        sleep(3)







    '''
    def test_invalid_login(self):
        self.driver.get("http://192.168.2.183:8084/#/login")
        # create obj1 that name Login and object2 that name MainPage
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("aref@gmail.com")
        login.enter_password("123")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(3)
    '''
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()