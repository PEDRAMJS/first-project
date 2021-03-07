import MySQLdb
ipl=[]
con=MySQLdb.connect(user='pedram',password='321321',host='localhost',database='pedram')
cur=con.cursor()
cur.execute('select * from ip_ping ip')
for ip in cur :
   d=list(ip)
   ipl.append(d[0])
   print(ipl)
   