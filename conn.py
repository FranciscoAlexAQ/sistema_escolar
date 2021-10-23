import sqlite3

# classe para a conexão 
class Conn:
    def __init__(self) -> None:
        self.criarTabelas()

    # criar a conexão
    def criarConn(self):
        try:
            self.conn = sqlite3.connect('banco_de_dados.db')
            print('Conectado ao banco de dados!')

        except Exception as e:
            print(e)

    # criar as tabelas
    def criarTabelas(self):
        try:
            self.criarConn()
            self.cursor = self.conn.cursor()

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS disciplinas (
                    id INTEGER PRIMARY KEY, 
                    nome VARCHAR NOT NULL, 
                    ch INTEGER NOT NULL, 
                    area VARCHAR NOT NULL
                );
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS professores (
                    id INTEGER PRIMARY KEY, 
                    nome VARCHAR NOT NULL, 
                    cpf INTEGER NOT NULL, 
                    idade INTEGER NOT NULL, 
                    cod_disc INTEGER NOT NULL, 

                    FOREIGN KEY(cod_disc) REFERENCES disciplinas(id)
                );
            ''')

            self.conn.commit()
        except Exception as e:
            print('erro: ', e)

   
Conn()
