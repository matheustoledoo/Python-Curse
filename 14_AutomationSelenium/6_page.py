#Classes de objetos de página
from element import BasePageElement  # Importa a base para elementos personalizados na página.
from locators import MainPageLocators  # Importa os localizadores (provavelmente constantes definidas em outro arquivo).

class SearchTextElement(BasePageElement):
    """Esta classe encapsula o campo de texto de pesquisa."""

    # Localizador do campo de busca. Geralmente, 'q' é usado como nome do parâmetro de pesquisa (ex: Google).
    locator = 'q'


class BasePage(object):
    """Classe base que inicializa o driver e será usada como base para todas as páginas."""

    def __init__(self, driver):
        # Recebe o driver (Selenium WebDriver) para interagir com a página.
        self.driver = driver


class MainPage(BasePage):
    """Define métodos específicos para a página principal."""

    # Declara um elemento de busca que será manipulado diretamente
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifica se o título da página contém a palavra 'Python'."""

        # Retorna True se "Python" estiver no título da página.
        return "Python" in self.driver.title

    def click_go_button(self):
        """Clica no botão 'GO' para iniciar a pesquisa."""

        # Busca o botão 'GO' usando um localizador definido em `MainPageLocators`.
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Define métodos para a página de resultados de busca."""

    def is_results_found(self):
        """Verifica se há resultados na página de pesquisa."""

        # Checa se a mensagem "No results found." NÃO está no conteúdo da página.
        # Se essa mensagem não estiver presente, assume-se que resultados foram encontrados.
        return "No results found." not in self.driver.page_source
