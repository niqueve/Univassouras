## Atividade 2 - P2

# Projeto

Este repositório contém um projeto Laravel (ou esqueleto). Para facilitar a demonstração rápida, adicionei um modo Docker leve que exibe a mensagem "Ola Mundo" sem precisar instalar dependências PHP/Composer.

## Rodar com Docker Compose (modo rápido "Ola Mundo")

1. Certifique-se de ter Docker e Docker Compose instalados.
2. No diretório do projeto, execute:

```bash
docker compose up --build
```

3. Abra http://localhost:8000 no seu navegador. Você deverá ver a mensagem:

```
Ola Mundo
```

Observações:
- A resposta "Ola Mundo" é produzida por uma verificação simples em `public/index.php` ativada pela variável de ambiente `SHOW_OLA_MUNDO`.
- Este modo é destinado a demonstrações rápidas. Para um ambiente Laravel completo, instale as dependências (composer install, etc.) e configure um servidor web apropriado.