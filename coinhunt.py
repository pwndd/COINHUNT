import time
import decimal
import os
import sys
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
from faker import Faker
import platform
import psutil
import random
import string
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("COINHUNT 2.4 - STATUS: IDLE")

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (------------)                                  ","cyan"))
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (====>-------)                                  ","cyan"))
print(colored("                             CHECKING RESOURCES.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (========>---)                                  ","cyan"))
print(colored("                            ALLOCATING RESOURCES.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","cyan"))
print(colored("                                LOAD SUCCESS.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
clear()
print("")
time.sleep(0.05)
print("")
time.sleep(0.03)
print(colored("               █████╗  █████╗ ██╗███╗  ██╗██╗  ██╗██╗   ██╗███╗  ██╗████████╗","cyan"))
time.sleep(0.03)
print(colored("              ██╔══██╗██╔══██╗██║████╗ ██║██║  ██║██║   ██║████╗ ██║╚══██╔══╝","cyan"))
time.sleep(0.03)
print(colored("              ██║  ╚═╝██║  ██║██║██╔██╗██║███████║██║   ██║██╔██╗██║   ██║   ","cyan"))
time.sleep(0.03)
print(colored("              ██║  ██╗██║  ██║██║██║╚████║██╔══██║██║   ██║██║╚████║   ██║   ","cyan"))
time.sleep(0.03)
print(colored("              ╚█████╔╝╚█████╔╝██║██║ ╚███║██║  ██║╚██████╔╝██║ ╚███║   ██║   ","cyan"))
time.sleep(0.03)
print(colored("               ╚════╝  ╚════╝ ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝   ","cyan"))
time.sleep(0.03)
print("")
time.sleep(0.03)
print("")


welcome = Fore.CYAN + "Welcome back! The script will automatically detect the best settings and auto-complete them for you.\n"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)

threads = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "coinhunt threads set 400\n"
for char in threads:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "Successfully set threads to 400.")

server = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "coinhunt server connect fastest\n"
for char in server:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "Checking subscription...")
time.sleep(5.0)
print(Fore.LIGHTMAGENTA_EX + "Subscription valid!")
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Connecting to fastest server...")
time.sleep(0.5)

list1 = ["ARGENTINA", "UK", "US", "RUSSIA", "GERMANY", "ITALY", "FRANCE", "POLAND", "SPAIN", "CHINA", "JAPAN", "INDIA", "BRAZIL", "INDONESIA", "AUSTRALIA", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND", "VIETNAM", "HONG KONG", "SOUTH KOREA", "TAIWAN", "JAPAN", "PHILIPPINES", "SINGAPORE", "MALAYSIA", "THAILAND",]
cntry = random.choice(list1)
ipss = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))

print(Fore.LIGHTMAGENTA_EX + "Testing server: ")
time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "Pinging " + str(cntry) + "-" + str(random.choice(range(1, 30))) + " [" + str(ipss) + "]" + " with 32 bytes of data:")
time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "Reply from " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(1)
print(Fore.LIGHTMAGENTA_EX + "Reply from " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(0.7)
print(Fore.LIGHTMAGENTA_EX + "Reply from " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(0.2)
print(Fore.LIGHTMAGENTA_EX + "Reply from " + str(ipss) + ": " + "bytes=32 time=" + str(random.choice(range(1, 30))) + " TTL=55")
time.sleep(2)

print(Fore.LIGHTMAGENTA_EX + "Connected.")

user = input(Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "How many wallets to go through?: ")
user = int(user)

start = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "coinhunt hunt start\n"
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)



time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Launching hunter.")
time.sleep(1.5)

print("")
print("")

ctypes.windll.kernel32.SetConsoleTitleW("COINHUNT VERSION 2.3 - STATUS: MINING")

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.CYAN + "COINHUNT" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTRED_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.RED + "0.00 BTC" + Fore.WHITE + "]")

for i in range(user):
    get_random_string(35)
    time.sleep(0.1)
    
winner = decimal.Decimal(random.randrange(20, 250))/100

letters = string.ascii_uppercase + string.digits
heheha = ''.join(random.choice(letters) for i in range(35))

def get_random_win(length):
    print(Fore.WHITE + "[" + Fore.CYAN + "COINHUNT" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTGREEN_EX + str(heheha) + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + str(winner) + " BTC" + Fore.WHITE + "]")

time.sleep(0.3)

get_random_win(35)

time.sleep(0.5)

ctypes.windll.kernel32.SetConsoleTitleW("COINHUNT VERSION 2.3 - STATUS: FOUND BTC!")

print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "COINHUNT" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " SAVING " + str(winner) + " BTC TO RESULTS.TXT" + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]") 
time.sleep(1)

fp = open('results.txt', 'w')
fp.write(heheha + ": " + str(winner) + " BTC")
fp.close()

print("")
print(Fore.CYAN + "COINHUNT IS NOW CLOSING...\nHave a nice day!")
time.sleep(1)

closing = Fore.CYAN + "COINHUNT 2022"
for char in closing:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

time.sleep(1)
print(Fore.RESET)