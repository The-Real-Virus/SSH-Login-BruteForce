# SSH Login Brute Force Tool

## Description
This is a simple Python-based SSH brute force script that attempts to log into a target host using a list of  
common passwords (e.g., from the `rockyou.txt` wordlist). The script uses `paramiko` for SSH connections.

## Features
- Brute-forces SSH login using a password list.
- Uses the `paramiko` library to connect to the SSH server.
- Customizable target host and username.
- Displays attempt count and status (success/failure) for each password.

## Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  
>sudo apt upgrade  

Step 2: Clone the repository  
>git clone https://github.com/The-Real-Virus/SSH-Login-BruteForce.git

Step 3: Go to the Tool Directory where u clone it and read requirements.txt file !  
>cd SSH-Login-BruteForce  
(read requirements.txt file using cat or gedit)

Step 4: extract the rockyou file using unrar  
>sudo apt install unrar (if it is not installed in ur kali linux)  
>unrar x rockyou.rar

Step 5: After Completing the process now u can run script  
>python3 Script.py


## Troubleshooting

1) `Missing :` 'rockyou.txt' file: If the script doesn't find the rockyou.txt file, make sure it is in the same
directory or specify the full path in the script.

2) `SSH Connection Errors:` Ensure the target host allows SSH connections,
and that the username and password list are correct.

3) `Permission Denied:` Ensure the script is run with the necessary privileges.


## MODIFICATION ( use own wordlist )

if u want to use ur own wordlist instead of rockyou.txt , u can modify in the script ,  

Step 1: create ur own wordlist  
Step 2: move it into the SSH Login Brute Force Directory ( deleting rockyou is not necessory )  
Step 3: open the script in editor ( gedit Script.py)  
Step 4: Find These Lines,  
  ''' try:  
  
            with open("rockyou.txt", "r") as password_list:  
                for password in password_list:  
                    password = password.strip("\n")  
                    attempts += 1  
                    print(f"[{attempts}] Attempting Password: '{password}'") '''  

Step 5: Here u can see rockyou.txt , change the name rockyou to ur own wordlist in quotes  
example : with open("mylist.txt", "r") as password_list:  

Step 6: Save the script and run !
