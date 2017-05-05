# irritating-doggo

crawler:
* Our crawler takes a directory to start in and a list of directories to ignore. We will ignore certain directories in order to keep the operating system and program files operable (Program Files, Applications, etc). This list will be sent to our encrypter (in crypto) and will encrypt a file each time the user fails in our game.

crypto:
* Encryption on a file is done in two parts. First, a AES key is generated for the file, and then the file is encrypted with that key. Second, the AES key will be encrypted with a public RSA key (irritating-doggo_public.pem), which was created with a private key beforehand, and then the encrypted key is stored into the data structure in file_struct.py. 

file_struct:
* Defines a File object that stores data on the files our ransomware is targeting, specifically the encryption and decryption keys. The decryption key data is kept null until the key.txt file is provided by the user.
