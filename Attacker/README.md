decrypt_rsa:
* To decrypt a file, the encrypted AES key for that file is given to a decryption function. The function then gets the actual AES key by decrypting it with the private RSA key (irritating-doggo_private.pem). Then the actual AES key is used to decrypt the file.

email_client.py:
* This python script will look through the irritatingdoggo@gmail.com account and find any new emails from victims and run the decryption_rsa script on the attachment.txt file they provide. It will also generate and send the key.txt file the victim will need to decrpt their filesystem. 
