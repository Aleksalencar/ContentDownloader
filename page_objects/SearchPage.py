class Search:
    def __init__(self,driver, key):
        self.driver = driver
        self.driver.get('https://www.anbient.com/search?search_api_views_fulltext='+key)

    def list_result(self):
        results = self.driver.find_elements_by_xpath('//header/h2/a')
        content = self.get_content(results)
        print(content)
        return content

    def get_content(self, results):
        result_list = []
        for result in results:
            name = result.text
            link = result.get_attribute('href')
            content = [name, link]
            result_list.append(content)
        return result_list