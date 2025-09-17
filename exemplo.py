# Testes de exemplo para fazer parecido IGNORAR
def test_login_valido(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("1234")
    time.sleep(1)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert message == "Login bem-sucedido!"

def test_login_invalido(driver):
    driver.find_element(By.ID, "username").send_keys("admin1")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("2626")
    time.sleep(1)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert message == "Usuário ou senha incorretos."

def test_checkboxs(driver):
    cb1 = driver.find_element(By.ID, "cb1")
    cb2 = driver.find_element(By.ID, "cb2")
    cb3 = driver.find_element(By.ID, "cb3")

    #SElecionar cada Checkbox
    cb1.click()
    time.sleep(1)
    cb2.click()
    time.sleep(1)
    cb3.click()
    time.sleep(1)

    assert cb1.is_selected() and cb2.is_selected() and cb3.is_selected()

def test_radiobuttons(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    radios = driver.find_elements(By.NAME, "gender")

    #Selecionar Feminino
    for radio in radios:
        if radio.get_attribute("value") == "Feminino":
            radio.click()
            time.sleep(1)
            assert radio.is_selected()
    
    for radio in radios:
        if radio.get_attribute("value") == "Masculino":
            radio.click()
            time.sleep(1)
            assert radio.is_selected()

    for radio in radios:
        if radio.get_attribute("value") == "Outro":
            radio.click()
            time.sleep(1)
            assert radio.is_selected()

def test_dropdown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    select = Select(driver.find_element(By.ID, "country"))
    time.sleep(1)
    select.select_by_visible_text("Brasil")
    time.sleep(1)
    assert select.first_selected_option.text == "Brasil"

    
def test_formulario_campos_obrigatorios(driver):
    driver.find_element(By.ID, "nome").clear()
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "mensagem").clear()
    time.sleep(1)
    driver.find_element(By.ID, "assunto").find_element(By.CSS_SELECTOR, "option[value='0']").click()
    time.sleep(1)
    driver.find_element(By.ID, "btn-envio").click()
    time.sleep(1)
    mensagem_clique = driver.find_element(By.ID, "mensagem-clique")
    assert mensagem_clique.text == "Preencha todos os campos!"
    assert "text-danger" in mensagem_clique.get_attribute("class")


def test_formulario_selecao_assunto(driver):
    driver.find_element(By.ID, "assunto").find_element(By.CSS_SELECTOR, "option[value='3']").click()
    time.sleep(1)
    assunto = driver.find_element(By.ID, "assunto")
    assert assunto.get_attribute("value") == "3"
