class Search:
    def __init__(self,drive):
        self.drive = drive
        self.address = 'https://www.anbient.com/anime'
        self.drive.get(self.address)



    def listar_anime(self):
        anime_list = []
        animes = self.drive.find_elements_by_tag_name('a')
        for anime in animes:
            name = anime.get_attribute('href')
            anime_list.append(name)
        return anime_list