try:
    import MySQLdb
except:
    print("MySQLdb Not Available")

class conexao:

	def __init__(self,network,user,passw,bd):
		self.newtork = network
		self.user = user
		self.passw = passw
		self.bd = bd

	def conecta(self):
		self.db = MySQLdb.connect(self.newtork,self.user,self.passw,self.bd)

	def close(self):
		self.db.close()
