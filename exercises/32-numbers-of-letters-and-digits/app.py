import string

abc=string.ascii_lowercase
ABC=string.ascii_uppercase
num="1234567890"

s=str(input())

d=0
l=0
for k in s:
    if k in num:
        d=d+1
    elif k in abc or k in ABC:
        l=l+1
print("LETTERS ", l, "DIGITS ", d)