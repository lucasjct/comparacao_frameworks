from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PreencherFormulario():

    def __init__(self, nome, sobrenome, email, text_area, genero):

        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.text_area = text_area
        self.genero = genero

    def setUp(self):

        self.driver  = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:5000/")

    def preencher_campos(self):

        self.driver.find_element_by_xpath('//*[@id="nome"]').send_keys(self.nome)
        self.driver.find_element_by_id('sobrenome').send_keys(self.sobrenome)
        self.driver.find_element_by_id('email').send_keys(self.email)
        Select(self.driver.find_element_by_id("selecionar-genero")).select_by_visible_text(self.genero)
        self.driver.find_element_by_class_name('textarea').send_keys(self.text_area)

    def marcar_campos_submeter(self):

        self.driver.find_element_by_id("inf-pesquisa").click()
        self.driver.find_element_by_id("option-yes").click()
        self.driver.find_element_by_id("submit").click()

    def encerrar_sessao(self):
        self.driver.close()

formulario = PreencherFormulario('Lucas José', "Carvalho Teixeira", 
                                'teste@gmail.com', 'Teste Selenium com Python','Masculino')

formulario.setUp()
formulario.preencher_campos()
formulario.marcar_campos_submeter()
formulario.encerrar_sessao()