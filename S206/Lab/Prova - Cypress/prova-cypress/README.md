# Prova Cypress - Demoblaze

Este projeto utiliza o Cypress para realizar testes automatizados de interface no site [Demoblaze](https://www.demoblaze.com/). Os testes cobrem funcionalidades de autenticação e carrinho de compras.

## Estrutura do Projeto

- `cypress/e2e/demoblaze/auth.cy.js`: Testes de autenticação (login válido e inválido).
- `cypress/e2e/demoblaze/cart.cy.js`: Testes de adição de produto ao carrinho.
- `cypress/fixtures/`: Dados de exemplo para testes.
- `cypress/support/`: Comandos customizados e configurações globais.

## Tecnologias Utilizadas
- [Cypress](https://www.cypress.io/) ^14.5.0
- [Mochawesome](https://github.com/adamgruber/mochawesome) (para relatórios)

## Instalação

1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd prova-cypress
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```

## Como executar os testes

1. Abra a interface do Cypress:
   ```bash
   npx cypress open
   ```
   Ou execute os testes em modo headless:
   ```bash
   npx cypress run
   ```

2. Selecione o teste desejado na interface ou aguarde a execução completa no terminal.

## Observações
- Os testes acessam o site público [Demoblaze](https://www.demoblaze.com/).
- Certifique-se de estar conectado à internet para rodar os testes.

---

Desenvolvido para fins de avaliação (Inatel - S206).