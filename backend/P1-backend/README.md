## AV1 backend


O principal objetivo é aplicar e demonstrar conceitos de engenharia de software na prática, mostrando como uma entidade pode encapsular não apenas dados, mas também comportamento e regras de negócio, além de comunicar suas mudanças de estado através de Eventos de Domínio.


### Estrutura do Projeto

A estrutura foi organizada para separar as responsabilidades, seguindo as boas práticas de DDD.

.
├── domain/
│   └── category.py       # Contém a Entidade de Domínio Category
├── events/
│   └── category_events.py  # Definição das classes de evento
├── main.py               # Script para demonstrar o ciclo de vida da entidade
└── README.md             # Este arquivo


### Funcionalidades

- Entidade de Domínio: A classe Category centraliza a lógica de negócio (validação, ativação, atualização).

- Construtor Inteligente: Utilização do método __post_init__ para validar dados e gerar valores padrão (como o UUID) no momento da criação.

- Event Sourcing (Padrão Simplificado): Cada alteração de estado na entidade (criação, atualização, etc.) gera um evento imutável que é registrado em uma lista interna.

- Serialização: Métodos to_dict() e from_dict() para converter o estado do objeto para um dicionário (compatível com JSON) e reconstruí-lo.

- Imutabilidade de Eventos: As classes de evento são definidas como dataclasses congeladas (frozen=True), garantindo que os fatos registrados não possam ser alterados.


### Como Executar

* Este projeto não requer dependências externas além de uma instalação padrão do Python 3.

1- Clone o repositório (ou tenha os arquivos na estrutura acima).

2- Execute o script principal a partir da raiz do projeto:

