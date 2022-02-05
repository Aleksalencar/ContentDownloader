from selenium import webdriver
from page_objects import ZippysharePage as zip


def donwload_zippy(ad):
    z = zip.Zippysahare(ad)
    z.download(ad)
    pass

donwload_zippy('https://www40.zippyshare.com/v/hNfvlzb0/file.html')
