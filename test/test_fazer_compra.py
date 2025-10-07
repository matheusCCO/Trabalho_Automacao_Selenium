import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.preenche_informacao_pedido import PreencheInformacao
from pages.valida_informacao_pedido import ValidaPedido 

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestFazerCompra():
    def test_cazer_compra(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        informacao_pedido = PreencheInformacao()
        valida_pedido = ValidaPedido()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"
        nome="Lucas"
        sobrenome="Silva"
        cep= 99999999
        # Realiza o login
        login_page.fazer_login("standard_user", "secret_sauce")
        
        # Adiciona o primeiro item no carrinho
        home_page.adicionar_item_carrinho(produto_1)
        home_page.voltar_para_home_page()

        # Adiciona o Segundo item no carrinho
        home_page.adicionar_item_carrinho(produto_2)
        
        #Acessa o carrinho
        home_page.acessa_carrinho()

        #verifca os produtos no carrinho
        carrinho_page.verifica_item_carrinho(produto_1)
        carrinho_page.verifica_item_carrinho(produto_2)
        
        #Inicia o pedido
        carrinho_page.fazer_compar_item_carrinho()
        
        # Preenche as informações pessoais para o pedido
        informacao_pedido.preenche_informacao(nome,sobrenome,cep)
        
        # Valida o pedido 
        valida_pedido.verifica_informacao_pedido()
        
        # Valida se o pedido foi feito
        valida_pedido.finaliza_pedido()

 
        # driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        # driver.find_element(By.ID,"add-to-cart").click()
        # driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # driver.find_element(By.ID,"checkout").click()
        # driver.find_element(By.ID,"first-name").send_keys("Teste")
        # driver.find_element(By.ID,"last-name").send_keys("Teste")
        # driver.find_element(By.ID,"postal-code").send_keys("99999999")
        # driver.find_element(By.ID,"continue").click()

        # assert driver.find_element(By.XPATH, "//*[@class='title']").is_displayed()

        # driver.find_element(By.ID,"finish").click()

        # assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()