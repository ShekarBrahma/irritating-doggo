# Irritating Doggo
Members: Shekar Brahma, Wyatt Duiker, Shailpik Roy

Background : Our project is a ransomware program that will continuously encrypt files on the victim’s machine, until they provide us with the random (Amazon Gift Card Code).

Requirements:
* Python3
* PyAudio 0.2.11
* pycryptodome 3.4.5

Our project has two different programs, one meant to be run on the victim’s machine, and the other on the attacker’s machine. They are currently separated into the Attacker and Victim directories.

To start the ransomware someone will need to run the file called game.py in the Victim directory. This file will open a “game” for the victim to play. They must continuously click a “Prevent Encryption” button, or all the files in the specified directory will be encrypted (in this case, the run_test_dir included with the code). When they give up, we will ask them to email irritatingdoggo@gmail.com a $10 Amazon code along with the generated attachment.txt, in the folder they choose. At this point, you can look inside the Victim/run_test_dir to verify the files are encrypted (Victim/run_test_dir/Users/Victim/Pictures has some images). Some directories will not be encrypted (Program Files, Windows , Program Files x86) to avoid an actual machine becoming nonfunctional. After sending this email (with just the attachment.txt file, no gift card is actually required), the attacker side will respond with a file called key.txt. To generate that response you will now run email_client.py in the Attacker directory. This will automatically check all unread emails, parse out the attachments, create the text file containing the decryption keys and reply back to the email where they got the attachment.txt file. Finally the victim has to pass in that text file into the application to unlock their files.You will return to the game, click continue and select the key.txt you received in the email to decrypt the files in Victim/run_test_dir. In a more practical situation, the code change be changed to target a user's entire filesystem or any specific location. 

You can follow these commands/directions to test the above explanation:
* Make sure python3, PyAudio, and pycryptodome are installed
* cd Victim
* python3 game.py
* Enjoy awesome background music
* Select “I give up”
* Ensure files in Victim/run_test_dir have been encrypted
* Select “Ok”
* Choose directory
* Send email to irritatingdoggo@gmail.com with attachment.txt (located in the choosen directory)
* Open a new terminal 
* cd Attacker
* python3 email_client.py
* Download key.txt from response
* Return to game.py prompt and select “Continue”
* Choose key.txt
* Select "Close"
* Ensure files in Victim/run_test_dir are decrypted

