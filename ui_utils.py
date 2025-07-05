import os

# 🎨 Terminal Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"

# 🧹 Safe screen clear (even in Termux)
def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass  # Some Termux environments block os.system

# 🖼️ Banner Display
def print_banner():
    print(rf"""{CYAN}
 /$$$$$$$$ /$$ /$$                 /$$$$$$$$                                      /$$$$$$                         
| $$_____/|__/| $$                |__  $$__/                                     /$$__  $$                        
| $$       /$$| $$  /$$$$$$          | $$  /$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$  \__//$$$$$$   /$$$$$$       
| $$$$$   | $$| $$ /$$__  $$         | $$ /$$__  $$|____  $$| $$__  $$ /$$_____/| $$$$   /$$__  $$ /$$__  $$      
| $$__/   | $$| $$| $$$$$$$$         | $$| $$  \__/ /$$$$$$$| $$  \ $$|  $$$$$$ | $$_/  | $$$$$$$$| $$  \__/      
| $$      | $$| $$| $$_____/         | $$| $$      /$$__  $$| $$  | $$ \____  $$| $$    | $$_____/| $$            
| $$      | $$| $$|  $$$$$$$         | $$| $$     |  $$$$$$$| $$  | $$ /$$$$$$$/| $$    |  $$$$$$$| $$            
|__/      |__/|__/ \_______/         |__/|__/      \_______/|__/  |__/|_______/ |__/     \_______/|__/            
{RESET}""")
    print(f"{CYAN}{BOLD}🔐 Welcome to the File_Transfer_Tool — by Abdul Ghaniy 🔐{RESET}\n")

