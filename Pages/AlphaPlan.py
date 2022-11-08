from locators import clickAlphaPlan


class AlphaPlan:
    def __init__(self, driver):
        self.driver = driver

    def click_to_AlphaPlan(self):
        self.driver.find_element('class name', clickAlphaPlan)
