ipl=['a','b','c','d']
ipl2=[]
c=0
b=0
print(ipl)
print(ipl2)
while c < 1 :
    if len(ipl2) < 5:
        ipl2.append(ipl[b])
        b= b + 1
    if b == 5 :
        ipl=[]
        ipl2=[]
print(ipl)
print(ipl2)