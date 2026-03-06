import os
import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor
import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re
import os
import uuid
import random
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import string
import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import re
import re
import requests
import random
import string
import requests
import random
import concurrent.futures as thread
import os
import string
import requests
import random
import concurrent.futures as thread
import os
import string
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import re
import requests
import os
import random
import time
import random
import requests
from colorama import init, Fore, Style
import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import platform
import os
import random
import uuid
import os
import requests
import random
import string
import uuid
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import json
import time
import uuid
import base64
import re
from concurrent.futures import ThreadPoolExecutor
import re
import requests
import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import os, sys, requests, threading
import sys
import requests
import threading
from time import sleep
from datetime import datetime
import faker
import hashlib
from faker import Faker
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from time import sleep,strftime
from requests import session
from bs4 import BeautifulSoup
import itertools
import threading
import time
import signal
import shutil
import getuseragent
from getuseragent import UserAgent
from rich.panel import Panel
luc    = "\033[1;32m"  # Bright Green
trang  = "\033[1;37m"  # Bright White
do     = "\033[1;31m"  # Bright Red
vang   = "\033[0;93m"  # Bright Yellow
hong   = "\033[1;35m"  # Bright Magenta (Pink)
xduong = "\033[1;34m"  # Bright Blue
xnhac  = "\033[1;36m"  # Bright Cyan
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
gh ="\x1b[38;5;196m"
gh2 = "\x1b[38;5;197m"
gh3 = "\x1b[38;5;198m"
gh4 = "\x1b[38;5;199m"
gh5  = "\x1b[38;5;200m"
gh6 = "\x1b[38;5;201m"
rb = "\x1b[38;5;190m"
rb2 = "\x1b[38;5;191m"
rb3 = "\x1b[38;5;192m"
rb4 = "\x1b[38;5;193m"
rb5 = "\x1b[38;5;194m"
rb6 = "\x1b[38;5;195m"
C = "\x1b[38;5;202m"
C2 = "\x1b[38;5;203m"
C3 = "\x1b[38;5;204m"
C4 = "\x1b[38;5;205m"
C5 = "\x1b[38;5;206m"
C6 = "\x1b[38;5;207m"
Q = "\x1b[38;5;118m"
Q2 = "\x1b[38;5;119m"
Q3 = "\x1b[38;5;120m"
Q4 = "\x1b[38;5;121m"
Q5 = "\x1b[38;5;122m"
Q6 = "\x1b[38;5;123m"
Q7 = "\x1b[38;5;165m"
W11 = "\x1b[42;19m"
BG ="\x1b[47;100m"
BG1 ="\x1b[40;1;37m"
RW= "\x1b[0;95m"
Z1 ="\x1b[38;5;46m"
B = "\x1b[38;5;34m"
B2 = "\x1b[38;5;35m"
B3 = "\x1b[38;5;36m"
B4 = "\x1b[38;5;37m"
B5= "\x1b[38;5;38m"
B6 = "\x1b[38;5;39m"
F = "\x1b[38;5;43m"
F1 = "\x1b[38;5;199m"
F2 = "\x1b[38;5;202m"
F3 = "\x1b[38;5;203m"
F4 = "\x1b[38;5;204m"
F5  = "\x1b[38;5;205m"

COLOR_DEFAULT = Style.RESET_ALL
COLOR_BLUE = Fore.BLUE
COLOR_MAGENTA = Fore.MAGENTA
COLOR_CYAN = Fore.CYAN
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
ICON = '➤ '
ARRAY_ANIMATION = [f'{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}  ', f'   {COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON} ', f'    {COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_RED}{ICON}{COLOR_YELLOW}{ICON}{COLOR_MAGENTA}{ICON}']
end='\033[0m'

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
        
        



    
    

