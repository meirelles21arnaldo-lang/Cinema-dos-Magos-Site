# ORM, tratar uma tabela como se fosse um objeto
import sqlite3 as sql
import app
#def é como se fosse o public static, pra inciar um método
#def conect_db(url):
#    conn = sql.connect(url)
#    return conn
# esse código é reduntante, o método ele serve mais para tratar as coisas agora

#-> pra falar que sempre vai retornar um objeto do tipo sql.Connection
def conect_db_cinema() -> sql.Connection:
    conn = sql.connect("cinema.db")
    return conn

#O conn: sql.Connection eu estou tipando o conn
def create_table_filmes(conn: sql.Connection):
    cursor = conn.cursor()
    cursor = cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero TEXT NOT NULL,
        classificacaoEtaria INTEGER NOT NULL,
        duracao INTEGER NOT NULL,
        capa BLOB
        )
    """)
    conn.commit()
    conn.close()
#Abre a conexão, faz o cursor, comita e fecha

#tem que tratar os erros nulo, numero ao inves de string
def cadastrar_filme(nome, genero, classificacaoEtaria, duracao, capa):

    conn = sql.connect("cinema.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO filmes (nome, genero, classificacaoEtaria, duracao, capa) VALUES (?, ?, ?, ?, ?)
    """,(nome, genero, classificacaoEtaria, duracao, capa))

    conn.commit()
    conn.close()

conn = conect_db_cinema()
create_table_filmes(conn)
