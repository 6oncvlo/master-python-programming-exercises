class jj:

    def getString(self):
        s=str(input())
        return s
    
    def printString(self,k):
        j=k.upper()
        return j

test1=jj()
w=test1.getString()
k=test1.printString(w)
print(k)