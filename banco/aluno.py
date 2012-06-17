from banco.conexao import *

class aluno:
    def __init__(self):
        self.conexao = conexao("localhost","filipe","123456","teste")
        self.conexao.conecta()

    def create(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = """
            CREATE TABLE aluno_tbl(
            identificador int(4) NOT NULL,
            dataInscricao date,
            dataUltimoAtestado date,
            FOREIGN KEY (identificador) REFERENCES pessoa_tbl (identificador))"""
        self.cursor.execute(self.sql)

    def insert(self,identificador,dataInscricao,dataUltimoAtestado):
        self.cursor = self.conexao.db.cursor()		
        self.sql = """INSERT INTO aluno_tbl (identificador,dataInscricao,dataUltimoAtestado)
            VALUES (%s,%s,%s)""" % (identificador,dataInscricao,dataUltimoAtestado)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deu commit na tabela aluno'
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela aluno'

    def update_identificador(self,identificador_novo,identificador_antigo):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE aluno_tbl 
            SET identificador = %s where identificador = %s
            """ % (identificador_novo,identificador_antigo)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou identificador_novo tabela aluno'
        except:
            self.conexao.db.rollback()
            print 'db rollback identificador_novo tabela aluno'
    
    def update_dataInscricao(self,dataInscricao,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE aluno_tbl 
            SET dataInscricao = %s where identificador = %s
            """ % (dataInscricao,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou dataInscricao tabela aluno'
        except:
            self.conexao.db.rollback()
            print 'db rollback dataInscricao tabela aluno'
    
    def update_dataUltimoAtestado(self,dataUltimoAtestado,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE aluno_tbl 
            SET dataUltimoAtestado = %s where identificador = %s
            """ % (dataUltimoAtestado,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou tipo dataUltimoAtestado tabela aluno'
        except:
            self.conexao.db.rollback()
            print 'db rollback tipo dataUltimoAtestado tabela aluno'

    def close(self):
		self.conexao.close()

    def delete(self,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """DELETE FROM aluno_tbl
          WHERE identificador = %s""" % (identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deletou identificador %s na tabela aluno' % identificador
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela aluno, nao deletou identificador %s' % identificador
