from pydantic import BaseModel


class Message(BaseModel):
    nome: str
    texto: str
