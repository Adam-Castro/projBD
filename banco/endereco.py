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

#def remove(self):
#def altera(self):
    def conecta(self):
        self.db = MySQLdb.connect(self.newtork,self.user,self.passw,self.bd)

    def close(self):
        self.db.close()
