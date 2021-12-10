x=int(input("x"))
y=int(input("y"))
r=[]
for xx in range(x):
    l=[]
    for yy in range(y):
        l.append(xx*yy)
    r.append(l)
print(r)