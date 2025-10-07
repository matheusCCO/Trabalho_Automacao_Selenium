import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class PreencheInformacao(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.nome = (By.ID,"first-name")
        self.sobrenome = (By.ID,"last-name")
        self.cep = (By.ID,"postal-code")
        self.continuar = (By.ID, "continue")
    
    def preenche_informacao(self, nome, sobrenome, cep):
        self.escrever(self.nome, nome)
        self.escrever(self.sobrenome, sobrenome)
        self.escrever(self.cep, cep)
        self.clicar(self.continuar)
    
    def verifica_informacao_pedido(self):
        self.verifca_elemento_existe()