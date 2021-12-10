import string

abc=string.ascii_lowercase
ABC=string.ascii_uppercase

s=str(input())

u=0
l=0
for k in s:
    if k in abc:
        l=l+1
    elif k in ABC:
        u=u+1
print("UPPER CASE ", u,"LOWER CASE ", l)