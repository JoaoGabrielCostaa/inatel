# S206 - Prova Postman API 2025 - JSONPlaceholder

Este projeto contém uma coleção do Postman para testar a API pública JSONPlaceholder. A coleção inclui exemplos de requisições GET e POST, além de um teste negativo.

## Como usar

1. Importe o arquivo `Collection.json` no Postman.
2. Execute as requisições conforme descrito abaixo.

## Endpoints da Coleção

### 1. GET - Listar Usuários
- **Método:** GET
- **URL:** `https://jsonplaceholder.typicode.com/users`
- **Descrição:** Retorna a lista de todos os usuários cadastrados na API.
- **Exemplo de uso:**
  - Basta enviar a requisição sem corpo ou parâmetros adicionais.

### 2. POST - Criar Postagem
- **Método:** POST
- **URL:** `https://jsonplaceholder.typicode.com/posts`
- **Headers:**
  - `Content-Type: application/json`
- **Body (raw):**
```json
{
  "title": "S206 Postagem de Teste",
  "body": "Conteúdo gerado na prova S206.",
  "userId": 1
}
```
- **Descrição:** Cria uma nova postagem associada ao usuário de ID 1.

### 3. GET - Usuário Inexistente (Negativo)
- **Método:** GET
- **URL:** `https://jsonplaceholder.typicode.com/users/9999`
- **Descrição:** Tenta buscar um usuário que não existe. Deve retornar uma resposta vazia ou erro, útil para testar cenários negativos.

## Observações
- A API JSONPlaceholder é pública e serve apenas para testes, não havendo persistência real dos dados enviados via POST.
- Foi utilizado a lib [Newman](https://www.npmjs.com/package/newman) para gerar o relatório final dos resultados dos testes que está localizado em (newman/newman-run-report-2025-06-19-14-59-39-570-0.html)

---

Qualquer dúvida, consulte a documentação oficial do [JSONPlaceholder](https://jsonplaceholder.typicode.com/).