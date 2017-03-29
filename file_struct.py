class File:
    global path
    global is_encrypted
    global encrypted_key

    def __init__(self, path):
        self.path = path
        self.is_encrypted = False
        self.encrypted_key = ""

    def encrypt(self):
        if not self.is_encrypted:
            # call shekar's encrypt
            self.is_encrypted = True
            self.encrypted_key = "TODO shekar sets this"