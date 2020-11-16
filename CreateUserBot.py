import names
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class CreateUserBot:
    DRIVER_PATH = 'chromedriver.exe'
    BASE_URL = "https://www.okcupid.com/"

    def __init__(self, email, password, headless=False):
        options = Options()
        options.headless = headless
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, executable_path=self.DRIVER_PATH)
        self.email, self.password = email, password
        self.first_name = names.get_first_name(gender='male')
        self.last_name = names.get_last_name()

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

    def initiate_profile_creation(self):
        self.driver.find_element_by_class_name('onboarding-stepIntro-button').click()
        time.sleep(5)

    def enter_first_name(self):
        self.driver.find_element_by_name('name').send_keys(self.first_name, Keys.RETURN)
        time.sleep(5)
        self.driver.find_element_by_class_name('profileDetails-button--next profileDetails-button--fixed').click()
        time.sleep(5)


if __name__ == '__main__':
    bot = CreateUserBot('randomemail758598@gmail.com', 'jsdjlkkjkljkl')
    bot.initiate_join()
    bot.enter_email()
    bot.enter_password()
    bot.initiate_profile_creation()
