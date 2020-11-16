import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CreateUserBot:
    DRIVER_PATH = 'chromedriver.exe'
    BASE_URL = "https://www.okcupid.com/"

    def __init__(self, email, headless=False):
        options = Options()
        options.headless = headless
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, executable_path=self.DRIVER_PATH)
        self.email = email

    def initiate_join(self):
        self.driver.get(self.BASE_URL)
        time.sleep(5)
        self.driver.find_element_by_class_name('splashdtf-signup-button').click()
        time.sleep(5)

    def enter_email(self):
        self.driver.find_element_by_name('email').send_keys(self.email)
        time.sleep(5)
        self.driver.find_element_by_class_name('signup2017-button').click()


if __name__ == '__main__':
    bot = CreateUserBot('randomemail758598@gmail.com')
    bot.initiate_join()
    bot.enter_email()
