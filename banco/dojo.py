from banco.conexao import *

class dojo:
    def __init__(self):
        self.conexao = conexao("localhost","filipe","123456","teste")
        self.conexao.conecta()

    def create(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = """
            CREATE TABLE dojo_tbl(
            identificador int(4) NOT NULL AUTO_INCREMENT,            
            nome varchar(30) NOT NULL,
            telefone varchar(10),
            identificador_end int(4) NOT NULL,
            identificador_prof int(4) NOT NULL,
            FOREIGN KEY(identificador_end) REFERENCES endereco_tbl (identificador),
            FOREIGN KEY(identificador_prof) REFERENCES professor_tbl (identificador),
            PRIMARY KEY (identificador))"""
        self.cursor.execute(self.sql)

    def insert(self,nome,telefone,identificador_end,identificador_prof):
        self.cursor = self.conexao.db.cursor()		
        self.sql = """INSERT INTO dojo_tbl (identificador,nome,telefone,identificador_end,identificador_prof)
            VALUES ('','%s',%s,%s,%s)""" % (nome,telefone,identificador_end,identificador_prof)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deu commit na tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela dojo'

    def update_nome(self,nome,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE dojo_tbl 
            SET nome = '%s'where identificador = %s
            """ % (nome,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou nome tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback nome tabela dojo'

    def update_numero(self,telefone,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE dojo_tbl 
            SET telefone = '%s'where identificador = %s
            """ % (telefone,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou telefone tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback telefone tabela dojo'

    def update_identificador_end(self,identificador_end,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE dojo_tbl 
            SET identificador_end = '%s'where identificador = %s
            """ % (identificador_end,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou endereco tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback endereco tabela dojo'

    def update_identificador_prof(self,identificador_prof,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE dojo_tbl 
            SET identificador_prof = '%s'where identificador = %s
            """ % (identificador_prof,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou professor tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback professor tabela dojo'

    def close(self):
		self.conexao.close()

    def delete(self,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """DELETE FROM dojo_tbl
          WHERE identificador = %s""" % (identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deletou identificador %s na tabela dojo' % identificador
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela dojo, nao deletou identificador %s' % identificador
