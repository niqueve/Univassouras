from faststream import FastStream
from faststream.rabbit import RabbitBroker
import json

from src.database.settings import settings
from src.database.mongo_client import get_mongo_collection
from src.database.redis_client import get_redis_client
from src.models.ride_model import Ride

#---------------------------configurar o broker
broker = RabbitBroker(settings.RABBITMQ_URL)
app = FastStream(broker)

#-----------------------------------pegar clientes
redis_client = get_redis_client()
mongo_collection = get_mongo_collection()

@broker.subscriber(queue="fineshed_ride", exchange="rides")
async def handle_ride(message: str):
    """
    1- Recebe a mensagem (String JSON)
    2- Valida os dados com o modelo Pydanc
    3- Atualiza o saldo no Redis 
    4- Salva a corrida no MongoDB
    """
    try:
        ride_data = json.loads(message)
        ride = Ride(**ride_data)
        print(f"Consumidor: Recebida corrida {ride.ride_id}")

        balance_key = f"saldo: {ride.driver.name}"
        new_balance = redis_client.incrbyfloat(balance_key, ride.fare)
        print(f"Consumidor: Saldo de {ride.driver.name} atualizado para {new_balance}")

        #--------------registrar no MongoDB
        ride_dict = ride.model_dump()
        ride_dict["ride_id"] = str(ride.ride_id)
        mongo_collection.insert_one(ride_dict)
        print(f"Consumidor: Corrida {ride.ride_id} salva no MongoDB.")

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")