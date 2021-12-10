s=str(input())
l=s.split(" ")
r=[]
for k in l:
    x=tuple(k.split(","))
    r.append(x)
    
r.sort()
print(r)