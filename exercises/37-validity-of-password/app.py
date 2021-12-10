import string

abc=string.ascii_lowercase
ABC=string.ascii_uppercase
num="1234567890"
esp="$#@"

s=str(input())
l=s.split(",")
r=[]

for k in l:
    if len(k)>5 and len(k)<13:
        a1=0
        A1=0
        n1=0
        e1=0
        for j in k:
            if j in abc:
                a1=a1+1
            if j in ABC:
                A1=A1+1
            
            if j in num:
                n1=n1+1
            if j in esp:
                e1=e1+1
        if a1*A1*n1*e1>1:
            r.append(k)

print(",".join(r))