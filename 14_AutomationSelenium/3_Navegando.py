from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.python.org")
select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
# select.deselect_all() #desmarcar todas as opções selecionadas

# Suponha que em um teste precisamos da lista de todas as opções selecionadas padrão.
# A classe Select fornece um método de propriedade que retorna uma lista:
select = Select(driver.find_element(By.XPATH, "//select[@name='name']"))
all_selected_options = select.all_selected_options

#Para obter todas as opções disponíveis:
options = select.options

#para enviar um formulario ou apenas clicar
driver.find_element(By.ID, "submit").click()


#Você pode usar arrastar e soltar, movendo um elemento por uma certa quantidade ou para outro elemento:

element = driver.find_element(By.NAME, "source") #elemento a se mover
target = driver.find_element(By.NAME, "target") #elemento onde vai ir o que quer se mover

from selenium.webdriver import ActionChains #chama a biblioteca
action_chains = ActionChains(driver) #instancia
action_chains.drag_and_drop(element, target).perform() #move de um para o outro



