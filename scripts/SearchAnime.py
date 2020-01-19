from selenium import webdriver
from page_objects import ZippysharePage as zip
from page_objects import SearchPage as search

d = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')

s = search.Search(d)

s.search('kono oto')
#print(s.listar_anime())