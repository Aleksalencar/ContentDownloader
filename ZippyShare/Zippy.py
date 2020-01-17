from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')

def zippidownload(addres):
    driver.get(addres)
    driver.implicitly_wait(10)
    dlbutton = driver.find_elements_by_id('dlbutton')
    dl = dlbutton[0].get_attribute('href')
    print(dl)
    driver.get(dl)
    pass



driver.get('https://www.anbient.com/anime/hibike-euphonium-2')
elements = driver.find_elements_by_tag_name('a')
episode_list = []
for element in elements:
    episode = element.get_attribute('href')
    if episode is not None and 'zippyshare.com/' in episode:
        episode_list.append(episode)
        pass
    pass
print(episode_list)
for episode in episode_list:
   try:
    zippidownload(episode)
    pass
   except:
       print("fail")
       pass
   pass
driver.get('chrome://downloads')