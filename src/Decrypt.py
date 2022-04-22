from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import Channels

class Decrypt:
    def __init__(self, secretCode):
        self.channelsManger = Channels.Manger()
        privateKey = self.channelsManger.loadPrivateKey(secretCode)
        sessionKey = self.DecryptSessionKey(privateKey)
        self.message = self.DecryptMessage(sessionKey).encode('ascii')
    
    def DecryptSessionKey(self, privateKey):
        enc_sessionKey = self.channelsManger.loadEncyptedSessionKey()
        chyper_rsa =  PKCS1_OAEP.new(privateKey)
        sessionKey = chyper_rsa.decrypt(enc_sessionKey)
        return sessionKey

    def DecryptMessage(self, sessionKey):
        nonce, tag, text = self.channelsManger.loadCypherAES()
        cipher_aes = AES.new(sessionKey, AES.MODE_EAX, nonce)
        message = cipher_aes.decrypt_and_verify(text, tag)
        return(message.decode("utf-8"))