def share112():
    clear()
    ethan()    
    access_token = input('ENTER THE TOKEN: ').strip()
    linex()
    share_url = input('ENTER THE FACEBOOK POST LINK: ').strip()
    linex()
    try:
        share_count = int(input('HOW MANY SHARES WILL THE TOOL STOP: ').strip())
    except ValueError:
        print('{red}INVALID INPUT PLEASE ENTER A NUMBER FOR SHARE COUNT.')
        return
    linex()
    time_interval = 0.001
    delete_after = 3600
    shared_count = 0
    lock = threading.Lock()
    start_time = t.time()
    success_list = []
    headers = {
        'authority': 'b-graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def share_post():
        nonlocal shared_count
        try:
            response = requests.post(
                f'https://b-graph.facebook.com/me/feed?access_token={access_token}&fields=id&limit=1&published=0',
                json={
                    'link': share_url,
                    'privacy': {'value': 'SELF'},
                    'no_story': True,
                },
                headers=headers
            )
            if response.status_code == 200:
                with lock:
                    shared_count += 1
                    success_list.append(response.json().get('id'))
                print(f'{C6} SUCCESSFULLY {green}SHARED {shared_count} {C5} ─────⪼ {green} {share_count}')
                if shared_count == share_count:
                    print('{green}FINISHED SHARING POSTS.')
                    if success_list:
                        threading.Timer(delete_after, delete_post, args=(success_list[-1],)).start()
            else:
                print(f'{red}FAILED TO SHARE POST: {response.json()}')
        except requests.exceptions.RequestException as error:
            print(f'{red}ERROR: {str(error)}')
    while shared_count < share_count:
        share_post()
        #time.sleep(time_interval)
    elapsed_time = t.time() - start_time
    avg_time_per_share = elapsed_time / share_count if share_count > 0 else 0
    total_time = timedelta(seconds=int(elapsed_time))
    avg_time = timedelta(seconds=int(avg_time_per_share))
    print(f"🚀 TARGET: {share_url}")
    print(f"✅ SUCCESSFULLY SHARED: {shared_count}/{share_count}")
    print(f"⏳ TOTAL TIME: {total_time}")
    print(f"⏱️ AVERAGE TIME PER SHARE: {avg_time}")
    linex()

def main():
    clear_screen()
    ethan()
    open('/sdcard/boostphere/FRAACCOUNT.txt', 'a').write('')
    open('/sdcard/boostphere/FRAPAGES.txt', 'a').write('')
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').write('')
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').write('')
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    print(f"""                      ACCOUNT EXTRACTION OVERVIEW
 {blue}──────────────────────────────────────────────────────────────────────────────────────\033[0m
  {blue}     📤FRA ACCOUNT{yellow} : {green}{total_accounts}
  {blue}     📤RPW ACCOUNT{yellow} : {green}{total_account_rpw}
 {blue}──────────────────────────────────────────────────────────────────────────────────────\033[0m""")
    print(f'''  {blue}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓''')
    print(f'''   {blue} ┃   {red}  No.       {white} ┃     {red}       Services       {white}     ┃  {red}      Status         {blue}       ┃ ''')
    print(f''' {blue}   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ''')
    print(f'''   {blue} │    {white}    1      {blue} │     {F1}     Auto Share        {blue}    │        {green}    Active          {blue}  │''')
    print(f'''   {blue} │  {white}      2     {blue}  │   {F1}  Cookies & Token Getter{blue}     |   {green}         Actvive          {blue} │ ''')
    print(f'''  {blue}  │   {white}     3      {blue} │   {F1}   Auto Facebook Creator {blue}    |    {green}        Actvive        {blue}   │ ''')
    print(f'''   {blue} │    {white}    4      {blue} │      {F1}    Auto Share V2     {blue}    │        {green}    Active          {blue}  │''')
    print(f'''   {blue} │    {white}    5      {blue} │     {F1}     Extractor        {blue}     │        {green}    Active          {blue}  │''')
    print(f''' {blue}   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ''')
    choice = input(f"{white} CHOOSE : ").strip()
    if choice == '1':
        share112()
    if choice == '2':
        get_token()
    if choice == '3':
        main3()
    if choice == '4':
        main2()
    if choice == '5':
        extraction()
    if choice == '9':
        clear_text_files()

    else:
        print(f"{red}Invalid choice, exiting.")

if __name__ == "__main__":
       #generate_and_check_code()
       main()
   
