a=input("Enter a: ")
b=input("Enter b: ")
a=int(a)
b=int(b)
print("Before Swap:")
print(f"A:{a} ,B:{b}")

a=a+b
b=a-b
a=a-b

print("After Swap:")
print(f"A:{a} ,B:{b}")

