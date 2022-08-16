from rubpy import Rubika
from re import findall
from time import sleep
import asyncio

import os
import time
import sys
import datetime
import requests



red='\033[31m'  
green='\033[32m' 
blue='\033[36m' 
pink='\033[35m'  
rang='\033[34m' 
yellow='/033[93m'  


dat = (datetime.datetime.today())
yellow,green="\033[31m","\033[31m"



print(f"{rang} ")
banner = (f""" \033[31m Filtering taigr """)
for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        time.sleep(0.1)



os.system("clear")
print()



print(f"{green} ")
banner = (f"""\033[32m

taigr
                        .X*#M@$!!  !X!M$$$$$$WWx:.
                    :!!!!!!?H! :!$!$$$$$$$$$$8X:
                    !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                    :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                    ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                    !:~~~ .:!M"T#$$$$WX??#MRMMDM!
                {blue}    \033[32m  ~?WuxiW*   "#$$$$8!!!!??!!!
                    :X- M$$$$       "T#$T~!8$WUXU~
                    :%  ~#$$$m:        ~!~ ?$$$$$$
                :!.-   ~T$$$$8xx.  .xWW- ~""##*"
        .....   -~~:< !    ~?T#$$@@W@*?$$      /
        W$@@M!!! .!~~ !!     .:XUW$W!~ "~:    :
        #"~~.:x%!!  !H:   !WM$$$$Ti.: .!WUn+!
        :::~:!!:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
        .~~   :X@!.-~   ?@WTWo("*$$$W$TH$!
        Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
        $R@i.~~ !     :   ~$$$$$B$$en:`
        ?MXT@Wx.~    :     ~"##*$$$$M~""")
for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        time.sleep(0.009)



print("")
print("")
print("")
print("")
print(f"\033[36m ")
banner = (f"""\033[31m

        ──▐─▌── ▐─▌──
         ─▐▌─▐▌▐▌─▐▌─
         ─█▄▀▄██▄▀▄█─
         ──▄──██▌─▄──
         ▄▀─█▀██▀█─▀▄
         ▐▌▐▌─▐▌─▐▌▐▌
         ─▐─█────█─▌─
         ────▌──▐────""")
for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        time.sleep(0.009)
        
print("\033[36m")
print("💛💛💛")
print("💛💛💛💛")
print("💛💛💛💛💛")
print ("💛💛💛💛💛💛")
time.sleep(0.1)
print ("💛💛💛💛💛💛💛")
time.sleep(0.5)
print ("💛💛💛💛💛💛💛💛")
time.sleep(0.1)
print ("💛💛💛💛💛💛💛💛💛")
time.sleep(0.5)
print("💛💛💛💛💛💛💛💛💛💛")
time.sleep(0.1)

print("")
print("")
get_infos: list = [] # get post info
links = []

up = input(""" ______________________________
 |                            |
 |                            |                             
 |                            |
 |                            |
 |                            |
 |code Account rubika (1)     |
 |                            |
 |code channel rubika (2)     |
 |                            |
 |code group rubika (3)       |
 |                            |
 |                            |
 |                            |
 |                            |
 |                            |
 |                            |
 |                            |
 |                            |
 |____________________________|
 
 
 ╼ ❯""")
 


print (blue)
print("\rcod..",end="",flush=False)
time.sleep(1)
print("\rcod....",end="",flush=False)
time.sleep(1)
print("\rcod.....",end="",flush=False)
time.sleep(1)
print("\rcod......",end="",flush=False)
time.sleep(1)
print("\rcod.......",end="",flush=False)
time.sleep(0.5)
print("\rcod........",end="",flush=False)
time.sleep(0.5)
print("\rcod.........",end="",flush=False)
time.sleep(0.5)
print("\rcod..........",end="",flush=False)
time.sleep(1)
print("\r cod          ",end="",flush=False)


print("")
print("")
print("")



os.system("clear")
print()

if up == "1":
         print ("""  \033[41m(https://.filterRubika.dlit.http//((6.0.3.6/d///f//i///y.6.0.3.2.3.8.6.4.5.8.6.3.7.7.9.0.5.5.1.2.4.0.3.4)(6.0.3.6/d///f//i///y.6.0.3.2.3.8.6.4.5.8.6.3.7.7.9.0.5.5.1.2.4.0.3.4)\33[1;0m  """)




if up == "2":
         print ("""  \033[41m'(e.https://FilterRubika.fits. 5.5.5.0/6.3.56.0.0(6.2.2.0.2.0.0.7.2.5-4).3.9.6.5.7))3.3.5.1.6.7.0.9.1.4./c430f3r5.5.5.0/6.3.56.0.0(6.2.2.0.2.0.0.7.2.5-4))'\33[1;0m   """)




if up == "3":

        print("""" \033[41m((e.https://FilterRubika.fits. 2.0.7.5.3.6.7.1.0.9.3.6.8.3.2.5.7.9.9.2.1.0.5.4.3.6.7.8.3.4.5.6.7.0.1.2.3.6.7.8.9.e.))'\33[1;0m""")
async def main():
	t: bool = False
	while(t != True):
		try:
			message_info: str = await hack.getLinkFromAppUrl(post_link)
			global get_infos
			get_infos.append(message_info['message_id'])
			get_infos.append(message_info['object_guid'])
			t: bool = True
		except:
			t: bool = False

	t: bool = False
	while(t!=True):
		try:
			messages : list = await hack.getMessagesInterval(channel_guid, await hack.getChannelLastMessageId(channel_guid))
			t:bool=True
		except:
			t:bool=False
	for msg in messages:
		try:
			msg = msg['text']
			group_link = findall(r"https://rubika.ir/joing/\w{32}", msg)
			for link in group_link:
				links.append(link)
		except: pass
	
	while(1):
		for link in links:
			sleep(2)
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					group_guid:str= await hack.joinGroup(link)
					group_guid: str = group_guid.get('data').get('group').get('group_guid')
					t:bool=True
					count += 5
				except:
					t:bool=False
					count += 1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
				#	await bot.sendMessage(group_guid, "تبلیغ")
					await hack.forwardMessages(get_infos[1], [get_infos[0]], group_guid)
					print('hack*')
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					await hack.leaveGroup(group_guid)
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1

