class Animal:
    def bark(self):
        return f'Animals sound'

class Dog(Animal):
    def bark(self):
        return f'bow bow'

class Cat(Animal):
    def bark(self):
        return f'meow meow'

animals =[Dog(),Cat(),Animal()]
for animal in animals:
    print(animal.bark(),end='\n')