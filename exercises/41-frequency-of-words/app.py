s=str(input())
l=s.split(" ")
r=[]
#print(l)
for k in l:
    if k in r:
        r[r.index(k)+1]=r[r.index(k)+1]+1
    else:
        r.append(k)
        r.append(1)
#print(r)
rr=[]
for k in range(len(r)//2):
    rr.append(r[2*k]+":"+str(r[2*k+1]))
rr.sort()
#print(rr)
print(" ".join(rr))