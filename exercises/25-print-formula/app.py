c=50
h=30
ln=str(input())
lnn=ln.split(",")
for k in range(len(lnn)):
    lnn[k]=str(round(2*c*float(lnn[k])/h))
w=",".join(lnn)
print(w)