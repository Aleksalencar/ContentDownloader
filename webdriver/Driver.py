import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By as hue


class Driver():

    def __init__(self):
        path = 'C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe'
        self.options = self.configuration()
        self.driver = webdriver.Chrome(executable_path=path,chrome_options=self.options)

    def configuration(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "D:\Downloads\Chrome"}
        chromeOptions.add_experimental_option("prefs", prefs)
        return chromeOptions

    def go_to_URL(self, url):
        self.driver.get(url)


    def wait_element(self, by, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(by, element))

    def minimize(self):
        self.driver.minimize_window()