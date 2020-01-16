from selenium import webdriver


def download(addres):
    chrome.get(addres)
    dlbutton = chrome.find_elements_by_id('dlbutton')
    dl = dlbutton[0].get_attribute('href')
    print(dl)
    chrome.get(dl)
    pass




episode_list = input()
print(episode_list)
chrome = webdriver.Chrome('C:/Users/Aleksander/PycharmProjects/AnimeDownloader/webdriver/chromedriver.exe')
for episode in episode_list:
   try:
    download(episode)
    chrome.implicitly_wait(10)
   except:
       print("fail")