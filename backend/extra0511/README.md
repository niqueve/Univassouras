### Atividade Extra - P2

#### Objetivo

Desenvolver uma aplicação simples em PHP que permita enviar informações de usuários (nome e e-mail) via formulário e armazenar esses dados no MySQL, utilizando Docker Compose para orquestrar os containers.

#### Como usar

* Clone este repositório

* Abra o terminal e digite o comando: 
docker compose up --build

* Acesse em:
http://localhost:8081

* Para acessar e visualizar  o banco de dados
docker compose exec db mysql -u user -p 1234 aula_php