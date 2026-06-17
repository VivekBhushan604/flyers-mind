def simpleInterest(p,r,t):
    return (p*r*t)/100.0

p=float(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time(years):"))
print(f"The simple interest on {p} on {r}% interest rate for {t} years is {simpleInterest(p,r,t)}.")