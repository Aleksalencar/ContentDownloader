from webdriver import Driver
from page_objects import ZippysharePage as zip
from page_objects import AnimePage as anime
from page_objects import SearchPage as search

d = Driver.Driver('D:\Downloads\Chrome', True)
s = search.Search(d.driver)


def donwload_zippy(ad):
    z = zip.Zippysahare(d.driver)
    z.download(ad)


def lista_zippy(ad):
    ad = str(ad)
    a = anime.Anime(ad, d.driver)
    zips = a.zippysahre_links()
    print('Inciando ', len(zips), ' downnloads de ', ad.split("/")[-1])
    return zips


def download_anime(anime):
    ad = anime[1]
    zip_ad = lista_zippy(ad)
    for zip in zip_ad:
        if zip is not None:
            donwload_zippy(zip)


def selection(anime_list):
    for i in range(len(anime_list)):
        print(i, " - ", anime_list[i][0])
    print("Selecione um indice: ")
    print('Digite "-1" para voltar')
    while True:
        choose = int(input())
        if choose == -1:
            search_for_anime()
        elif -1 < choose < len(anime_list):
            return anime_list[choose]
        else:
            print('Escolha invalida!')


def anime_chooser(anime_list):
    if len(anime_list) != 0:
        return selection(anime_list)
    else:
        print("Nada foi encontrado")
        search_for_anime()


def search_for_anime():
    print('Digite o termo para a busca de um anime: ')
    key = input()
    s.search(key)
    anime_list = s.list_result()
    anime = anime_chooser(anime_list)
    download_anime(anime)


search_for_anime()
