from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CreateUserBot:
    DRIVER_PATH = 'chromedriver.exe'
    BASE_URL = "https://www.okcupid.com/"

    def __init__(self, headless=False):
        options = Options()
        options.headless = headless
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, executable_path=self.DRIVER_PATH)

    def initiate_join(self):
        self.driver.get(self.BASE_URL)
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div/div/div[5]/a').click()


if __name__ == '__main__':
    bot = CreateUserBot()
    bot.initiate_join()
