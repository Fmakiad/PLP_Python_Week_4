class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am identified as {self.gender}.")


person1 = Person("Francis Lungu", 24, "Male")


person1.introduce()
