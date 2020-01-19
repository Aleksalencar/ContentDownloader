class Search:
    def __init__(self,drive):
        self.drive = drive
        self.drive.get('https://www.anbient.com/anime')

    def listar_anime(self):
        self.driver.implicitly_wait(10)
        anime_list = []
        animes = self.driver.find_elements_by_xpath('//*[@id="animes"]/div[2]/article/div[2]/h2/a')
        for anime in animes:
            name = anime.text
            link = anime.get_attribute('href')
            content = [name, link]
            anime_list.append(content)
        return anime_list

    def search(self, key):

        pass

    def apply(self):
        apply_btn = self.driver.find_element_by_id('edit-submit-animes')
        apply_btn.click()
        self.driver.implicitly_wait(10)
        pass