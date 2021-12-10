#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    return (n*d+(c*n)//100,(c*n)%100)
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(1,99,2))
