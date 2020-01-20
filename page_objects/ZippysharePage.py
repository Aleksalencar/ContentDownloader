class Zippysahare:

    def __init__(self, driver):
        self.driver = driver
        self.retry = 0

    def download(self,address):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        try:
            self.driver.get(address)
            dlbutton = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.ID, "dlbutton")))
            dl = dlbutton.get_attribute('href')
            if dl is not None:
                self.driver.get(dl)
                dl = str(dl)
                print("Inicio no download de ", dl.split('/')[-1])
        except Exception as e:
            print("falha no download de ", address," devido a ", e)