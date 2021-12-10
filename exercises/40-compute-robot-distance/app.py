from math import *

s=str(input())
l=s.split(" ")
v=0
h=0
for k in range(len(l)):
    if l[k]=="UP":
        v=v+int(l[k+1])
    elif l[k]=="DOWN":
        v=v-int(l[k+1])
    if l[k]=="RIGHT":
        h=h+int(l[k+1])
    if l[k]=="LEFT":
        h=h-int(l[k+1])
print(round(sqrt(v**2+h**2)))