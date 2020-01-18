class Anime:
    def __init__(self, address, driver):
        self.address = address
        self.driver = driver
        self.driver.get(self.address)


    def zippysahre_links(self):
        elements = self.driver.find_elements_by_xpath("//a[contains(@href, 'zippyshare.com/')]")
        episode_list = []
        for element in elements:
            episode = element.get_attribute('href')
            episode_list.append(episode)
        print(episode_list)
        return episode_list
