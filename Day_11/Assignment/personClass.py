class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def profile(self):
        print("\nPerson Profile")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")


person1 = Person("Vivek", 22, "Dehradun")

person1.profile()