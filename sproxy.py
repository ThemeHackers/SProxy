import os
import sys
import httpx
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fw = Fore.WHITE
fre = Fore.RESET
author = 'https://github.com/ThemeHackers'
version = '0.0.1'
def banner():
    print(fr + f'''
 ________  ________  ________  ________     ___    ___ ___    ___ 
|\   ____\|\   __  \|\   __  \|\   __  \   |\  \  /  /|\  \  /  /|
\ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \  \ \  \/  / | \  \/  / /
 \ \_____  \ \   ____\ \   _  _\ \  \\\  \  \ \    / / \ \    / / 
  \|____|\  \ \  \___|\ \  \\  \\ \  \\\  \  /     \/   \/  /  /  
    ____\_\  \ \__\    \ \__\\ _\\ \_______\/  /\   \ __/  / /    
   |\_________\|__|     \|__|\|__|\|_______/__/ /\ __\\___/ /     
   \|_________|                            |__|/ \|__\|___|/      
                                       
                                        Dev: {author} Version: {version}                         
          ''' + fre)
proxy_urls = [
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
    'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
    'https://proxyspace.pro/http.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
]
if __name__ == "__main__":
    file = "SProxy/proxy.txt"
    try:
        if os.path.isfile(file):
            os.system('cls' if os.name == 'nt' else 'clear')
            os.remove(file)
            print(f"{fr}File {file} already exists!\n{fy}Starting to download a new {file}!\n")
            banner()
        with open(file, 'a') as data:
            for url in proxy_urls:
                try:
                    response = httpx.get(url)
                    response.raise_for_status()  
                    if response.text.strip(): 
                        proxies = response.text.strip().splitlines()
                        for proxy in proxies:
                            data.write(proxy + "\n")
                        print(f" -| Fetched {fg}{url}")
                    else:
                        print(f"{fr} -| {url} returned empty response")
                except httpx.RequestError as e:
                    print(f"{fr} -| An error occurred while requesting {url}: {e}")

        with open(file, 'r') as count:
            total = sum(1 for line in count)
        print(f"\n{fw}( {fy}{total} {fw}) {fg}Proxies successfully downloaded.")
    
    except Exception as e:
        print(f"{fr}An unexpected error occurred: {e}")
        sys.exit(1)
