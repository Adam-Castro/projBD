import sys
import os

#try:
#    import pygtk
#    pygtk.require("2.0")
#except:
#    pass
#try:
#    import gtk
#except:
#    print("GTK Not Availible")
#    sys.exit(1)

from banco.endereco import *

class principal:
	
	def __init__(self):
		self.end = endereco()
		#self.end.create()
		#self.end.insert('bronze','227','ouro verde','rio das ostras','rj','28890000')
		#self.end.altera_rua('virgem','1')
		self.end.altera_cep('45678921',2)
		self.end.close()

if __name__ == '__main__':
	principal()
	
