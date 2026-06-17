def palindrome(s):
    size=len(s)
    l=int(size/2)
    size-=1
    for i in range (0,l):
        if s[i] != s[size-i]:
            return False
    return True
    
a=input("Enter a string:")
fac=palindrome(a)
if fac == True :
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")

