class AllAnimesSearch():
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://www.anbient.com/anime')

    def listar_anime(self):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        anime_list = []
        content_Xpath = "https://www.anbient.com/anime"
        wait = WebDriverWait(self.driver, 10)
        animes = wait.until(EC.presence_of_element_located((By.XPATH, content_Xpath)))
        for anime in animes:
            name = anime.text
            link = anime.get_attribute('href')
            content = [name, link]
            anime_list.append(content)
        return anime_list

    def search(self, key):
        search_box = self.driver.find_element_by_id('edit-title')
        search_box.clear()
        search_box.send_keys(key)
        self.apply()
        pass

    def apply(self):
        apply_btn = self.driver.find_element_by_id('edit-submit-animes')
        apply_btn.click()
        pass