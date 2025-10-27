import os

# RabbitMQ settings
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "user")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "password")
RABBITMQ_QUEUE = "mensagens"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8005