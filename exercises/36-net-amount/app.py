s=str(input())
t=0
l=s.split(" ")
for k in range(len(l)):
    if l[k]=="D":
        t=t+int(l[k+1])
    elif l[k]=="W":
        t=t-int(l[k+1])
print(t)