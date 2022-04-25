from Crypto.PublicKey import RSA
import os

class Channels:
        public = 'public'
        sender = 'sender'
        reciver = 'reciver'

class Manger:
    def __init__(self):
        self.privateFilePath = self.buildFileName(Channels.reciver, 'privateKey')
        self.publicFilePath = self.buildFileName(Channels.public, 'PublicKey')
        self.sessionKey = self.buildFileName(Channels.sender, 'sessionKey')
        self.encryptedSessionKeyPath = self.buildFileName(Channels.public, 'EncryptedSessionKey')
        self.cypherAES = self.buildFileName(Channels.public, 'AESCypher')
        self.reciverACK  = self.buildFileName(Channels.public, 'reciverACK')

    def buildFileName(self, channel, filename):
        return f'{channel}/{filename}.bin'

    def writeBytes(self, filepath, data):
        f=open(filepath, 'wb')
        f.write(data)
        f.close()

    def loadBytes(self, filepath):
        f = open(filepath, 'rb')
        data = f.read()
        f.close()
        return data

    def storeSessionKey(self, sessionKey):
        self.writeBytes(self.sessionKey, sessionKey)
    
    def storeReciverKeys(self, privateKey, publicKey):
        self.writeBytes(self.privateFilePath, privateKey)
        self.writeBytes(self.publicFilePath, publicKey)
    
    def storeEncyptedSessionKey(self, encSessKey):
        self.writeBytes(self.encryptedSessionKeyPath, encSessKey)

    def stoteCypherAES(self, nonce, tag, text):
        file = open(self.cypherAES, 'wb')
        [ file.write(x) for x in (nonce, tag, text)]
        file.close()

    def loadPublicKey(self):
        _bytes = self.loadBytes(self.publicFilePath)
        return RSA.import_key(_bytes)
    
    def loadPrivateKey(self, secretCode):
        _bytes = self.loadBytes(self.privateFilePath)
        return RSA.import_key(_bytes, passphrase = secretCode)
    
    def loadSessionKey(self):
        return self.loadBytes(self.sessionKey)
    
    def loadEncyptedSessionKey(self):
        return self.loadBytes(self.encryptedSessionKeyPath)

    def loadCypherAES(self):
        file = open(self.cypherAES, 'rb')
        (nonce, tag, text) = [ file.read(x) for x in (16, 16, -1)]
        file.close()
        return nonce, tag, text
    
    def checkReciverACK(self):
        return os.path.isfile(self.reciverACK)
    
    def removeReciverACK(self):
        os.remove(self.reciverACK)

    def genReciverACK(self):
        open(self.reciverACK, 'wb').close() #touch file
    




    