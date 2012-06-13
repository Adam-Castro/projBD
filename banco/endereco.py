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
		self.db = MySQLdb.connect(self.newtork,self.user,self.passw,self.bd)
	
	def insert(self,self.rua,self.numero,self.bairro,self.cidade,self.estado,self.cep):
		self.cursor = self.db.cursor()
		self.sql = "INSERT INTO endereco (\
                    rua,numero,bairro,cidade,estado,cep) VALUES (\
                    '%s',%s,'%s','%s','%s',%s)"%\
                    (self.rua,self.numero,self.bairro,self.cidade,self.estado,self.cep)
        try:
             self.cursor.execute(self.sql)
             self.db.commit()       
             print 'deu commit na tabela endereco'     
		except:
			self.db.rollback
            print 'db rollback tabela endereco'
        self.db.close()
	def remove(self):
	def altera(self):

