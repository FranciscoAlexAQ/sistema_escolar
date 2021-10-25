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

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS turmas (
                    id INTEGER PRIMARY KEY, 
                    turma VARCHAR NOT NULL
                );
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudantes (
                    id INTEGER PRIMARY KEY, 
                    nome VARCHAR NOT NULL, 
                    idade VARCHAR NOT NULL, 
                    matricula VARCHAR NOT NULL, 
                    cod_turma INTEGER, 
                    FOREIGN KEY (cod_turma) REFERENCES turmas(id)
                );
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS notas (
                    id INTEGER PRIMARY KEY, 
                    nota DECIMAL NOT NULL, 
                    bimestre VARCHAR NOT NULL, 
                    cod_aluno INTEGER, 
                    FOREIGN KEY (cod_aluno)REFERENCES estudantes(id)
                );
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS eventos (
                    id INTEGER PRIMARY KEY, 
                    assunto VARCHAR NOT NULL, 
                    local VARCHAR NOT NULL, 
                    data VARCHAR NOT NULL,
                    hora VARCHAR NOT NULL
                );
            ''')

            self.conn.commit()
        except Exception as e:
            print('erro: ', e)

   
Conn()
