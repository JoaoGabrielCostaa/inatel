describe('Testes no site Demoblaze - Autenticação', () => {
  const username = 'TestUser_Inatel_JoaoGabriel';
  const password = 'TestPassword';

  beforeEach(() => {
    cy.visit('https://www.demoblaze.com/index.html');
  });

  it('Login com sucesso', () => {
    login(username, password);
    cy.contains(`Welcome ${username}`).should('be.visible');
  });

  it('Login inválido (negativo)', () => {
    login('UsuarioInvalido', 'SenhaErrada');
    cy.on('window:alert', (str) => {
      expect(str).to.contain('User does not exist');
    });
  });
});

describe('Testes no site Demoblaze - Carrinho de compras', () => {

  beforeEach(() => {
    cy.visit('https://www.demoblaze.com/index.html');
  });

  it('Adicionar produto ao carrinho', () => {
    cy.contains('Samsung galaxy s6').click();
    cy.contains('Add to cart').click();
    cy.on('window:alert', (str) => {
      expect(str).to.equal('Product added.');
    });
    cy.get('.navbar-nav').contains('Cart').click();
    cy.contains('Samsung galaxy s6').should('be.visible');
  });
});


function login(username, password) {
  cy.get('#login2').click();
  cy.wait(1000);
  cy.get('#loginusername').type(username);
  cy.get('#loginpassword').type(password);
  cy.get('button[onclick="logIn()"]').click();
}

