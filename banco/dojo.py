from banco.conexao import *

class dojo:
    def __init__(self):
        self.conexao = conexao("localhost","filipe","123456","teste")
        self.conexao.conecta()

    def create(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = """
			CREATE TABLE dojo_tbl (
			  identificador INT(4) NOT NULL AUTO_INCREMENT,
			  identificador_end INT(4) NOT NULL,
			  nome VARCHAR(30) NOT NULL,
			  telefone VARCHAR(10) NULL,
			  PRIMARY KEY(identificador, identificador_end),
			  FOREIGN KEY(identificador_end)
				REFERENCES endereco_tbl(identificador)
				  ON DELETE RESTRICT
				  ON UPDATE CASCADE
			)
			ENGINE=InnoDB"""
        self.cursor.execute(self.sql)

    def drop(self):
		self.cursor = self.conexao.db.cursor()
		self.sql = "DROP TABLE dojo_tbl"
		self.cursor.execute(self.sql)

    def insert(self,identificador_end,nome,telefone):
        self.cursor = self.conexao.db.cursor()		
        self.sql = """INSERT INTO dojo_tbl (identificador,identificador_end,nome,telefone)
            VALUES ('',%s,'%s','%s')""" % (identificador_end,nome,telefone)
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
            SET nome = '%s' where identificador = %s
            """ % (nome,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou nome tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback nome tabela dojo'

    def update_telefone(self,telefone,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE dojo_tbl 
            SET telefone = '%s' where identificador = %s
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
            SET identificador_end = %s where identificador = %s
            """ % (identificador_end,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou endereco tabela dojo'
        except:
            self.conexao.db.rollback()
            print 'db rollback endereco tabela dojo'

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
