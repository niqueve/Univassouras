from pymongo import MongoClient
import json


client = MongoClient("mongodb://localhost:27017/")

#--------------------------------------------------------------------------create
def create_db ():
    global client 
    db_name = input("Digite o nome do banco: ")
    db_table = input ("digite o nome da tabela: ")
    db = client[db_name]
    db_col = db[db_table]
    answer = input("Deseja  inserir os dados agora? (SIM/NAO) ").upper()
    if answer == "SIM":
        data_name = input("Insira o nome do arquivo (ex. dados.json): ")
        try:
            with open(data_name, "r") as file:
                data = json.load(file)
                db_col.insert_many(data)
        except Exception as exc:
            print(f"Não foi possível acessar o arquivo:\n {exc}")
    return db, db_col

#---------------------------------------------------------------------------read
def read_db (db_col):
    for dado in db_col.find():
        print(dado)

#-----------------------------------------------------------------------update
def update_db (db_col):
    key_data = input("Qual dado deseja modificar? (ex: nome joao) ")
    if len(key_data) != 2:
        print("Formato invalido, digite exatamente 2  valores separados por espaço")
    else:
        k,d = key_data.split()
        query = {k : d}
        answer = input("Qual valor deseja atribuir: ")
        new_values = {"$set": {k : answer}}
        db_col.update_one(query, new_values)
        print("Dados atualizados")

#-----------------------------------------------------------------------------------delete
def delete_one_db (db_col):
    key_data = input("digite o dado que deseja deletar (ex: nome joao): ")
    if len(key_data) != 2:
        print("Formato inválido, digite extamente 2 valores separados por espaço")
    else:
        k,d = key_data.split()
        query = {k : d}
        db_col.delete_one(query)
        print("Dado deletado")

#----------------------------------------------------------------------------test

db, db_col = create_db()

insert_this = {
  "nome": "Jonas",
  "idade": 31,
  "cidade": "São Paulo",
  "habilidades": ["Java", "JavaScript", "SQL"]
}

db_col.insert_one(insert_this)


read_db(db_col)
