import os

# RabbitMQ settings
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER") or os.getenv("RABBITMQ_DEFAULT_USER") or "user"
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS") or os.getenv("RABBITMQ_DEFAULT_PASS") or "password"
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/")
RABBITMQ_QUEUE = "mensagens"

# Connection settings
RABBITMQ_CONNECTION_ATTEMPTS = 10
RABBITMQ_RETRY_DELAY = 5

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8005