<h1 align="center">TRANSFLOW</h1>

## Sobre

Gerenciador de corridas com processamento assíncrono que utiliza FastAPI, MongoDB, Redis, RabbitMQ e FastStream.

*Trabalho desenvolvido para a disciplina de Banco de Dados Não Relacional (NoSQL) da Universidade de Vassouras (Univassouras) - Campus Maricá.*


## Estrutura

```text
transflow/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── producer.py
│   ├── consumer.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── mongo_client.py
│   │   └── redis_client.py
│   └── models/
│       ├── __init__.py
│       └── corrida_model.py
│
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Passos de instalação

### 1- Clone este repositório
```bash
    git clone <seu-repositorio>
    cd transflow
```
### 2- Crie o arquivo .env
Copie o conteúdo da sessão "Variáveis de Ambiente" ou utilize o arquivo .env.example e o renomeie fazendo as alterações que julgar necessário.

### 3- Suba os containers
```bash
    docker-compose up --build
```

## Variáveis de ambiente necessárias
O sistema é configurado via um arquivo `.env` na raiz do projeto.

| Variável | Descrição | Valor Padrão (Docker) |
| :--- | :--- | :--- |
| `MONGO_URL` | Connection string para acesso ao MongoDB. O host `mongo` refere-se ao nome do serviço no compose.yaml. | `mongodb://mongo:27017/` |
| `REDIS_HOST` | Hostname do serviço Redis no Docker. | `redis` |
| `REDIS_PORT` | Porta padrão do serviço Redis. | `6379` |
| `RABBITMQ_URL` | String de conexão AMQP para o RabbitMQ. Inclui usuário, senha, host e porta. | `amqp://guest:guest@rabbitmq:5672/` |

## Instruções de uso e testes
A API estará disponível em `http://localhost:8000/docs`.

### Testando o Fluxo

1.  **Acesse a UI do RabbitMQ (Opcional):**
    Acesse `http://localhost:15672` (login: `guest` / `guest`). Vá para a aba "Queues" e observe a fila `corrida_finalizada`.

2.  **Consulte o saldo inicial:**
    Os saldos de "Carla" (100) e "Joao" (200) são pré-configurados no Redis.

    `GET http://localhost:8000/saldo/Carla`
    ```json
    { "driver": "Carla", "balance": 100.0 }
    ```

3.  **Cadastre uma nova corrida (POST):**
    Vá para `http://localhost:8000/docs`, encontre `POST /corridas` e use o *Try it out*.

    **Exemplo de body:**
    ```json
    {
        "passenger": {"name": "Monique", "phone": "00000-0000"},
        "driver": {"name": "Carla", "score": 4.8},
        "origin": "Centro",
        "destination": "Inoã",
        "fare": 35.90,
        "payment_method": "Pix"
    }
    ```

    A resposta deve ser um `202 Accepted`:
    ```json
    {
        "message": "Corrida recebida e sendo processada.",
        "ride_id": "..."
    }
    ```

4.  **Observe os Logs:**
    Nos logs do `docker-compose`, você verá o `worker` recebendo, processando e salvando a mensagem.

5.  **Verifique o Saldo Atualizado (Redis):**
    Execute o `GET /saldo/Carla` novamente.

    `GET http://localhost:8000/saldo/Carla`
    ```json
    { "driver": "Carla", "balance": 135.5 }
    ```

6.  **Verifique a Corrida Salva (MongoDB):**
    Liste todas as corridas cadastradas.

    `GET http://localhost:8000/corridas`
    ```json
    [
      {
        "ride_id": "...",
        "passager": { "nome": "Monique", "telefone": "00000-0000" },
        "driver": { "nome": "Carla", "nota": 4.8 },
        "origin": "Centro",
        "destination": "Inoã",
        "fare": 35.50,
        "payment_method": "Pix"
      }
    ]
    ```

### Para acessar

```text
API: http://localhost:8000
RabbitMQ Management: http://localhost:15672 (guest/guest)
MongoDB: localhost:27018
Redis: localhost:6379
```

## Captura de tela do sistema em execução

<img src="docs/terminal.png">
