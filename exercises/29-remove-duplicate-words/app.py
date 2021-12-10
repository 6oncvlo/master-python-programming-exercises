s=str(input())
l=s.split(" ")
l.sort()
ln=list(set(l))
ln.sort()
print(ln)
print(" ".join(ln))

