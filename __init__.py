# Last-modified: 18 Jun 2012 23:26:23

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
from banco.dojo import *
from banco.aluno import *
from banco.pessoa import *
from banco.professor import *

class principal:
    def __init__(self):
        self.endereco = endereco()
        self.endereco.drop()
        #self.end.create()
        #self.pessoa = pessoa()
        #self.pessoa.create()
        #self.pessoa.close()
        #self.professor = professor()
        #self.professor.create()
        #self.professor.close()
        #self.aluno = aluno()
        #self.aluno.create()
        #self.aluno.close()
        #self.dojo = dojo()
        #self.dojo.create()
        #self.dojo.close()
        #self.end.insert('bronze','227','ouro verde','rio das ostras','rj','28890000')
        #self.end.update_rua('virgem',4)
        #self.end.delete(3)

if __name__ == '__main__':
    principal()
