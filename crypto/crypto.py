import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt_file(file_name):
    """
    Encrypts the given file using AES.
    :param file_name: file to be encrypted
    """
    with open(file_name, 'rb') as f:
        text = f.read()
    encrypted_text = encrypt(text)
    with open(file_name, 'wb') as f:
        f.write(encrypted_text)


def encrypt(text):
    """
    Encrypts the binary text.
    :param text: binary text to be encrypted
    :return: binary string
    """
    key = os.urandom(32)
    store_aes_key(key)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(text))


def pad(text):
    """
    Adds 0's to the end to binary text to complete AES block.
    :param text: binary text to be padded
    :return: binary string
    """
    return text + b"\0" * (AES.block_size - len(text) % AES.block_size)


def store_aes_key(aes_key):
    """
    Stores the encrypted AES key to use for decryption.
    :param aes_key: AES encryption key
    """
    with open('irritating-doggo_public.pem', 'r') as f:
        rsa_key = PKCS1_OAEP.new(RSA.importKey(f.read()))
    with open('aes_key.txt', 'wb') as f:
        f.write(rsa_key.encrypt(aes_key))


def decrypt_file(file_name, key):
    """
    Decrypts the file using a AES key.
    :param file_name: file to be decrypted
    :param key: AES encryption key
    """
    with open(file_name, 'rb') as f:
        cipher_text = f.read()
    decrypted_text = decrypt(cipher_text, key)
    with open(file_name, 'wb') as f:
        f.write(decrypted_text)


def decrypt(cipher_text, key):
    """
    Decrypts the binary text.
    :param cipher_text: binary text to be decrypted
    :param key: AES encryption key
    :return: binary string
    """
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = cipher.decrypt(cipher_text[AES.block_size:])
    return text.rstrip(b"\0")


# encrypt_file('test.txt')

priv_key = open('irritating-doggo_private.pem', "r").read()
rsakey = PKCS1_OAEP.new(RSA.importKey(priv_key))
aes_key = rsakey.decrypt(open('aes_key.txt', 'rb').read())
decrypt_file('test.txt', aes_key)