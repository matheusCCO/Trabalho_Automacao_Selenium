import conftest
from pages.base_page import BasePage
from pages.login_page import By

class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//*[@class='title']")
        self.item = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.btn_adicionar_carrinho = (By.ID,"add-to-cart")
        self.carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")
        self.item_carrinho = (By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']")
        self.btn_voltar = (By.ID, "back-to-products")

    def verificar_login_sucesso(self):
        self.vefificar_se_elemento_existe(self.titulo_pagina)
    
    def adicionar_item_carrinho(self, nome_item):
        item= (self.item[0],self.item[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.btn_adicionar_carrinho)
    
    def acessa_carrinho(self):
        self.clicar(self.carrinho)
    
    def voltar_para_home_page(self):
        self.clicar(self.btn_voltar)






