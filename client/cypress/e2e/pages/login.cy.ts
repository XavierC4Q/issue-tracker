/// <reference types="cypress" />

context('Login Page', () => {
  it('Navigates to Login page', () => {
    cy.visit('http://localhost:3000/login');

    cy.get('div').contains('Login Here');

  });
});