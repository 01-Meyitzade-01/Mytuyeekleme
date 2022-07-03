from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    '   _____             __',
    '  /  _  \    _______/  |_____________',
    ' /  /_\  \  /  ___/\   __\_  __ \__  \\',
    '/    |    \ \___ \  |  |  |  | \// __ \_',
    '\____|__  /____  >  |__|  |__|  (____   /',
    '        \/     \/                     \/'
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Version: 1.2 | Author: Cryptonian{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yeni hesap ekle'+n)
    print(lg+'[2] Tüm yasaklı hesapları filtrele'+n)
    print(lg+'[3] Belirli hesapları sil'+n)
    print(lg+'[4] Astranızı güncelleyin'+n)
    print(lg+'[5] Çıkış'+n)
    a = int(input('\nSeçimini gir: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Eklenecek hesap sayısını girin: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Telefon Numarasını Girin: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Tüm hesapları şuraya kaydetti: vars.txt')
            clr()
            print(f'\n{lg} [*] Logging in from new accounts\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Giriş başarılı')
                c.disconnect()
            input(f'\nAna menüye gitmek için entera basın...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesap yok! Lütfen biraz ekleyin ve tekrar deneyin')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3939406 , 'BAAqza4DFV-aEvgEAqsr37s1rxNqQE92ymPBIGOHSGsTsrK3ma1X_PrFYHAgvKWI0wkdmw3uUyYsx5gsB1DKGlaP6446yE1mqnJDJUvjX7vFj0syb6OVGpSG1OfBI0xRFeqexSV9vbeS2x2VWoFIDROLy-bpsuXe9l6eoI5H1lin2IPcfop_emdks3ypUsx3LdB2s_zra6eLE-I4Js-gpq05KGzgcALmPspPpBZjO9RKGX6mECxyNQG8wkTxScZzcJIdA-syp5zIzzaN8419WW1H6A79HPg8HBtTDFm-vRrdepOg-vvRAPBE3IbI3puZBoNwNTT2SiMHHC_x9gwBCrTaWwtv0QA')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] kodu giriniz: '))
                        print(f'{lg}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Tebrikler! Yasaklı hesap yok')
                input('\nAna menüye gitmek için entera basın...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Engellenen tüm hesaplar kaldırıldı'+n)
                input('\nAna menüye gitmek için entera basın...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Silmek için bir hesap seçin\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Bir seçim girin: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesap Silindi{n}')
        input(f'\nAna menüye gitmek için entera basın...')
        f.close()
    elif a == 4:
        # aşağıdaki snippet için github.com/th3unkn0n adresine teşekkürler
        print(f'\n{lg}[i] Güncellemeleri kontrol etme...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt')
        except:
            print(f'{r} İnternete bağlı değilsin')
            print(f'{r} Lütfen internete bağlanın ve tekrar deneyin')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Güncellemeler indiriliyor...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/manager.py')
                print(f'{lg}[*] Updated to version: {version.text}')
                input('Çıkmak için entera basın...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('Ana menüye gitmek için entera basın...')
        else:
            print(f'{lg}[i] Astra'nız zaten güncel')
            input('Ana menüye gitmek için entera basın...')
    elif a == 5:
        clr()
        banner()
        exit()
