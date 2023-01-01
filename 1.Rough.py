
'''n=9

for i in range(1,n+1):
    if i==6:
        break
    print(i)

print("\n","\n")    
n=9

for i in range(1,n+1):
    if i==6:
        continue
    print(i)

print("\n","\n")
n=9

for i in range(1,n+1):
    if i==8:
        pass
    print(i)


def fun(a):
    square=a*a
    return square
print(fun(7))


a=input('Enter any string :')
i=-1
while -len(a)<=i:
      print(a[i])
      i+=-1
 
a=int(input('Enter any number :'))

t=a

r=0

while a!=0:
    d=a%10

    r=r*10+d

    a=a//10
    
if t==r:
    print('It is Palindrome')
else:
    print('It is not a Palindrome')

def fun():
    a=6
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact

print(fun())


a=int(input("Enter no of terms ="))
lst=[]
for i in range(1,a+1):
    b=int(input("Enter any number ="))
    lst.append(b)

for j in range(len(lst)-1):
    for k in range(0,j+1):
        if lst[k]>lst[j+1]:
            s=lst[k]
            lst[k]=lst[j+1]
            lst[j+1]=s
print("Ascending Order of entered numbers =", lst) 

#To arrange in alphabetical order
a=int(input("Enter no of terms ="))
lst=[]
for i in range(1,a+1):
    b=input("Enter any number =")
    lst.append(b)

for j in range(len(lst)-1):
    for k in range(0,j+1):
        if lst[k]>lst[j+1]:
            s=lst[k]
            lst[k]=lst[j+1]
            lst[j+1]=s
print("Alphabetical order =",lst)

a="Divi"
b="Dharshan"

a=a+b
b=a[0:len(a)-len(b)]
a=a[len(b):]

print("a =",a)
print("b =",b)


a="I AM DIVYADHARSHAN"
c=0
for i in range(0,len(a)):
    if a[i] !=' ':
        c+=1
print(c)

board={ '1':' ', '2':' ','3':' ','4':' ', '5':' ','6':' ','7':' ', '8':' ','9':' '}
board_keys = []

for key in board:
    board_keys.append(key)

def printboard(Board):
    print('-------')
    print('|'+ Board['1']+'|'+Board['2']+'|'+Board['3']+'|')
    print('-------')
    print('|'+ Board['4']+'|'+Board['5']+'|'+Board['6']+'|')
    print('-------')
    print('|'+ Board['7']+'|'+Board['8']+'|'+Board['9']+'|')
    print('-------')
    
    
def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printboard(board)
        print("Enter which place you want to place "+ turn +"?")
        print(turn)

        move = input()

        if board[move]==' ':
            board[move]=turn
            count+=1
        else:
            print("That place already filled, Enter another place..")
            continue

        if count>=5:
            if board['7']==board['8']==board['9'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['4']==board['5']==board['6'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['1']==board['2']==board['3'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['1']==board['4']==board['7'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['2']==board['5']==board['8'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['3']==board['6']==board['9'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['1']==board['5']==board['9'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break
            elif board['3']==board['5']==board['7'] !=' ':
                printboard(board)
                print("\n\tGame Over")
                print("****"+ turn +" won*****")
                break


        if count==9:
            print("Game Over..")
            print("It's a Tie")
            

        
        if turn=='X':
            turn='O'
        else:
            turn='X'

game()

a="COMPUTER"
c=len(a)
for j in range(1,c+1):
    print(a[:j])
for i in range(1,c+1):
    print(a[:c])
    c-=1


n=int(input("Enter limit ="))

for i in range(2,n):
    if n%i==0:
        break
    else:
        print(i)

str="COMPUTER"
j=0
for i in str:
    print(str[:j+1])
    j+=1

str="COMPUTER"
j=len(str)
for i in str:
    print(str[:j])
    j-=1

try:
     n=int(input("Enter Number :"))
     print(n)
except:
     print("IDIOT, ENTER NUMBER(NOT STRING OR SPECIAL CHARACTERS)")
    

'''
'''
import csv

n=int(input("Enter no of students :"))
#csv.register_dialect('dialect',lineterminator='\n')
mylist=[]

for i in range(n):
     name=input("Enter Name :")
     clas=input("Enter Class :")
     #tot=int(input("Enter Total :"))
     #rank=int(input("Enter Rank :"))
     #c=int(input("Enter Cut-OFF :"))
     
     mylist.append([name,clas])

Fileobj=open("D:\\Mark.csv","w")
#writeobj=csv.writer(Fileobj,dialect='dialect')
print(mylist)
for i in mylist:
     writeobj.writerow(i)
Fileobj.close()'''

