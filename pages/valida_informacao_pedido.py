import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class ValidaPedido(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name']")
        self.finalizar = (By.ID,"finish")
        self.pedido_feito=(By.XPATH, "//*[@class='complete-header']")

    def verifica_informacao_pedido(self):
        self.verifca_elementos_existe(self.item_inventario)
        self.clicar(self.finalizar)
    
    def finaliza_pedido(self):
        self.verifca_elemento_existe(self.pedido_feito)