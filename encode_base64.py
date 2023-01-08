import pyfiglet
import os 


import base64
from time import sleep

import webbrowser



#print("\033[3m")
#31 m     سرخ
red="\033[91m"
#32m   سبز
green="\033[92m"

#zard   زرد

zard="\033[93m"

#lagvary    لاجوری 
lagvary="\033[94m"

#galby

glaby="\033[95m"

#cyan

cyan="\033[96m"
#سفید

withe ="\033[97m"


###№#######
#green##

logo = """
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`
---------------------------------------------
\033[1;96m|-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|
\033[1;96m|               Talha Technology Channel              |
\033[1;96m|This Tool is Only for Bangladesh FB Acounts|
\033[1;96m|------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|
\033[1;91m [⚡\033[1;97mAuthor Name: Talha     ⚡\033[1;91m]
\033[1;91m [⚡\033[1;97mYutube Channel: Talha Technology ⚡\033[1;91m]
\033[1;91m [⚡       \033[1;97mWhatsApp: +9934388986 ⚡\033[1;91m]
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mTalhaYT\033[1;95m-_-_-_-_-_-_-_-_-»
"""

print(logo)
webbrowser.open("https://www.facebook.com/profile.php?id=100079226812922")

def pyfiglet_1():
	name="Kyhan"
	name_1=pyfiglet.figlet_format(name,font="big")
	print(green+name_1)
	
	
###

def pyfiglet_2():
	name="Kyhan"
	name_1=pyfiglet.figlet_format(name,font="big")
	
	print(glaby+name_1)
	
	
###### addreesess 

s="_"

def addresses():
	print(red+s*200+"""
	name	 is:    """+green+"""kyhan 
	fone   	is:    """+glaby+""" 09934388986
	"""+cyan+"""gmaile is: """+red+"""     kyhan@gmial.com
				
			""")
#addresses()

sleep(1.0)

print("""



""")


os.system("cdg-open  https://www.facebook.com/profile.php?id=100079226812922")

webbrowser.open("https://www.facebook.com/profile.php?id=100079226812922")


addresses()
print(s*150)
print("""
	
	
	""")
	
print(green+"""encrypt base64 """+glaby+"""[1]""")
print("""""")
print(green+"""decrypt base64 """+glaby+"""[2]""")
	
print("""
	
	
	""")
	

import base64
from time import sleep
#31 m     سرخ
red="\033[91m"
#32m   سبز
green="\033[92m"

#zard   زرد

zard="\033[93m"

#lagvary    لاجوری 
lagvary="\033[94m"

#galby

glaby="\033[95m"

#cyan


cyan="\033[96m"
#سفید

withe ="\033[97m"


####
def encrypt_1():
	os.system("clear")
	pyfiglet_2()
	
	file=input(glaby+"Enter file adresses :")
	sleep(2.4)
	open_file=open(file,"r").read()
	dd=open_file.encode("utf-8")
	enc=base64.b16encode(dd)
	print("""   
	
	""")
	print(open_file)
	
	sleep(1.0)
	
#	print(green,enc)
	
	print("""
	
	""")
	
	sleep(1.0)
	
	file_1=input(glaby+"Enter file adresses :")
	sleep(2.0)
	open_file_1=open(file_1,"wb")
	
	ss=open_file_1.write(enc)
	sleep(3.0)
	
	
	
#encrypt_1()
webbrowser.open("https://www.facebook.com/profile.php?id=100079226812922")	
os.system("cdg-open  https://www.facebook.com/profile.php?id=100079226812922")	
	
def decrypt_1():
	os.system("clear")
	pyfiglet_2()
	sleep(2.0)
	addresses()
	
	sleep(1.0)
	


	
	file=input(glaby+"Enter file adresses :")
	
	sleep(2.4)
	open_file=open(file,"r").read()
	
	dec=base64.b16decode(open_file).decode("utf-8")
	print("""
	
	""")
	sleep(2.0)
#	print("encrypt is   "+green,open_file)
	print("""
	
	""")
	sleep(1.0)
	print("decrypt is :   "+cyan,dec)
	
	print("""
	
	""")
	sleep(3.0)
	
	file_1=input(glaby+"Enter adsresses :")
	
	open_file_1=open(file_1,"w")
	open_file_1.write(dec)

input_1=input(cyan+"Enter   wat add :")

if input_1==str(1):
	
	encrypt_1()
	
else:
	decrypt_1()

	

























