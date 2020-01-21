import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By as hue


class Driver():

    def __init__(self,d_path):
        root = os.path.dirname(os.path.abspath(__file__))
        path = root + "\\chromedriver.exe"
        if d_path is not None:
            options = self.configuration(d_path)
        self.driver = webdriver.Chrome(executable_path=path,chrome_options=options)

    def configuration(self,d_path):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": d_path}
        chromeOptions.add_experimental_option("prefs", prefs)
        return chromeOptions

    def go_to_URL(self, url):
        self.driver.get(url)


    def wait_element(self, by, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(by, element))

    def minimize(self):
        self.driver.minimize_window()