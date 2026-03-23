#1. Write a program that takes two integers, computes their sum, difference, product, and division, checks if they’re even/odd, and converts one to a float.
int1=int(input("Enter the first integer: "))
int2=int(input("Enter the second integer: "))
sum=int1+int2
dif=int1-int2
prod=int1*int2
div=int1/int2
if int1%2==0:
    print(int1,"is even")
else:
    print(int1,"is odd")
if int2%2==0:
    print(int2,"is even")
else:
    print(int2,"is odd")
float_int1=float(int1)
