import redis 
from .settings import settings

class RedisDB:
    def __init__(self):
        try:
            self.client = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=0,
                decode_responses=True
            )
            self.client.ping()
            print("Redis connected successfuly!")
        except Exception as e:
            print(f"Error connecting to Redis: {e}")
            self.client = None

    def get_client(self):
        return self.client
    
    def set_default_balances(self):

        #-------------------configurar saldos iniciais para teste
        if self.client:
            if not self.client.exists("balance:Carla"):
                self.client.set("balance:Carla", 100)
            if not self.client.exists("balance:Monique"):
                self.client.set("balance:Monique", 200)

redis_db = RedisDB()
redis_db.set_default_balances()

#---------------------------------------dependÊncia
def get_redis_client():
    return redis_db.get_client()