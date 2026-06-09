import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        #se já existe um banco de dados ele conecta, se não existe ele cria
        self.connection = sqlite3.connect(db_name)

                                #cria a tabela se ela não existir
        self.connection.execute('''
                                CREATE TABLE IF NOT EXISTS dados(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    score INTEGER NOT NULL,
                                    date TEXT NOT NULL)
                                ''')



    #SALVAR NO BANCO DE DADOS
    def save(self, score_dict: dict):
        #insere os dados no banco
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        #executa o comando no BD
        self.connection.commit()


    #TOP 10 score
    #                       retorna uma lista 
    def score_top10(self) -> list :
        #retorno dos 10 maiores score da tabela
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        #encerra a conexao com o banco de dados
        return self.connection.close()
