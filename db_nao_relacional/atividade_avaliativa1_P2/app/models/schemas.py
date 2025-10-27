from pydantic import BaseModel

class Message(BaseModel):
    """
    Schema for message data
    
    Attributes:
        nome (str): Nome do remetente
        texto (str): Conteúdo da mensagem
    """
    nome: str
    texto: str