principal=input("Enter principal: ")
rate=input("Enter rate of interest: ")
time=input("Enter time: ")
principal=int(principal)
rate=int(rate)
time=int(time)
simpleInterest=(principal*rate*time)/100
print(f"Simple Interest: {simpleInterest}")