a=input("Enter a binary number: ")
b=input("Enter another binary number: ")
a=int(a,2)
b=int(b,2)
c=a+b
c=bin(c)[2:]
print("The sum of two binary numbers are: ", c)
