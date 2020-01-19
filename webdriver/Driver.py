import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expectedConditions
from selenium.webdriver.common.by import By


class Driver():

    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')



    def go_to_URL(self, url):
        self.driver.get(url)


    def WaitForElement(self, locator, By):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expectedConditions.visibility_of_element_located((By, locator)))
