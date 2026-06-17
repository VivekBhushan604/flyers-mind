pie=3.14
def areaCircle(r):
    return pie*r*r

r=int(input("Enter radius of circle:"))
area=areaCircle(r)
print(f"Area of a circle with {r} radius is {area}.")