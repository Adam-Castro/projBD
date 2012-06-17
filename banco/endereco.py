try:
    import MySQLdb
except:
    print("MySQLdb Not Available")

class endereco:
    def __init__(self):
        self.newtork = "localhost"
        self.user = "filipe"
        self.passw = "123456"
        self.bd = "teste"
        self.conecta()

    def create(self):
        self.cursor = self.db.cursor()
        self.sql = """
            CREATE TABLE endereco_tbl(
            identificador int(4) AUTO_INCREMENT,
            rua varchar(30) NOT NULL,
            numero int(4),
            bairro varchar(30) NOT NULL,
            cidade varchar(30) NOT NULL,
            estado varchar(2) NOT NULL,
            cep varchar(8),
            PRIMARY KEY (identificador))"""
        self.cursor.execute(self.sql)

    def insert(self,rua,numero,bairro,cidade,estado,cep):
        self.cursor = self.db.cursor()		
        self.sql = """INSERT INTO endereco_tbl (identificador,rua,numero,bairro,cidade,estado,cep) 
            VALUES ('','%s',%s,'%s','%s','%s','%s')""" % (rua,numero,bairro,cidade,estado,cep)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'deu commit na tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback tabela endereco'

    def altera_rua(self,rua,identificador):
        self.cursor = self.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET rua = '%s'where identificador = %s
            """ % (rua,identificador)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'atualizou rua tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback rua tabela endereco'

    def altera_numero(self,numero,identificador):
        self.cursor = self.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET numero = '%s'where identificador = %s
            """ % (numero,identificador)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'atualizou numero tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback numero tabela endereco'

    def altera_bairro(self,bairro,identificador):
        self.cursor = self.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET bairro = '%s'where identificador = %s
            """ % (bairro,identificador)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'atualizou bairro tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback bairro tabela endereco'

    def altera_cidade(self,cidade,identificador):
        self.cursor = self.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET cidade = '%s'where identificador = %s
            """ % (cidade,identificador)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'atualizou cidade tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback cidade tabela endereco'

    def altera_estado(self,estado,identificador):
        self.cursor = self.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET estado = '%s'where identificador = %s
            """ % (estado,identificador)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'atualizou estado tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback estado tabela endereco'

    def altera_cep(self,cep,identificador):
        self.cursor = self.db.cursor()
        self.sql = """UPDATE endereco_tbl 
            SET cep = '%s'where identificador = %s
            """ % (cep,identificador)
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
            print 'atualizou cep tabela endereco'
        except:
            self.db.rollback()
            print 'db rollback cep tabela endereco'

    def conecta(self):
        self.db = MySQLdb.connect(self.newtork,self.user,self.passw,self.bd)

    def close(self):
        self.db.close()