'''import sqlite3

con=sqlite3.connect('ABD.db')
cur=con.cursor()

#s="""CREATE TABLE student(NAME char(30), AGE integer primary key);"""
#cur.execute(s)

#s="""INSERT INTO student VALUES("S.DIVYADHARSHAN",NULL),("R.N.SHARAVANA KUMAR",NULL),("R.N.DEEPIKA",NULL);"""
#cur.execute(s)

s="""SELECT*FROM student;"""
cur.execute(s)

r=cur.fetchall()
for i in r:
     print(i)

con.commit()
con.close()'''


'''
import sqlite3

con=sqlite3.connect('ac.db')
cur=con.cursor()

#S="""CREATE TABLE input(NAME char(30),CLASS varchar(20));"""
#cur.execute(S)
#print("TABLE CREATED")

"""n=int(input("Enter no of inputs :"))

for i in range(n):
     name=input("Enter Name :")
     clas=input("Enter Class :")

     cur.execute("INSERT INTO input VALUES(?,?)",(name,clas))
"""
S="""SELECT*FROM input;"""
cur.execute(S)

c=[i[0] for i in cur.description]
print(c)

r=cur.fetchall()
for i in r:
     print(list(i))
   
con.commit()
con.close()
'''
'''
import csv
csv.register_dialect('dia',lineterminator='\n')

n=int(input('ENTER NUMBER OF STUDENTS :'))

a=[]

for i in range(n):
     name=input('\nENTER NAME :')
     clas_sec=input('ENTER CLASS AND SEC :')
     roll=int(input('ENTER ROLL NUMBER :'))
     print('\t**** ENTER YOUR MARKS SUBJECT-WISE ****')
     eng=int(input('\tENGLISH :'))
     lang=int(input('\tLANGUAGE :'))
     mat=int(input('\tMATHEMATICS :'))
     comp=int(input('\tCOMPUTER SCIENCE :'))
     phy=int(input('\tPHYSICS :'))
     che=int(input('\tCHEMISTRY :'))

     tot=eng+lang+mat+comp+phy+che

     a.append([name,clas_sec,roll,tot])

for i in a:
     print(i)
'''
'''
import sqlite3

con=sqlite3.connect('kk.db')
cur=con.cursor()

#st="""CREATE TABLE detail(NAME char(40), EMP_NO integer, PLACE varchar(40));"""#
#cur.execute(st)
for x in range(4):
     print("\n1.INSERTING RECORDS\n2.UPDATING RECORS\n3.DELETING RECORDS\n4.TO PRINT RECORDS\n5.EXIT")
     n=int(input('\nENTER YOUR CHOICE :'))
     if n==1:
          q=int(input("ENTER NO OF RECORDS YOU WANT TO ADD :"))
          for x in range(q):
               a=input('\nENTER NAME :')
               b=int(input('ENTER EMPLOYEE NUMBER :'))
               c=input('ENTER PLACE :')

               cur.execute("INSERT INTO detail VALUES(?,?,?)",(a,b,c))
     elif n==2:
          print("\n1.TO UPDATE NAME\n2.TO UPDATE EMPLOYEE NUMBER\n3.TO UPDATE PLACE")
          ch=int(input('\nENTER CHOICE :'))
          if ch==1:
               n_name=input("\nENTER NEW NAME :")
               o_name=input("ENTER OLD NAME :")

               cur.execute("UPDATE detail SET NAME=(?) WHERE NAME=(?)",(n_name,o_name))
          elif ch==2:
               n_emno=int(input("\nENTER NEW EMPLOYEE NUMBER :"))
               o_emno=int(input("ENTER OLD EMPLOYEE NUMBER :"))

               cur.execute("UPDATE detail SET EMP_NO=(?) WHERE EMP_NO=(?)",(n_emno,o_emno))

          elif ch==3:
               n_place=input("\nENTER NEW PLACE :")
               o_place=input("ENTER OLD PLACE :")

               cur.execute("UPDATE detail SET PLACE=(?) WHERE PLACE=(?)",(n_place,o_place))
          else:
               print("ENTER AVAILABLE CHOICE")

     elif n==3:
          d=input("\nENTER EMPLOYEE NUMBER TO DELETE RECORD :")

          cur.execute("DELETE FROM detail WHERE EMP_NO=(?)",(d))

     elif n==4:
          st="""SELECT*FROM detail;"""
          cur.execute(st)
          d=[k[0] for k in cur.description]
          print(d)
          r=cur.fetchall()
          for i in r:
               print(list(i))

     elif n>4:
          break

con.commit()
con.close()
'''
'''
import sqlite3
con=sqlite3.connect("sample3.db")
cur=con.cursor()
s="""SELECT name FROM sqlite_master WHERE type="table" """
cur.execute(s)
r=cur.fetchall()
print(*r,sep="\n")
con.close()
'''
'''
import pywhatkit as p

p.sendwhatmsg("+919940282465","I AM SENDING THIS MESSAGE THROUGH WHATSAPP",14,53)
'''
'''

import csv,operator

u=open("D:\\sample.csv","r")
 
r=csv.reader(u)
next(r)

a=int(input("Enter column according to which you want to sort :"))

s=sorted(r,key=operator.itemgetter(a-1))

for l in s:
     print(l)
'''
'''
import operator

a=[["KEYBOARD",48,12000],["MONITOR",52,23000],["MOUSE",20,4000]]

s=sorted(a,key=operator.itemgetter(2))

for i in s:
     print(i)'''
