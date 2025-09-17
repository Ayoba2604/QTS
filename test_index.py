import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#caso precise:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


URL = "C:\\Users\\20231350328\\Documents\\ExProva_Selenium\\index.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


def test_formulario_preenchimento_e_envio(driver):
    driver.find_element(By.ID, "nome").send_keys("Teste Nome")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("teste@email.com")
    time.sleep(1)
    driver.find_element(By.ID, "assunto").find_element(By.CSS_SELECTOR, "option[value='2']").click()
    time.sleep(1)
    driver.find_element(By.ID, "mensagem").send_keys("Mensagem de teste.")
    time.sleep(1)
    driver.find_element(By.ID, "btn-envio").click()
    time.sleep(1)
    mensagem_clique = driver.find_element(By.ID, "mensagem-clique")
    assert mensagem_clique.text == "Informações enviadas com sucesso!"
    assert "text-success" in mensagem_clique.get_attribute("class")


