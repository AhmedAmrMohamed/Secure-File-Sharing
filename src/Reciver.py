from PublicKeyEstablishment import PublicKeyEstablishment
from Decrypt import Decrypt
from FileLoader import FileLoader 
import Channels  
import time

class Reciver:
    def __init__(self, secretCode):
        self.secretCode = secretCode.encode('ascii')
        self.channelsManger = Channels.Manger()
        self.EstablishPublicKey()
    
    def writeFile(self, message):
        fl = FileLoader('../reciver/dec.py') ##TODO: you know what...
        fl.writeFile(message)

    def EstablishPublicKey(self):
        PublicKeyEstablishment(False, self.secretCode)
        self.channelsManger.genReciverACK()
    
    def Decrypt(self, secretCode):
        msg = Decrypt(secretCode).message
        self.writeFile(msg)


