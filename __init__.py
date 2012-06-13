import sys
import os

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
except:
    print("GTK Not Availible")
    sys.exit(1)

class TesteGui:
	
	
