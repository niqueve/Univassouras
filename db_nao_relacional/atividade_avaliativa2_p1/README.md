# FastAPI Chat - Versão Refatorada

Este é um projeto de chat em tempo real desenvolvido com FastAPI, MongoDB e WebSockets, refatorado para seguir boas práticas de organização de código, modularidade e manutenibilidade.
Toda a aplicação é encapsulada em um container Docker, garantindo um ambiente de desenvolvimento padronizado e um processo de implantação (deploy) simplificado.

## Tecnologias Utilizadas

Backend: FastAPI

Comunicação Real-Time: WebSockets

Banco de Dados: MongoDB (com MongoDB Atlas)

Containerização: Docker & Docker Compose

Validação de Dados: Pydantic

Driver Assíncrono para DB: Motor

## Estrutura de Arquivos

O projeto está organizado da seguinte forma para separar as responsabilidades:

├── app/
│   ├── config.py         # Configurações via variáveis de ambiente
│   ├── database.py       # Conexão com o MongoDB
│   ├── models.py         # Modelos de dados (Pydantic)
│   ├── ws_manager.py     # Gerenciador de conexões WebSocket
│   ├── routes/
│   │   └── messages.py   # Rotas REST para mensagens
│   └── main.py           # Ponto de entrada da aplicação
│
├── static/
│   |── index.html
|   |__ script.js
|   |__ style.css
│
├── .env                  # Arquivo de configuração local (NÃO versionar)
├── requirements.txt      # Dependências Python
|__ compose.yaml
|__ Dockerfile
|
└── README.md             # Este arquivo

## Como Rodar o Projeto

### Pré-requisitos
- Python 3.9+
- Uma conta no MongoDB Atlas (ou um servidor MongoDB local)

### Passo a passo
1- Baixe ou clone os arquivos deste repositório
2- Configure as Variáveis de Ambiente
*A aplicação precisa da sua string de conexão do MongoDB Atlas para funcionar.

- Crie o arquivo .env na raiz do projeto;
- Adicione suas credenciais ao arquivo .env
- Suba o Container com Docker Compose

* A aplicação ficará disponível em: http://localhost:8000/