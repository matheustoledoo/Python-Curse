from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() #escolhe qual o browser vai utilizar
driver.get("http://www.python.org") #escolhe qual o site
assert "Python" in driver.title #opcional: para identificar se o titulo coincide com 'python'
elem = driver.find_element(By.NAME, "q") #preucura po elementos por nome que equivalem a 'q'
elem.clear() #limpar ualquer texto pré-preenchido no campo de entrada (por exemplo, “Pesquisar”)
elem.send_keys("pycon") #troca por pycom
elem.send_keys(Keys.RETURN) #retorna essa chave pedida
assert "No results found." not in driver.page_source #caso nao encontre
