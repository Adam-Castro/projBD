from banco.conexao import *

class pessoa:
    def __init__(self):
        self.conexao = conexao("localhost","filipe","123456","teste")
        self.conexao.conecta()

    def create(self):
        self.cursor = self.conexao.db.cursor()
        self.sql = """
            CREATE TABLE pessoa_tbl(
            identificador int(4) AUTO_INCREMENT,
            nome varchar(30) NOT NULL,
            telefone_casa varchar(10),
            telefone_cel varchar(10),
            dataNasc date,
            email varchar(30),
            tipoSanguineo varchar(30),
            detalheSaude varchar(200),
            altura float(4,2),
            peso int(3),
            graduacao varchar(15),
            matricula_fkerj varchar(30),
            tipoPessoa int(1),
            identificador_end int(4),
            identificador_dojo int(4),
            FOREIGN KEY (identificador_end) REFERENCES endereco_tbl (identificador),
            FOREIGN KEY (identificador_dojo) REFERENCES dojo_tbl (identificador),
            PRIMARY KEY (identificador))"""
        self.cursor.execute(self.sql)

    def insert(self,nome,telefone_casa,telefone_cel,dataNasc,email,tipoSanguineo,detalheSaude,altura,peso,graduacao,matricula_fkerj,tipoPessoa,identificador_end,identificador_dojo):
        self.cursor = self.conexao.db.cursor()		
        self.sql = """INSERT INTO pessoa_tbl (identificador,nome,telefone_casa,telefone_cel,dataNasc,email,tipoSanguineo,detalheSaude,altura,peso,graduacao,matricula_fkerj,tipoPessoa,identificador_end,identificador_dojo)
            VALUES ('','%s','%s','%s',%s,'%s','%s','%s',%s,%s,'%s','%s',%s,%s,%s)""" % (nome,telefone_casa,telefone_cel,dataNasc,email,tipoSanguineo,detalheSaude,altura,peso,graduacao,matricula_fkerj,tipoPessoa,identificador_end,identificador_dojo)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deu commit na tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela pessoa'

    def update_identificador_dojo(self,identificador_end,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET identificador_dojo = %s where identificador = %s
            """ % (identificador_dojo,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou identificador_dojo tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback identificador_dojo tabela pessoa'
    
    def update_identificador_end(self,identificador_end,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET identificador_end = %s where identificador = %s
            """ % (identificador_end,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou identificador_end tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback identificador_end tabela pessoa'
    
    def update_tipoPessoa(self,tipoPessoa,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET tipoPessoa = %s where identificador = %s
            """ % (tipoPessoa,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou tipo pessoa tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback tipo pessoa tabela pessoa'

    def update_matricula_fkerj(self,matricula_fkerj,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET matricula_fkerj = '%s' where identificador = %s
            """ % (matricula_fkerj,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou matricula fkerj tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback matricula fkerj tabela pessoa'

    def update_nome(self,nome,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET nome = '%s' where identificador = %s
            """ % (nome,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou nome tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback nome tabela pessoa'

    def update_telefone_casa(self,telefone_casa,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET telefone_casa = '%s' where identificador = %s
            """ % (telefone_casa,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou telefone_casa tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback telefone_casa tabela pessoa'

    def update_telefone_cel(self,telefone_cel,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET telefone_cel = '%s' where identificador = %s
            """ % (telefone_cel,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou telefone_cel tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback telefone_cel tabela pessoa'

    def update_dataNasc(self,dataNasc,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET dataNasc = %s where identificador = %s
            """ % (dataNasc,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou dataNasc tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback dataNasc tabela pessoa'

    def update_email(self,email,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET email = '%s' where identificador = %s
            """ % (email,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou email tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback email tabela pessoa'

    def update_altura(self,altura,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET altura = %s where identificador = %s
            """ % (altura,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou altura tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback altura tabela pessoa'

    def update_peso(self,peso,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET peso = %s where identificador = %s
            """ % (peso,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou peso tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback peso tabela pessoa'

    def update_graduacao(self,graduacao,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET graduacao = %s where identificador = %s
            """ % (graduacao,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou graduacao tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback graduacao tabela pessoa'

    def update_tipoSanguineo(self,tipoSanguineo,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """UPDATE pessoa_tbl 
            SET tipoSanguineo = '%s' where identificador = %s
            """ % (tipoSanguineo,identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'atualizou tipoSanguineo tabela pessoa'
        except:
            self.conexao.db.rollback()
            print 'db rollback tipoSanguineo tabela pessoa'

    def close(self):
		self.conexao.close()

    def delete(self,identificador):
        self.cursor = self.conexao.db.cursor()
        self.sql = """DELETE FROM pessoa_tbl
          WHERE identificador = %s""" % (identificador)
        try:
            self.cursor.execute(self.sql)
            self.conexao.db.commit()
            print 'deletou identificador %s na tabela pessoa' % identificador
        except:
            self.conexao.db.rollback()
            print 'db rollback tabela pessoa, nao deletou identificador %s' % identificador
