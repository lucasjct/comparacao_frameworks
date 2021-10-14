from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Locators():
    def __init__(self, driver):
            
        self.nome = (By.XPATH,'//*[@id="nome"]')
        self.sobrenome = (By.ID, 'sobrenome')
        self.email = (By.ID,'email')
        self.genero = (By.ID,"selecionar-genero")
        self.resumo = (By.CLASS_NAME,'textarea')
        self.pesquisa = (By.ID,"inf-pesquisa")
        self.selecionar_sim = (By.ID,"option-yes")
        self.submeter = (By.ID,'submit')
        driver.get("http://127.0.0.1:5000/")
        
class TestFormulario(Locators):

    def test_preencher_campos(self, nome, sobrenome, email, genero, resumo):
        
        driver.find_element(*self.nome).send_keys(nome)
        driver.find_element(*self.sobrenome).send_keys(sobrenome)
        driver.find_element(*self.email).send_keys(email)
        #Select(find_element(*self.genero).select_by_visible_text(genero))
        driver.find_element(*self.resumo).send_keys(resumo)

    def test_marcar_campos_submeter(self):

        driver.find_element(*self.pesquisa).click()
        driver.find_element(*self.selecionar_sim).click()
        driver.find_element(*self.submeter).click()

    def encerrar_sessao(self):
        driver.quit()


driver  = webdriver.Chrome()
formulario = TestFormulario(driver)

formulario.test_preencher_campos('Teste', 'Selenium', 'teste@selenium.com', 
                                'selenium webdriver',"Testando aplicações com selenium")
formulario.test_marcar_campos_submeter()
formulario.encerrar_sessao()