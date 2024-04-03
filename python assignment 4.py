class person:
    def __init__(self,name,age,gender):
        self.name= name
        self.age= age
        self.gender= gender
    def introduce(self):
        print(f"my name is {self.name}. I am {self.age} years old and I am {self.gender}.")
person1 = person("Alice", 25,"Female")
person1.introduce()