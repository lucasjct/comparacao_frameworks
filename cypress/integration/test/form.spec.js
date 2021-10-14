/// <reference types="cypress" />


describe('Simples exemplo de uso Cypress', () => {

    it("Acessando o Formulário", () => {

      cy.visit('http://127.0.0.1:5000/')

      cy.title("Formulário Teste")

      cy.get('h2')
        .should('contain.text', 'Formulário para Teste')
    })

    it("Preenchendo os campos", () => {

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
