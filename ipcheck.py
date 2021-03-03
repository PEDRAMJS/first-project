import MySQLdb
import ipaddress
import threading
import subprocess
ipl=[]
def ipcheck(x):
    ipl.append(x)
    print ('======={CHECKING}====>>>'+x)
    res=subprocess.call(['ping '+x+' -c 1 -W 1'],shell=True,universal_newlines=True,stdout=subprocess.PIPE,)
    if res ==0:
        print ('=========='+' Host is   up '+'==========(@_@)')
    elif res < 2:
        print ('=========='+' Host is down '+'==========(X_X)')
for ip in ipl:
    t=threading.Thread(target=ipcheck(ip))
dbcon= MySQLdb.connect(user='pedram',password='321321',host='localhost',database='pedram')
cur=dbcon.cursor()
cur.execute('select ip from ip_ping ip')
for dbn in cur: