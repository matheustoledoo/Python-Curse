from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cria uma instância do navegador Firefox para automação
driver = webdriver.Firefox()

# Abre uma página específica no navegador
driver.get("http://somedomain/url_that_delays_loading")

try:
    # Aguarda até que um elemento com ID "myDynamicElement" esteja presente no DOM
    # - WebDriverWait(driver, 10): Define um tempo máximo de espera de 10 segundos.
    # - until(EC.presence_of_element_located): Espera até que a condição seja verdadeira,
    #   neste caso, que o elemento esteja presente no DOM.
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    # Fecha o navegador, independentemente de sucesso ou erro no bloco try.
    driver.quit()


#Esperas implícitas
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
