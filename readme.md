## __Comparação entre Robot Framework e Selenium com Python.__  

<p>O objetivo é mostrar a diferença entre sintaxe e a utilização aplicada em determinados contextos.  O exemplo utilizado é o clássico preenchimento de fomrulário.</p>

<h2 style='text-align:center'>🚧 Em construção...  🚧</h2>   

***    

![Badge](https://img.shields.io/badge/Selenium-Python-blue)
![Badge](https://img.shields.io/badge/RobotFramework-Browser-brightgreen)    



### ROBOT FRAMEWORK

Tempo aproximado de execução: 11.5s   
Navegador: Chrome  


```PYTHON
*** Settings ***
Library         Browser

*** Variables ***
&{dados}                nome=Lucas  sobrenome=Texeira   email=teste@gmail.com   resumo=Automacao com RobotFramework
${nome}                 id=nome
${sobrenome}            id=sobrenome
${email}                id=email
${genero}               id=selecionar-genero
${resumo}               xpath=//textarea[@class='textarea']
${select_pesquisa}      id=inf-pesquisa
${select_option}        id=option-yes
${submit}               id=submit

*** Test Case ***
Cenário - Preencher Formulário
    Acessar Formulario
    Preencher Campos
    Submeter

*** Keywords ***
Acessar Formulario
    New Browser         chromium    headless=False
    New Page            http://127.0.0.1:5000/     

Preencher Campos
    Fill Text           ${nome}             ${dados.nome}
    Fill Text           ${sobrenome}        ${dados.sobrenome}
    Fill Text           ${email}            ${dados.email}
    Fill Text           ${resumo}           ${dados.resumo}
    #Fill Text          ${genero}           Masculino
    Click               ${select_pesquisa}
    CLick               ${select_option}

Submeter
    CLick               ${submit}

```   

### PYTHON COM SELENIUM    

Tempo aproximado de execução em localhost: 9.40s   
Navegador: Chrome  

```PYTHON
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
        
class PreencherFormulario(Locators):

    def preencher_campos(self, nome, sobrenome, email, genero, resumo):
        
        driver.find_element(*self.nome).send_keys(nome)
        driver.find_element(*self.sobrenome).send_keys(sobrenome)
        driver.find_element(*self.email).send_keys(email)
        #Select(find_element(*self.genero).select_by_visible_text(genero))
        driver.find_element(*self.resumo).send_keys(resumo)

    def marcar_campos_submeter(self):

        driver.find_element(*self.pesquisa).click()
        driver.find_element(*self.selecionar_sim).click()
        driver.find_element(*self.submeter).click()

    def encerrar_sessao(self):
        driver.quit()


driver  = webdriver.Firefox()
formulario = PreencherFormulario(driver)

formulario.preencher_campos('Teste', 'Selenium', 'teste@selenium.com', 
                            'selenium webdriver',"Testando aplicações com selenium")
formulario.marcar_campos_submeter()
formulario.encerrar_sessao()

```


Tempo aproximado de execução em localhost: 9.40s   
Navegador: Chrome  
### CYPRESS
```javascript

describe('Simples exemplo de uso Cypress', () => {

    it("Acessando o Formulário", () => {

      cy.visit('http://127.0.0.1:5000/')

      cy.title("Formulário Teste")

      cy.get('h2')
        .should('contain.text', 'Formulário para Teste')
    })

    it("Preenchendo os campos", () =>{

      cy.get('#nome').type("Lucas José")
      cy.get('#sobrenome').type('Carvalho Teixeira')
      cy.get('#email').type('lucasjcteixeira@gmail.com')

      cy.get("#selecionar-genero").select("Masculino")
      cy.get('.textarea').type("Lorem ipsum Lorem ipsum Lorem ipsum ")

      cy.get("#inf-pesquisa").check()
      cy.get(':nth-child(6) > .control > :nth-child(3)').click()
    })

    it("Validação Modal", () => {
      cy.get('#submit').click()
      cy.contains('Salvar').click()
  })
})


```