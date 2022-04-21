from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import Channels

class Encrypt():
    def __init__(self, message):
        self.channelsManger = Channels.Manger()
        publicKey, sessionKey = self.loadKeys()
        self.Encrypt(publicKey, sessionKey, message)
        
    def loadKeys(self):
        publicKey = self.channelsManger.loadPublicKey()
        sessionKey = self.channelsManger.loadSessionKey()
        return publicKey, sessionKey

    def Encrypt(self, publicKey, sessionKey, message):
        self.EncryptSessionKey(publicKey, sessionKey)
        self.EncryptMessage(sessionKey, message)

    def EncryptSessionKey(self, publicKey, sessionKey):
        cipher_rsa = PKCS1_OAEP.new(publicKey)
        enc_session_key = cipher_rsa.encrypt(sessionKey)
        self.channelsManger.storeEncyptedSessionKey(enc_session_key)
    
    def EncryptMessage(self, sessionKey, message):
        cipher_aes = AES.new(sessionKey, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(message)
        self.channelsManger.stoteCypherAES(cipher_aes.nonce, tag, ciphertext)