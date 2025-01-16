import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#A classe de caso de teste é herdada de unittest.TestCase . Herdar da classe TestCase é a maneira de informar ao módulo unittest que este é um caso de teste:
class PythonOrgSearch(unittest.TestCase):

    #criando uma instância de um Firefox WebDriver
    def setUp(self):
        self.driver = webdriver.Firefox()

    #método de caso de teste
    def test_search_in_python_org(self):
        driver = self.driver #firefox
        driver.get("http://www.python.org") #site que deseja ir
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()