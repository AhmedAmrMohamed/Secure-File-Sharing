#usage: python reckey.py SECRETCODE

from src.Reciver import Reciver
import os

secretCode = ''.join(os.sys.argv[1:])
r = Reciver(secretCode)
r.EstablishKey()
