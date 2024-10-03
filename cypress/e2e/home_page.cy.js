
describe('My first e2e test', () => {
    it('Should show that H1 title contains question text', () => {
        cy.visit('http://localhost:8000/polls')
        cy.contains('What\'s up').click()
        cy.get('h1').should('contain', 'What\'s up')
    })

    it('Should list all the choices for the question', () => {
        cy.visit('http://localhost:8000/polls')
        cy.contains('What\'s up').click()
        cy.get('label').should('contain', 'Not much')
        cy.get('label').should('contain', 'The sky')
    })

    it('Should allow selecting a choice', () => {
        cy.visit('http://localhost:8000/polls')
        cy.contains('What\'s up').click()
        cy.get('input[type="radio"]').first().check()
        cy.get('input[type="radio"]').first().should('be.checked')
    })
})