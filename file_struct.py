import crypto.crypto as crypto #crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class File:
    global path
    global is_encrypted
    global encrypted_key #RSA key encrypted with AES
    global decrypted_key

    def __init__(self, path):
        self.path = path
        self.is_encrypted = False
        self.encrypted_key = ""
        self.decrypted_key = None

    def encrypt(self):
        if not self.is_encrypted:
            key_to_store = crypto.encrypt_file(self.path)
            self.is_encrypted = True
            with open('./crypto/aes_key.txt', 'rb') as f:
                self.encrypted_key = f.read()

    def decrypt(self):
        if self.is_encrypted:# and self.decrypted_key is not None
            self.is_encrypted = False
            priv_key = open('./crypto/irritating-doggo_private.pem', "r").read()
            rsakey = PKCS1_OAEP.new(RSA.importKey(priv_key))
            aes_key = rsakey.decrypt(self.encrypted_key) #piku will eventually return this
            crypto.decrypt_file(self.path, aes_key)

    def get_decrypted_key(self):
        # TODO get from piku's stuff
        self.decrypted_key = ""