from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import Channels

class PublicKeyEstablishment:
    def __init__(self):
        self.channelsManger = Channels.Manger()
    
    def genSenderSessionKey(self):
        session_key = get_random_bytes(16)
        self.channelsManger.storeSessionKey(session_key)

    def genReciverkeys(self, secretCode):
        key = RSA.generate(2048)
        privateKey = key.export_key(passphrase=secretCode, pkcs=8,
            protection="scryptAndAES128-CBC")
        publicKey = key.publickey().export_key()
        self.channelsManger.storeReciverKeys(privateKey, publicKey)

    def Encrypt(self, message):
        publicKey = self.channelsManger.loadPublicKey()
        sessionKey = self.channelsManger.loadSessionKey()
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

    def Decrypt(self, secretCode):
        privateKey = self.channelsManger.loadPrivateKey(secretCode)
        sessionKey = self.DecryptSessionKey(privateKey)
        return self.DecryptMessage(sessionKey)
    
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




## tests
# x = PublicKeyEstablishment()
# x.genSenderSessionKey()
# x.genReciverkeys('ahmed amr')
# x.Encrypt('something in the way'.encode('utf-8'))
# y = x.Decrypt('ahmed amr')

