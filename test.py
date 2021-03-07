import MySQLdb
import time
import concurrent.futures   
import threading
import subprocess
ipl=[]
Aip=[]
Xip=[]
dbcon= MySQLdb.connect(user='pedram',password='321321',host='localhost',database='pedram')
cur=dbcon.cursor()
cur.execute('select ip from ip_ping')
for ipn in cur:
   d=list(ipn)
   ipl.append(d[0])
def ipcheck(x):
   print ('=======[CHECKING]====>>>'+x)
   res=subprocess.call(['ping '+x+' -c 5 -W 1'],shell=True,universal_newlines=True,stdout=subprocess.PIPE,)
   if res ==0:
      Aip.append(x)
      print ('=========='+' Host '+x+' is   up '+'==========(@_@)')
   elif res > 0:
      Xip.append(x)
      print ('=========='+' Host '+x+' is down '+'==========(X_X)')   
   return
def concurrency():
   with concurrent.futures.ThreadPoolExecutor() as executor:
      t1 = executor.map(ipcheck,ipl)
concurrency()
print(Xip)
print('Dead ip')
print(Aip)
print('Alive ip')