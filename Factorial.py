a=int(input("Enter a number: "))
def factorial(a):
    if a <= 1:
        return 1
    else:
        return a*factorial(a-1)
result=a*factorial(a-1)
print("Factorial of",a,"is",result)
factorial(a)