'''
import time
from time import sleep

a="HI SATHYAVATHI"

for i in a:
     print("\t\t",i);sleep(0.4)
'''
'''
import upsidedown

print(upsidedown.transform("HI DIVYADHARSHAN"))

'''
'''
import sqlite3

c=sqlite3.connect("DD.db")
cu=c.cursor()

cu.execute("DROP TABLE one;")
s="""CREATE TABLE one(Name char(50),Age integer,DOB date,Average float);"""
cu.execute(s)

s="""INSERT INTO one VALUES("Nethaji",24,"2004-1-1",96.8),("DIVI",19,"2003-9-1",65.3),("DEVIL",21,"2004-8-1",56.3),("AMBANI",17,"2004-2-1",98.5);"""
cu.execute(s)

cu.execute("""SELECT*FROM one WHERE(DOB>="2003-1-1" AND DOB<="2004-6-1");""")
r=cu.fetchall()
z=[i[0] for i in cu.description]
print(tuple(z))
print(*r,sep="\n")

c.commit()
c.close()
'''
'''
import qrcode

n=input("Enter anything :")
i=qrcode.make(n)
i=save('D://dd1.jpg')
'''
'''
import capi

s=capi.convert("divi")
print(s)'''
"""
import dharshan
b=int(input("Enter number of inputs :"))
d=[]
for i in range(b):
     c=input("Enter anything :")
     d.append(c)

dharshan.asc_sort(d)
dharshan.des_sort(d)
a=input("Enter anything :")
dharshan.dec_to_bin(a)"""
"""
def format_number(b):
     a=list(str(b))
     n=len(a)-3
     for i in range(n,0,-3):
          a.insert(i,",")
     print(*a,sep="")

format_number(45909049)
"""
"""
import matplotlib.pyplot as p

a=["25/12","26/12","27/12","28/12","29/12","30/12","31/12","01/01","02/01","03/01","04/01","05/01","06/01","07/01","08/01","09/01","10/01","11/01","12/01","13/01","14/01"]
b=[606,610,605,619,739,890,1155,1489,1594,1728,2731,4862,6983,8981,10978,12895,13990,15379,17934,20911]
c=[685,679,663,638,614,608,603,611,624,662,674,688,721,984,1525,1808,2547,3043,4039,6235]

p.plot(a,b,label="NEW CASES",color="red")
p.plot(a,c,label="DISCHARGE",color="green")
p.legend(["NEW CASES","DISCHARGE"],loc="upper left")
p.title("TAMILNADU'S CORONAVIRUS SCENARIO SINCE CHRISTMAS")
p.show()""""""
print("Switch Statement from Python 3.10")
def check(a):
     match a:
          case "green":
               return "python"
          case "blue":
               return "c++"

for i in range(2):
     n=input("Enter colour to match language :")
     print(check(n))"""
