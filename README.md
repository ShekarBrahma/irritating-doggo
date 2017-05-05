# irritating-doggo
Group Members: Shekar Brahma (brahma2), Wyatt Duiker (duiker2), Shailpik Roy (sroy15)

Background : Our project is a ransomware program that will continuously encrypt files on the victim’s machine, until they provide us with the random (Amazon Gift Card Code).

Requirements:
PyAudio 0.2.11
pycryptodome 3.4.5

Our project has two different programs, one meant to be run on the victim’s machine, and the other on the attacker’s machine. 

To start the ransomware someone will need to run the file called game.py in the Victim directory. This file will open a “game” for the victim to play. They must continuously click a “Prevent Encryption” button, or all the files in the specified directory will be encrypted (in this case, the run_test_dir included with the code). When they give up, we will ask them to email irritatingdoggo@gmail.com a $10 Amazon code along with the generated attachment.txt, in the folder they choose. At this point, you can look inside the run_test_dir to verify the files are encrypted (Victim\run_test_dir\Users\Victim\Pictures has some images). Some directories will not be encrypted (Program Files, Windows , Program Files x86) to avoid an actual machine becoming nonfunctional. After sending this email (with just the attachment.txt file, no gift card is actually required), the attacker side will respond with a file called key.txt. To generate that response you will now run email_client.py in the Attacker directory. This will automatically check all unread emails, parse out the attachments, create the text file containing the decryption keys and reply back to the email where they got the attachment.txt file. Finally the victim has to pass in that text file into the application to unlock their files.You will return to the game, click continue and select the key.txt you received in the email to decrypt your files. 

You can follow these commands/directions to test the above explanation:

cd Victim
python3 game.py
Select “I give up”
Ensure files have been encrypted
Select “Ok”
Choose directory
Send email to irritatingdoggo@gmail.com with attachment.txt
Open a new terminal 
cd Attacker
python3 email_client.py
Download key.txt from response
Return to game.py prompt and select “Continue”
Select “key.txt”
Ensure files are decrypted
