def evenOdd(n):
    if n%2==0:
        return True
    else:
        return False
    
a=int(input("Enter a number:"))
r=evenOdd(a)
if r==True:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd  number.")