"""
a=int(input("Enter any number : "))
t=a
z=0
while a!=0:
     d=a%10
     z=z*10+d
     a//=10
if (z==t):
     print("Palindrome")
else:
     print("Not Palindrome")
"""
"""
a=input("Enter Player Name : ")

match a:
     case "Virat":
          print("Cricketer")
     case "Ronaldo":
          print("Footballer")
     case "Allu Arjun":
          print("Actor")
"""
"""
n=int(input())
h=list(map(int,input().split()))
k=[x for x in h if x>=0]

def check(h,k):
    if h==k:
        return True
    
def palin(n):
    m=""
    ni=str(n)
    for i in ni:
        m=m+i
    if ni=="1":
        return False
    if ni==m:
        return True
    else:
        return False

if check(h,k) and palin(n):
    print(True)
else:
    print(False)
"""
"""
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)
"""
"""
a="aacccbbazaabb"
b,c,d=a[0],1,[]
for i in a[1:]:
     if i in b:
          b+=i
          c+=1
     else:
          d.append(c)
          b,c=i,1
d.append(c)
print(*d,sep="\n")
"""
"""
a='welcome'
b,e="",0
for i in range(len(a)):
     if a[i] in "aeiou":
          s=e
          e=i
          for k in range(s,e):
               b+=a[i]
b+=a[e:]
print(b)
"""
"""
a="1222311"
b,c,d=a[0],1,[]
for i in range(1,len(a)):
     if a[i] in b:
          b+=a[i]
          c+=1
     else:
          d.append([a[i-1],c])
          b,c=a[i],1
d.append([a[len(a)-1],c])
for i in d:
     print((i[1],int(i[0])),end=" ")
"""
"""
s=input()
d,c={},[]
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
def second(c):
     return c[1]
for i in d.items():
    b=list(i)
    c.append(b)
print(d)
c.sort(reverse=True,key=second)
print(c)

for i in c[:3]:
     print(i[0],i[1])
print(min(c))
"""
"""
s=input().split()
d=[]
for i in range(int(s[1])):
    k = list(int(x) for x in input().split())
    d.append(k)
a=list(zip(*d))
print(a)
"""
"""
a=input()

if(len(a)==12):
    print("+91 "+a[2:])
elif(len(a)==11):
    print("+91 "+a[1:])
else:
    print("+91 "+a[:])
"""
"""
class student():
     def start(self):
          return self.x
p = student()
p.x="Divi"
print(p.start())

"""
"""
import re
f = open("D:\\text.txt")
t = f.read()
n = re.findall('[0-9]+',t)
s = sum([int(x) for x in n])
print(s)
f.close()
"""
"""
from itertools import *
l,mo=list(map(int,input().split()))
s=[]

for i in range(l):
    inp=list(map(int,input().split()))
    s.append(inp)
b=list(product(*s))
su=[]
for i in b:
     s=0
     for j in i:
          s+=j*j
     su.append(s)
print(max(su))
print(b)

for i in range(len(s)):
     a[i].pop(0)
b=list(product(*s))
su=[]
for i in b:
     s=0
     for j in i:
          s+=j*j
     su.append(s)
print(max(su))
print(b)
"""
"""
a=[]
ans=[]
for i in range(2):
    inp=input()
    a.append(inp)
b=a[0]
for i in a[1:]:
    for j in range(1,len(a[0])+1):
        b=b[:j]
        if b in i:
            ans.append(True)
        else:
            break
print(*ans)

"""
"""
a=["a","b","a","a","b"]
b=["a","c"]
c=[]
for i in b:
     co=1
     ans=[]
     for j in a:
          if i==j:
               ans.append(co)
          co+=1
     else:
          if ans==[]:
               c.append([-1])
          else:
               c.append(ans)
for i in c:
     print(*i)
"""
"""

a=reversed([4,2,1])
b=reversed([0,0,1])
c,d="",""
for i in a:
     c+=str(i)
for i in b:
     d+=str(i)
e=str(int(c)+int(d))

answer=[]
for i in e:
     answer.insert(0,int(i))
print(answer)

"""
"""
a=input().split()
average=0
c=0
for i in a:
     if "*" in i:
          r=i.split("*")
          average+=int(r[0])
     else:
          average+=int(i)
          c+=1
if c==0:
     c=1
     average=average/c
else:
     average=average/c
print(average)

"""
"""
#LONGEST PALINDROMIC SUBSTRING
a="abacgd"
an=[]
for i in range(len(a)):
     for j in range(len(a)):
          b=a[i:j+1]
          if b==b[::-1]:
               an.append(b)
l=len(an[0])
k=[]
for i in an:
     if len(i)>=l:
          k.append(i)
          l=len(i)
print(k[len(k)-1])"""
"""
a=[]
ans=[]
for i in range(2):
    inp=input()
    a.append(inp)
b=a[0]
for i in a[1:]:
    for j in range(1,len(a[0])+1):
        b=b[:j]
        if b in i:
            ans.append(True)
        else:
            break
print(*ans)

"""
"""
#MEDIAN Of the Array of data
a=[int(x) for x in input().split()]
if (len(a)%2!=0):
     print(a[len(a)//2])
else:
     print((a[len(a)//2]+a[len(a)//2-1])/2)
"""
"""
a=input().strip()
k=len(a)
for i in range(len(a)):
    print("*"*k)
"""
"""
god={"f":"FRIENDSHIP","l":"LOVE","a":"AFFECTION","m":"MARRIAGE","e":"ENEMY","s":"SIBLING"}
a=list(input())
b=list(input())
for i in a[:]:
    if i in b:
        a.remove(i)
        b.remove(i)
n=len(a)+len(b)
fate=list("flames")
for i in range(6,1,-1):
    fate.pop((n%i)-1)
print(god["".join(fate)])
"""
"""
import string
s="race a car"
su=""
for i in s.strip():
    if (i.isalnum()==True):
        su=i.lower()+su
if su!=su[::-1]:
    print("false")
else:
    print("true")
"""
"""
god={"f":"FRIENDSHIP","l":"LOVE","a":"AFFECTION","m":"MARRIAGE","e":"ENEMY","s":"SIBLING"}
fate=list("flames")
a,b=list(input()),list(input())
for i in a[:]:
    if i in b:
        a.remove(i)
        b.remove(i)
n=len(a)+len(b)
for i in range(6,1,-1):
    fate.pop((n%i)-1)
print(f"It's a {god[''.join(fate)]}")
"""
"""
a=input()
ind=0
b=[]
for i in range(len(a)):
    sam=""
    for j in range(i+1):
        try:
            sam=a[ind]+sam
            ind+=1
        except:
            continue
    
    if sam!="":
        b.append(sam)
            
for i in range(len(b)):
    print(b[i].rjust(i+1,"*"))
"""
"""
a=input()
ind=0
for i in range(len(a)):
    sam=""
    for j in range(i+1):
        try:
            sam=a[ind]+sam
            ind+=1
        except:
            continue
    if sam!="":
        print(" ".join(list(sam.rjust(i+1,"*"))))

"""
"""
god={"f":"FRIENDSHIP","l":"LOVE","a":"AFFECTION","m":"MARRIAGE","e":"ENEMY","s":"SIBLING"}
fate=list("flames")
a,b=list(input()),list(input())
for i in a[:]:
    if i in b:
        a.remove(i)
        b.remove(i)
n=len(a)+len(b)
for i in range(6,1,-1):
    fate.pop((n%i)-1)
print(f"Relationship between you two will end up as a {god[''.join(fate)]}")
"""
"""
a=input().strip()
for i in range(len(a)//2):
    print(a[i]+((len(a)//2-1)-i)*"*"+a[len(a)-i-1])
print(a[len(a)//2])
for i in range((len(a)//2)-1,-1,-1):
    print(a[i]+((len(a)//2-1)-i)*"*"+a[len(a)-i-1])
"""
a=input("Enter Player Name : ")

match a:
     case "Virat":
          print("Cricketer")
     case "Ronaldo":
          print("Footballer")
     case "Krishnapriya":
          print("Programmer")
     case _:
          print("404 NOT FOUND")







           





