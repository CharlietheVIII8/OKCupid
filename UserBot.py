import datetime
import random
import time

import names
from Photo import Photo
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class UserBot:
    DRIVER_PATH = 'chromedriver.exe'
    BASE_URL = "https://www.okcupid.com/"
    GENERATED_PHOTOS_API_KEY = 'h839ZfTUYsDmet4_iY6Adg'

    def __init__(self, email, password, age=None, gender='Man', headless=False, created=False, country="Canada",
                 zip_code=None, city='Toronto', looking_for='Women'):
        if not created:
            options = Options()
            options.headless = headless
            options.add_argument("start-maximized")
            self.driver = webdriver.Chrome(options=options, executable_path=self.DRIVER_PATH)
            self.email, self.password, self.gender, self.age, self.country, self.zip_code = email, password, gender, \
                                                                                            age, country, zip_code
            self.first_name = names.get_first_name(gender='male')
            start_dt = datetime.datetime.now() - datetime.timedelta(days=(age + 1) * 365)
            end_dt = datetime.datetime.now() - datetime.timedelta(days=age * 365)
            self.birth_date = self.random_date(start_dt, end_dt)
            self.city = city
            self.looking_for = looking_for
            self.photo = Photo(gender, age)

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

    def enter_living_info(self):
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/span/div[2]/div[1]/label/select'). \
            click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/span/div[2]/div[1]/label/select'). \
            send_keys(self.country)
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div[1]/div/div/div/div/div/span/div[2]/div[2]/span[2]/input') \
            .send_keys(self.city, Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/div/div[3]/button').click()
        time.sleep(5)

    def initiate_preferences(self):
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/button')
        time.sleep(5)

    def enter_connections(self):
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/button[1]'). \
            click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/button[2]'). \
            click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/button[3]'). \
            click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/button[4]'). \
            click()
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/div/div/div/button').click()
        time.sleep(5)

    def enter_desired_mate(self):
        if self.looking_for == 'Women':
            self.driver.find_element_by_xpath(
                '//*[@id="main_content"]/div[1]/span/div/div/div' +
                '/div/div[1]/div/div/div/div/div[1]/div/div/div/button[2]').click()
        elif self.looking_for == 'Men':
            self.driver.find_element_by_xpath(
                '//*[@id="main_content"]/div[1]/span/div/div/div/' +
                'div/div[1]/div/div/div/div/div[1]/div/div/div/button[1]').click()
        else:
            exit('Invalid Desired Mate')
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/div/div/div/button[2]').click()
        time.sleep(5)

    def enter_desired_age(self):
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/label[1]/select').click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/label[1]/select').send_keys(
            '18')
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/label[2]/select').click()
        self.driver.find_element_by_xpath(
            '//*[@id="main_content"]/div[1]/span/div/div/div/div/div[1]/div/div/div/div/label[2]/select').send_keys(
            '99')
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/div/div/div/button[2]').click()
        time.sleep(5)

    def initiate_tell_us_about_yourself(self):
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[1]/span/div/button').click()
        time.sleep(5)


def create_user_bot(email, password, age):
    bot = UserBot(email, password, age=age)
    bot.initiate_join()
    bot.enter_email()
    bot.enter_password()
    bot.initiate_profile_creation()
    bot.enter_first_name()
    bot.enter_gender()
    bot.enter_birth_date()
    bot.enter_living_info()
    bot.initiate_preferences()
    bot.enter_connections()
    bot.enter_desired_mate()
    bot.enter_desired_age()
    bot.initiate_tell_us_about_yourself()
    return bot


if __name__ == '__main__':
    bot = create_user_bot('randomemail758598@gmail.com', 'jsdjlkkjkljkl', age=23)
