class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'{self.name}, Hello')

person1 =Person("John",90)
person1.talk()