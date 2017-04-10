import crawler.crawler as crawl

def find_encrypted(file_list):
    result = []
    for file in file_list:
        if file.is_encrypted:
            result.append(file)
    return result

dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows", "Public", "Applications"]
start_dir = "./run_test_dir"
file_list = crawl.crawl_files(start_dir, dirs_to_skip)

for file in file_list:
    print("encrypting: " + file.path)
    file.encrypt()

print(len(find_encrypted(file_list)))

for file in file_list:
    print("decrypting: " + file.path)
    file.decrypt()

print(len(find_encrypted(file_list)))

