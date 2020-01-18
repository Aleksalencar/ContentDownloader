from selenium import webdriver
from page_objects import ZippysharePage as zip
from page_objects import AnimePage as anime

d = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')

def lista_zippy(ad):
    a = anime.Anime(ad,d)
    return a.zippysahre_links()

lista_zippy('https://www.anbient.com/anime/Kono-Subarashii-Sekai-ni-Shukufuku-wo')