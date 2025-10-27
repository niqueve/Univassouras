#### Atividade 1 - P2

Configurar um ambiente com Docker Compose contendo:

- FastAPI (aplicação principal)

- Kafka ou RabbitMQ (sistema de mensageria)

Criar um endpoint REST /enviar que:

- Receba um JSON com uma mensagem (ex: nome e texto)

- Envie essa mensagem para um tópico (Kafka) ou fila (RabbitMQ)

Criar um consumidor que:

- Leia as mensagens do tópico/fila

- Exiba no terminal (print) o conteúdo recebido