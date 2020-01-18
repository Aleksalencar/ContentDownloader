class Zippysahare:

    def __init__(self, address, driver):
        self.address = address
        self.driver = driver
        self.retry = 0

    def download(self):
        try:
            self.driver.get(self.address)
            self.driver.implicitly_wait(10)
            dlbutton = self.driver.find_elements_by_id('dlbutton')
            for btn in dlbutton:
                dl = btn.get_attribute('href')
                if dl is not None:
                    self.driver.get(dl)
                    print(dl)
            dl = str(dl)
            print("sucesso no download de ", dl)
        except Exception as e:
            print("falha no download de ", self.address," devido a ", e)
