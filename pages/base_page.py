from xml.dom.minidom import Element
import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time
class BasePage:
    def __init__(self):
        self.driver = conftest.driver
    
    def encontar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        self.encontar_elemento(locator).send_keys(text)
        self.espera()
    
    def clicar(self, locator):
        self.encontar_elemento(locator).click()
        self.espera()
    
    def verificar_se_elemento_existe(self, locator): 
        assert self.encontar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        self.espera_elemento_aparecer(locator)
        return self.encontar_elemento(locator).text
    
    def espera_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(*locator))
    
    def verifca_elemento_existe(self,  locator):
        assert self.encontar_elemento(locator), f"Elemento '{locator}', não existe na tela"

    def verifca_elemento_nao_existe(self,  locator):
        assert len(self.encontar_elementos(locator)) == 0, f"Elemento '{locator}', existe na tela"
    
    def verifca_elementos_existe(self,  locator):
        assert len(self.encontar_elementos(locator)) > 0, f"Elemento '{locator}', não existe na tela"

    

    def espera(self, timeout=2):
        time.sleep(timeout)

