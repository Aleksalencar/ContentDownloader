from selenium import webdriver
from page_objects import ZippysharePage as zip

d = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')

def donwload_zippy(ad):
    z = zip.Zippysahare(d)
    z.download(ad)
    pass

donwload_zippy('https://www40.zippyshare.com/v/hNfvlzb0/file.html')
