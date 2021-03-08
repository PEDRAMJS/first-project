import MySQLdb
import concurrent.futures   
import threading
import subprocess
ipl=[]
dbcon= MySQLdb.connect(user='pedram',password='321321',host='localhost',database='pedram')
cur=dbcon.cursor()
cur.execute('select ip from ip_ping')
for ipn in cur:
    d=list(ipn)
    ipl.append(d[0])


class pedram:
    def ipcheck(x):
        print ('=======[CHECKING]====>>>'+x)
        res=subprocess.call(['ping '+x+' -c 5 -W 1'],shell=True,universal_newlines=True,stdout=subprocess.PIPE,)
        if res ==0:
            print ('=========='+' Host is   up '+'==========(@_@)')
        elif res > 0:
            print ('=========='+' Host is down '+'==========(X_X)')   
        return
t = threading.Thread(target=pedram.ipcheck(ip))