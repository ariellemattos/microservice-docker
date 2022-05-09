import sys
from time import sleep
import sqlalchemy
import pymysql
from pandas import DataFrame


def connect():
    dbConnect = "mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}".format(
        host="db",
        dbname="loja",
        user="aluno",
        password="123456",
        port="3306",
    )

    engine = sqlalchemy.create_engine(dbConnect, connect_args={'connect_timeout': 100000})
    timeout = 5
    while True:
        print("tentando")
        try:
            conn = engine.connect()
            print("tentou e conseguiu")
            break
        except:
            print('DB not started, trying again at {} seconds'.format(timeout))

        sleep(timeout)
    
    return conn


def consulta():
    conn = connect()

    result = conn.execute("select * from Produto")

    return DataFrame(result.mappings().all(), columns=[
        'nome',
        'categoria',
        'preco']
    )


def gravar(nome, categoria, preco):
    sql = """ INSERT INTO Produto (nome, categoria, preco) VALUES (%s,%s,%s)"""

    conn = connect()

    insert = (nome, categoria, preco)

    conn.execute(sql, insert)

    conn.close()

    return "OK"


def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS Produto (
        nome varchar(200), 
        categoria varchar(200), 
        preco numeric(18,2)
    );
    """

    conn = connect()

    conn.execute(sql)

    conn.close()


try:
    create_table()
except Exception as err:
    print(err)
