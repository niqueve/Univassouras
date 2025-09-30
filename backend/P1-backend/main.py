import json
from domain.category import Category

def print_separator(title: str):
    print(f"\n{'- '*20} {title} {'- '*20}")

#-------------------------------------------------------Criação da Categoria e Evento Inicial
print_separator("Criação da Categoria")
categoria = Category(name="   Aventura   ", description="Filme de Aventura")
print(f"Categoria criada: {categoria}")
print(f"Representação: {repr(categoria)}")
print("Evento de criação registrado:")
print(f"-> {categoria.events[0]}")

#---------------------------------------------------------------- Demonstração da Serialização
print_separator("Serialização e Reconstrução")

# Serializando para um dicionário
categoria_dicionario = categoria.to_dict()
print("\nObjeto serializado para dicionário:")
print(json.dumps(categoria_dicionario, indent=2))

# Reconstruindo a partir do dicionário
categoria_reconstrucao = Category.from_dict(categoria_dicionario)
print(f"\nObjeto reconstruído: {categoria_reconstrucao}")
print(f"O objeto reconstruído tem seu próprio evento de criação: {categoria_reconstrucao.events[0]}")

# Verificando se os objetos são equivalentes em estado
sao_equivalentes = categoria.id == categoria_reconstrucao.id and \
                 categoria.name == categoria_reconstrucao.name
print(f"\nOs estados dos objetos original e reconstruído são equivalentes? {sao_equivalentes}")


#-----------------------------------------------------------------Ciclo de Vida e Eventos de Domínio
print_separator("Ciclo de Vida e Registro de Eventos")

# Atualizando a categoria
print("\nAtualizando a categoria...")
categoria.update(description="Filmes de ação")

# Desativando a categoria
print("Desativando a categoria...")
categoria.deactivate()
print(f"Estado atual: {categoria}")

# Ativando a categoria novamente
print("Ativando a categoria...")
categoria.activate()
print(f"Estado final: {categoria}")

# --- 4. Lista Final de Eventos ---
print_separator("4. Lista Final de Eventos de Domínio")
print("Histórico de eventos para a categoria original:")
for i, event in enumerate(categoria.events):
    print(f"{i+1}. {event}")