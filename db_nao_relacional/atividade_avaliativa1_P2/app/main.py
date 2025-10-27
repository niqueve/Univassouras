from fastapi import FastAPI
from app.api.routes import messages

# Create FastAPI app
app = FastAPI(
    title="Message API",
    description="API para envio de mensagens via RabbitMQ",
    version="1.0.0"
)

# Include routers
app.include_router(messages.router, tags=["messages"])
