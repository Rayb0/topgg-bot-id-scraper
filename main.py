import httpx, threading, json, base64, os, sys
from itertools import cycle

def install(package):
    os.system(f"{sys.executable} -m pip install {package}")

try:
    import httpx
except ModuleNotFoundError:
    install("json")
try:
    import threading
except ModuleNotFoundError:
    install("base64")
try:
    import threading
except ModuleNotFoundError:
    install("itertools")


def get_proxies():
    with open("proxies.txt", "r") as file:
        proxies = file.read().splitlines()
    return proxies

proxy_pool = cycle(get_proxies())

def get_proxy():
    proxy = next(proxy_pool)
    return proxy

def FormatProxy(proxy):
    if '@' in proxy:return proxy
    elif len(proxy.split(':')) == 2:return proxy
    else:
        if '.' in proxy.split(':')[0]:return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
        else:return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])

bro = input('[?] How many ids: ')
def kek():
    try:
        session = httpx.Client(proxies={"https://": f"http://{FormatProxy(get_proxy())}"})
        lol = session.get(f'https://top.gg/api/client/entities/search?platform=discord&entityType=bot&amount={bro}')
        amogus = json.load(lol).get('results')

        for bruh in amogus:
            what = bruh['id']
            print(f"[!] Server: ({what})")
            with open(f'{"servers.txt"}', 'a+') as f:
                f.write(f'{what}\n')
            with open(f'{"serversWinvite.txt"}', 'a+') as f:
                f.write(f'https://discord.com/oauth2/authorize?client_id={what}&permissions=537159744&scope=applications.commands%20bot\n')
    except Exception as e:
        pass

if __name__ == "__main__":
    threading.Thread(target=kek).start()