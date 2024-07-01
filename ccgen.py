
import time
from colorama import Fore, Style
import msvcrt as key
import random
import os

try:
    import ccard
except ModuleNotFoundError:
    print("Installing libraries...")
    os.system("pip install ccard")
    time.sleep(5)
bins = "No BIN"

def cardgen():
    global bins
    user_input = None
    valid_inputsc = {b'1', b'3'}
    print(Fore.BLUE, Style.BRIGHT, """
    ▄████▄   ▄████▄       ██████  ███▄    █ ▓█████ ▓█████
    ▒██▀ ▀█  ▒██▀ ▀█     ▒██    ▒  ██ ▀█   █ ▓█   ▀ ▓█   ▀
    ▒▓█    ▄ ▒▓█    ▄    ░ ▓██▄   ▓██  ▀█ ██▒▒███   ▒███
    ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒     ▒   ██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒▓█  ▄
    ▒ ▓███▀ ░▒ ▓███▀ ░   ▒██████▒▒▒██░   ▓██░░▒████▒░▒████▒
    ░ ░▒ ▒  ░░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░░ ▒░ ░
    ░  ▒     ░  ▒      ░ ░▒  ░ ░░ ░░   ░ ▒░ ░ ░  ░ ░ ░  ░
    ░        ░           ░  ░  ░     ░   ░ ░    ░      ░
    ░ ░      ░ ░               ░           ░    ░  ░   ░  ░
    ░        ░
                    {0}https://github.com/Sneezedip   

    {1}[1] - {0}Generate card
    {1}[3] - {0}Exit

    """.format(Fore.RED,Fore.CYAN), Style.RESET_ALL)
    user_input = key.getch()
    if user_input in valid_inputsc:
        if user_input == b'1':
            ccgen()
        elif user_input == b'3':
            os.system('cls')
            exit()
        else:
            os.system('cls')
            cardgen()
    else:
        os.system('cls')
        cardgen()

def ccgen():
    global bins, file, txt_name, cards_qt, user_input
    valid_inputsc = {b'1', b'2'}
    cards_qt = 0
    if bins == "No BIN":
        bins = None
        cards_qt = int(
            input(f"{Fore.CYAN}How many cards?{Style.RESET_ALL}"))
        print(f"""
            {Fore.BLUE}Do you want to save the cards in a .txt file?
            {Fore.CYAN}[1] - {Fore.YELLOW}Yes
            {Fore.CYAN}[2] - {Fore.YELLOW}No
            """)
        user_input = key.getch()
        if user_input in valid_inputsc:
            if user_input == b'1':
                program = True
                file = True
                print(f"""
                How do you want to appear in the txt?
                {Fore.CYAN}[1] - {Fore.YELLOW}card_number|expire|cvv
                
                {Fore.CYAN}[2] - {Fore.YELLOW}card_number
                    expire
                    cvv
                """)
                option = key.getch()
                print("TXT NAME")
                txt_name = input("↪ ")
            if user_input == b'2':
                program = True
                file = False
        while program:
            for i in range(0, cards_qt):
                card = ccard.visa()
                month = ''.join(str(random.randint(8, 12)))
                year = ''.join(str(random.randint(24, 27)))
                cvv = ''.join(str(random.randint(100, 999)))
                if int(month) >= 1 and int(month) <= 9:
                    month = '0'+str(month)
                else:
                    continue
                expire = f"""{month}|20{year}"""
                if file == True:
                    if option == b'1':
                        with open(f"{txt_name}.txt", "a") as f:
                            f.write(f"{card}|{expire}|{cvv}\n")
                    elif option == b'2':
                        with open(f"{txt_name}.txt", "a") as f:
                            f.write(f"Card #{i+1}")
                            f.write(f"\n[+] Card Number: {card}")
                            f.write(f"\n[+] Expire Date: {expire}")
                            f.write(f"\n[+] CVV : {cvv}")
                            f.write("\n")
                    else:
                        print("error")
                        ccgen()
                else:
                    print(f"Card #{i+1}")
                    print(f"[+] Card Number: {card}")
                    print(f"[+] Expire Date: {expire}")
                    print(f"[+] CVV : {cvv}")
                    print("\n")
            print("Press any key to return to menu...")
            user_input = key.getch()
            os.system('cls')
            cardgen()



cardgen()