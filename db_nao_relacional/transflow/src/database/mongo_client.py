from pymongo import MongoClient
from .settings import settings

class MongoDB:
    def __init__(self):
        try:
            self.client = MongoClient(settings.MONGO_URL)
            self.db = self.client["transflow"]
            self.collection = self.db["rides"]
            print("MongoDB connected successfully!")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            self.client = None
            self.db = None
            self.collection = None

    def get_collection(self):
        return self.collection
    
    def close_connection(self):
        if self.client:
            self.client.close()

mongo_db = MongoDB()

#---------------------------------------dependência FastAPI
def get_mongo_collection():
    return mongo_db.get_collection()