import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    #setup
    global driver
    options = Options()
    options.add_argument("--incognito")  # Abre o Chrome em modo anônimo
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # reun test
    yield

    # teardown
    driver.quit()