from webdriver import Driver
from page_objects import SearchPage
d = Driver.Driver()
key = 'kono oto'

s = SearchPage.Search(d.driver,key)
s.list_result()



