
import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.user_field = (By.ID,"user-name")
        self.senha_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.erro_mensagem_login = (By.XPATH, "//*[text()='Epic sadface: Username and password do not match any user in this service']")
        
    def fazer_login(self, user, senha):
        self.escrever(self.user_field, user)
        self.escrever(self.senha_field, senha)
        self.clicar(self.login_button)

    def verifcar_mansagem_erro_login_existe(self):
        self.vefificar_se_elemento_existe(self.erro_mensagem_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.erro_mensagem_login)
        assert texto_encontrado == texto_esperado, f"o texto retornado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'"