class File:
    global path
    global is_encrypted
    global key

    def __init__(self, path):
        self.path = path
        self.is_encrypted = False
        self.key = ""

    def encrypt(self):
        if not self.is_encrypted:
            # call shekar's encrypt
            self.is_encrypted = True
            self.key = "TODO shekar sets this"