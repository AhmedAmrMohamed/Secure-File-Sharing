#usage: python recdec.py SECRETCODE 

from src.Reciver import Reciver
import os

secrectCode = ''.join(os.sys.argv[1])

r = Reciver(secrectCode)
r.Decrypt()