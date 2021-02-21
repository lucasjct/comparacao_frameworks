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
    #Fill Text           ${genero}           Masculino
    Click               ${select_pesquisa}
    CLick               ${select_option}
    
Submeter
    CLick               ${submit}