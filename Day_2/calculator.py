a=float(input("Enter operand 1: "))
o=input("Enter operator(+,-,*,/):")
b=float(input("Enter operand 2: "))
if(o =='+'):
    result = a+b
elif(o =='-'):
    result = a-b
elif(o =='*'):
    result = a*b
elif(o =='/'):
    if(b==0):
        result="Undefined"
    else:
        result = a/b
else:
    print("Invalid Operator")
    exit()

print(f"\n{a} {o} {b} = {result}")