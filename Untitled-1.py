import random
f=open("numbers.txt")
pierw=[]
def new():
    for i in f:
        n=0
        i=i.strip()
        for x in range(1,int(i)):
            if int(i)%x!=0:
                n+=1
            if n+2==int(i):
                print(int(i))
new()
