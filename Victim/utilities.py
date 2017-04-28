import os

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

def decrypt(file_path, file_list):
    keys = get_aes_keys(file_path)

    for i in range(len(file_list)):
        _file = file_list[i]
        _file.update_decrypted_key(keys[i])
        _file.decrypt()
