import crypto.crypto as crypto  # crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class File:
    allFiles = []

    def __init__(self, path):
        self.path = path
        self.is_encrypted = False
        self.encrypted_key = ""
        self.decrypted_key = None
        File.allFiles.append(self)

    def encrypt(self):
        if not self.is_encrypted:
            crypto.encrypt_file(self.path)
            self.is_encrypted = True
            with open('./crypto/aes_key.txt', 'rb') as f:
                self.encrypted_key = f.read()

    def decrypt(self):
        self.is_encrypted = False
        crypto.decrypt_file(self.path, self.decrypted_key)

    def update_decrypted_key(self, new_key):
        self.decrypted_key = new_key
