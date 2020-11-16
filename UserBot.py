import datetime
import random
import time

import names
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class UserBot:
    DRIVER_PATH = 'chromedriver.exe'
    BASE_URL = "https://www.okcupid.com/"

    def __init__(self, email, password, age=None, gender='Man', headless=False, created=False):
        if not created:
            options = Options()
            options.headless = headless
            options.add_argument("start-maximized")
            self.driver = webdriver.Chrome(options=options, executable_path=self.DRIVER_PATH)
            self.email, self.password, self.gender, self.age = email, password, gender, age
            self.first_name = names.get_first_name(gender='male')
            start_dt = datetime.datetime.now() - datetime.timedelta(days=(age + 1) * 365)
            end_dt = datetime.datetime.now() - datetime.timedelta(days=age * 365)
            self.birth_date = self.random_date(start_dt, end_dt)

    @staticmethod
    def random_date(start_dt, end_dt):
        time_between_dates = end_dt - start_dt
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_dt + datetime.timedelta(days=random_number_of_days)
        return random_date

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

    def enter_gender(self):
        if self.gender == 'Man':
            self.driver.find_element_by_xpath(
                '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/label[2]').click()
        elif self.gender == 'Woman':
            self.driver.find_element_by_xpath(
                '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/label[1]').click()
        else:
            exit('Invalid Gender')
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/div/div[3]/button').click()
        time.sleep(5)

    def enter_birth_date(self):
        month = self.birth_date.strftime('%B')
        day = self.birth_date.day
        year = self.birth_date.year
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/div/div[1]/label/select').click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/div/div[1]/label/select').send_keys(
            month)
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/div/div[2]/label/select').click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/div/div[2]/label/select').send_keys(
            day)
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/div/div[3]/label/select').click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/div/div[3]/label/select').send_keys(
            year, Keys.RETURN)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/div/div[3]/button').click()
        time.sleep(5)


if __name__ == '__main__':
    bot = UserBot('randomemail758598@gmail.com', 'jsdjlkkjkljkl', age=23)
    bot.initiate_join()
    bot.enter_email()
    bot.enter_password()
    bot.initiate_profile_creation()
    bot.enter_first_name()
    bot.enter_gender()
    bot.enter_birthdate()
