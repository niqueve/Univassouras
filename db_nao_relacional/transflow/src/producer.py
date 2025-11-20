from faststream.rabbit import RabbitBroker
from src.database.settings import settings

broker = RabbitBroker(settings.RABBITMQ_URL)

async def publish_ride(ride):
    """Publica um evento de corrida no broker."""
    await broker.publish(
        ride.model_dump_json(),
        queue="ride_completed",
        exchange="rides"
    )