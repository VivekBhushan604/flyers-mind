def factorial(n):
    fac=1
    for i in range(2,n+1):
        fac*=i
    return fac

a=int(input("Enter a number:"))
fac=factorial(a)
print(f"Factorial of {a} is {fac}")