from selenium import webdriver
from page_objects import ZippysharePage as zip
from page_objects import AnimePage as anime

d = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')


def donwload_zippy(ad):
    z = zip.Zippysahare(ad,d)
    z.download()
    pass
def lista_zippy(ad):
    a = anime.Anime(ad,d)
    return a.zippysahre_links()

def download_anime(ad):
    zip_ad = lista_zippy(ad)
    for zip in zip_ad:
        donwload_zippy(zip)
        pass
    pass


download_anime('https://www.anbient.com/anime/Sakamoto-desu-ga')
