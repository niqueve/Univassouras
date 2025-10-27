import os
import time
import sys
import json
import pika

RABBIT_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
QUEUE_NAME = "mensagens"


def callback(ch, method, properties, body):
    try:
        msg = json.loads(body.decode())
    except Exception:
        msg = body.decode()
    print("Recebido:", msg, flush=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    while True:
        try:
            params = pika.ConnectionParameters(host=RABBIT_HOST)
            connection = pika.BlockingConnection(params)
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE_NAME, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
            print("[*] Aguardando mensagens. Ctrl+C para sair", flush=True)
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ não disponível, tentando novamente em 5s...", flush=True)
            time.sleep(5)
        except KeyboardInterrupt:
            print("Interrompido", flush=True)
            try:
                connection.close()
            except Exception:
                pass
            sys.exit(0)


if __name__ == '__main__':
    main()
