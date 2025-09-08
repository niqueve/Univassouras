### Atividade Avaliativa 1 - P1

*Este script Python permite a realização de operações básicas de CRUD (Create, Read, Update, Delete) em um banco de dados MongoDB. Ele se conecta a uma instância local do MongoDB (mongodb://localhost:27017/).


#### Pré-requisitos

Python 3.x

Biblioteca pymongo

Servidor MongoDB: Uma instância do MongoDB deve estar em execução em localhost na porta padrão 27017.


#### Funcionalidades

O script inclui as seguintes funções principais para interagir com o banco de dados:

create_db(): Cria um novo banco de dados e uma coleção, com a opção de importar dados de um arquivo JSON.

read_db(db_col): Exibe todos os documentos presentes na coleção especificada.

update_db(db_col): Permite modificar o valor de um documento com base em uma chave e um valor.

delete_one_db(db_col): Exclui um único documento da coleção com base em uma chave e um valor.

