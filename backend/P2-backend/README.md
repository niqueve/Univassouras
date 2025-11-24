# Backend com PHP, Docker e Laravel

O projeto consiste em um sistema de gerenciamento de Categorias (CRUD) utilizando **Laravel** containerizado com **Docker**.

## Tecnologias Utilizadas

* **Linguagem:** PHP 8.2
* **Framework:** Laravel 10/11
* **Banco de Dados:** MySQL 8.0
* **Infraestrutura:** Docker & Docker Compose
* **Frontend:** Blade Templates + Bootstrap 5

## Estrutura do Projeto

A estrutura foi organizada para separar a infraestrutura da aplicação:

* `compose.yaml`: Orquestração dos containers (App e Banco).
* `Dockerfile`: Definição da imagem do servidor PHP com extensões necessárias.
* `src/`: Pasta contendo todo o código fonte do projeto Laravel.

## Pré-requisitos

* Docker Desktop instalado e rodando.
* Git (opcional, para clonar).

## Como Rodar o Projeto


### 1. Subir os Containers
No terminal, dentro da pasta raiz do projeto:

```bash
docker compose up -d --build
```

### 2. Configuração Inicial do Laravel
Após subir os containers, execute os comandos abaixo para configurar o ambiente.

```bash
# 1. Instalar dependências do PHP (caso a pasta vendor não exista)
docker compose exec app composer install

# 2. Copiar o arquivo de ambiente
docker compose exec app cp .env.example .env

# 3. Gerar a chave de criptografia do Laravel
docker compose exec app php artisan key:generate

# 4. Dar permissão de escrita nas pastas de log e cache (Evita Erro 500)
docker compose exec app chmod -R 777 storage bootstrap/cache

```
### 3. Banco de dados
O container do banco de dados já está configurado no compose.yaml. Para criar as tabelas:

```bash
# Rodar as migrations
docker-compose exec app php artisan migrate
```

## Acessando a Aplicação
Após a configuração, o projeto estará disponível em:

URL Principal: http://localhost:8000

Listagem de Categorias: http://localhost:8000/categorias


***A URL principal redireciona automaticamente para a listagem de categorias*