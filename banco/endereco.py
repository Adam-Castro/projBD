# Last-modified: 18 Jun 2012 23:25:31

from banco.conexao import *

class endereco:
    def __init__(self):
        self.conexao = conexao("localhost","filipe","123456","teste")
        self.conexao.conecta()

    def create(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = """
            CREATE TABLE IF NOT EXISTS endereco_tbl (
              identificador INT(4) NOT NULL AUTO_INCREMENT,
              rua VARCHAR(30) NOT NULL,
              numero INT(4) NULL,
              bairro VARCHAR(30) NULL,
              cidade VARCHAR(30) NULL,
              estado VARCHAR(2) NULL,
              cep VARCHAR(8) NULL,
              PRIMARY KEY(identificador)
            )ENGINE=InnoDB"""
        self.cursor.execute(self.sql)

    def insert(self,rua,numero,bairro,cidade,estado,cep):
        self.cursor = self.conexao.db.cursor()
        self.sql = """INSERT INTO endereco_tbl (identificador,rua,numero,bairro,cidade,estado,cep)
            VALUES ('','%s',%s,'%s','%s','%s','%s')""" % (rua,numero,bairro,cidade,estado,cep)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deu commit na tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela endereco'

    def update_rua(self,rua,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET rua = '%s' where identificador = %s
            """ % (rua,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou rua tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback rua tabela endereco'

    def update_numero(self,numero,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE endereco_tbl
            SET numero = %s where identificador = %s
            """ % (numero,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou numero tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback numero tabela endereco'

    def update_bairro(self,bairro,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET bairro = '%s' where identificador = %s
            """ % (bairro,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou bairro tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback bairro tabela endereco'

    def update_cidade(self,cidade,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET cidade = '%s' where identificador = %s
            """ % (cidade,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou cidade tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback cidade tabela endereco'

    def update_estado(self,estado,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET estado = '%s' where identificador = %s
            """ % (estado,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou estado tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback estado tabela endereco'

    def update_cep(self,cep,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET cep = '%s' where identificador = %s
            """ % (cep,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou cep tabela endereco'
        except:
            self.conexao.db.rollback()
            print 'db rollback cep tabela endereco'

    def close(self):
        self.conexao.close()

    def drop(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = "DROP TABLE IF EXISTS endereco_tbl"
        try:
            self.cursor.execute(self.sql)
        except:
            print "nao deletou tabela endereco_tbl"

    def delete(self,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """DELETE FROM endereco_tbl
          WHERE identificador = %s""" % (identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deletou identificador %s na tabela endereco' % identificador
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela endereco, nao deletou identificador %s' % identificador
