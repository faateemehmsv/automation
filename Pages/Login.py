from locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', email_input_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('name', password_input_name).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element('name', login_button_name).click()
