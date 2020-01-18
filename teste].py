import os
from selenium import webdriver

chrome_path = 'C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/Driver.py'
chrome = webdriver.Chrome(chrome_path)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
chrome_path = str(ROOT_DIR+'webdriver\ChromeWebDriver.py')

print(chrome_path)
print('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/Driver.py')
