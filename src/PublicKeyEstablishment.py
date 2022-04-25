from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import src.Channels

class PublicKeyEstablishment:
    # pke ( true) : sneder
    # pke (fals, string): reciver
    def __init__(self, sender = True, secretCode = None):
        self.channelsManger = src.Channels.Manger()
        if sender:
            self.GenSenderSessionKey()
        else:
            self.GenReciverkeys(secretCode)
    
    def GenSenderSessionKey(self):
        session_key = get_random_bytes(16)
        self.channelsManger.storeSessionKey(session_key)

    def GenReciverkeys(self, secretCode):
        key = RSA.generate(2048)
        privateKey = key.export_key(passphrase=secretCode, pkcs=8,
            protection="scryptAndAES128-CBC")
        publicKey = key.publickey().export_key()
        self.channelsManger.storeReciverKeys(privateKey, publicKey)
        




## tests
# x = PublicKeyEstablishment()
# x.genSenderSessionKey()
# x.genReciverkeys('ahmed amr')
# x.Encrypt('something in the way'.encode('utf-8'))
# y = x.Decrypt('ahmed amr')

