#DAY 1
a=int(input())
b=""
for i in range(a):
     a=[i for i in input().split()]
     for _ in a:
          b+=chr(int(_,16))
     b+="\n"
print(b)
