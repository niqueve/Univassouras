### Repositório atividades backend e banco de dados não relacional

#### ---------------------------------- Atividade avaliativa 1

#### --------------------------------- Atividade avaliativa 2

*Atividade – Refatoração de Código FastAPI + MongoDB + WebSockets

Contexto:

Você recebeu um sistema de chat em tempo real desenvolvido com FastAPI, MongoDB Atlas e WebSockets. O código atual funciona, mas possui alguns pontos que podem ser melhorados para seguir boas práticas de organização, manutenção e escalabilidade.

Seu objetivo será refatorar esse código e entregar uma versão organizada, modularizada e mais clara.

🎯 Objetivos da Atividade

Aplicar boas práticas de organização de código em projetos Python.
Refatorar para deixar o projeto mais modular e legível.
Usar padrões de projeto simples (ex: separação de camadas).
Melhorar a manutenibilidade do código.
🔧 Tarefas a serem realizadas

Organização em módulos
Criar pastas/arquivos para separar responsabilidades, por exemplo:
database.py → Conexão com MongoDB e funções auxiliares.
models.py → Funções de serialização e schemas.
ws_manager.py → Classe WSManager.
routes/ → Rotas REST (messages.py).
main.py → Apenas inicialização do FastAPI e montagem das rotas.

Uso de Pydantic
Criar modelos MessageIn (entrada) e MessageOut (saída) com validação.
Substituir Body(..., embed=True) por esses modelos.
Melhorar tratamento de erros
Quando before_id não for válido, retornar um erro 400 em vez de simplesmente ignorar.
Garantir que mensagens sem conteúdo não sejam salvas no banco.
Configurações externas

Criar um arquivo config.py que centralize variáveis como MONGO_URL e MONGO_DB.
Documentação mínima
Adicionar docstrings explicando os principais métodos (ex: broadcast, serialize, db).
Escrever no README.md como rodar o projeto.
✅ Critérios de Entrega

O código deve rodar corretamente após refatorado.
A estrutura deve estar modularizada (mínimo 3 arquivos além do main.py).
Deve existir pelo menos 1 modelo Pydantic para entrada e saída de mensagens.
O tratamento de erros deve estar mais explícito.
