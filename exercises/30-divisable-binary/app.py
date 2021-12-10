s=str(input())
ln=s.split(",")
r=[]
for k in ln:
    
    if (8*int(k[0])+4*int(k[1])+2*int(k[2])+int(k[3]))%5==0:
        r.append(k)
print(",".join(r))