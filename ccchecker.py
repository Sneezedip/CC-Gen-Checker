from colorama import Fore, Style
import msvcrt as key
import os
def Menu():
    os.system("cls")
    user_input = None
    valid_inputsc = {b'1', b'3'}
    print(Fore.MAGENTA, Style.BRIGHT, """
 ▄████▄   ▄████▄      ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ▀█  ▒██▀ ▀█     ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒▓█    ▄    ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░▒ ▓███▀ ░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ░▒ ▒  ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░  ▒        ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░        ░           ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
░ ░      ░ ░         ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                    {2}https://github.com/Sneezedip   

    {1}[1] - {0}CHECK!
    {1}[3] - {0}Exit

    """.format(Fore.LIGHTYELLOW_EX,Fore.BLUE,Fore.MAGENTA), Style.RESET_ALL)
    user_input = key.getch()
    if user_input in valid_inputsc:
        if user_input == b'1':os.system("cls");checker()
        elif user_input == b'3': os.system('cls');exit()
        else:os.system('cls');Menu()
    else:os.system('cls');Menu()

def checker():
    cards = []
    cards_full = []
    while True:
        print(Fore.RED, "                                        [INFORMATION]")
        print(Fore.MAGENTA, "Input your full txt location with the cards organized by (card|exp|cvv) or else it won't work")
        print(Fore.GREEN, "Consider using my cc generator! discord- .sneezedip\n")
        print(Fore.RED, "[WARNING] NEVER USE YOUR PERSONAL INFORMATION! [WARNING]\n")
        card_Location = input(f"{Fore.YELLOW}--> {Style.RESET_ALL}")
        try:
            with open(card_Location, "r") as file:
                card_lines = file.readlines()
                for card in card_lines:
                    cards_full.append(card)
                    cards.append(card.split("|")[0].replace(" ", "").strip())
            break
        except FileNotFoundError:
            print("Invalid txt file or Location not found")
    i = 0
    for card in cards:
        single = []
        for index, number in enumerate(card):
            if index % 2 == 0:
                n = int(number) * 2
                if n > 9:
                    n -= 9
                single.append(int(n))
            else:
                single.append(int(number))
        total_sum = sum(single)
        is_valid = total_sum % 10 == 0
        color = Fore.GREEN if is_valid else Fore.RED
        print(f"{color}[X] Card: {cards_full[i]} | Valid: {is_valid}{Style.RESET_ALL}")
        with open ("validcards.txt","a") as file:
            file.write(cards_full[i])
        i += 1
    print(Fore.GREEN,"DONE!")
    print(Fore.GREEN,"Thanks for using snee checker! any infos add discord : .sneezedip")
    input("any key to return...")
    Menu()
Menu()