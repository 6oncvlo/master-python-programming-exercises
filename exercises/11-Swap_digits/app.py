#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  return (num%10)*10+num//10
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(79))

