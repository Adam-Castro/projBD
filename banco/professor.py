from banco.conexao import *

class aluno:
    def __init__(self):
        self.conexao = conexao("localhost","filipe","123456","teste")
        self.conexao.conecta()

    def create(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = """
            CREATE TABLE professor_tbl(
            identificador int(4) NOT NULL,
            identificador_dojo int(4) NOT NULL
            FOREIGN KEY (identificador) REFERENCES pessoa_tbl (identificador),
            FOREIGN KEY (identificador_dojo) REFERENCES dojo_tbl (identificador))"""
        self.cursor.execute(self.sql)

    def insert(self,identificador,identificador_dojo):
        self.cursor = self.conexao.db.cursor()		
        self.sql = """INSERT INTO professor_tbl (identificador,identificador_dojo)
            VALUES (%s,%s)""" % (identificador,identificador_dojo)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deu commit na tabela professor'
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela professor'

    def update_identificador(self,identificador_novo,identificador_antigo):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE professor_tbl 
            SET identificador = %s where identificador = %s
            """ % (identificador_novo,identificador_antigo)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou identificador_novo tabela professor'
        except:
            self.conexao.db.rollback()
            print 'db rollback identificador_novo tabela professor'
    
    def update_identificador_dojo(self,identificador,identificador_dojo):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE professor_tbl 
            SET identificador_dojo = %s where identificador = %s
            """ % (identificador_dojo,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou identificador dojo tabela professor'
        except:
            self.conexao.db.rollback()
            print 'db rollback identificador_dojo tabela professor'

    def close(self):
		self.conexao.close()

    def delete(self,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """DELETE FROM professor_tbl
          WHERE identificador = %s""" % (identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deletou identificador %s na tabela professor' % identificador
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela professor, nao deletou identificador %s' % identificador
