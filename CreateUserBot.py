import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

class CreateUserBot:
    DRIVER_PATH = 'chromedriver.exe'
    BASE_URL = "https://www.okcupid.com/"

    def __init__(self, email, password, headless=False):
        options = Options()
        options.headless = headless
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, executable_path=self.DRIVER_PATH)
        self.email, self.password = email, password

    def initiate_join(self):
        self.driver.get(self.BASE_URL)
        time.sleep(5)
        try:
            self.driver.find_element_by_id('onetrust-accept-btn-handler').click()
        except ElementClickInterceptedException:
            pass
        self.driver.find_element_by_class_name('splashdtf-signup-button').click()
        time.sleep(5)

    def enter_email(self):
        self.driver.find_element_by_name('email').send_keys(self.email, Keys.RETURN)
        time.sleep(5)
        self.driver.find_element_by_class_name('signup2017-button').click()
        time.sleep(5)

    def enter_password(self):
        self.driver.find_element_by_name('password').send_keys(self.password, Keys.RETURN)
        time.sleep(5)
        self.driver.find_element_by_class_name('signup2017-button').click()
        time.sleep(5)



if __name__ == '__main__':
    bot = CreateUserBot('randomemail758598@gmail.com', 'jsdjlkkjkljkl')
    bot.initiate_join()
    bot.enter_email()
    bot.enter_password()
