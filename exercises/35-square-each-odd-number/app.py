s=str(input())
ln=s.split(",")
for k in ln:
    if int(k)%2==0:
        ln.remove(k)
print(",".join(ln))