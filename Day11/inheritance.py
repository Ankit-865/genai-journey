class Animal:
    def speak(self):
        print("I can speak!")
class Dog(Animal):
    def bark(self):
        print("Woof!")
dog = Dog()
dog.speak()
dog.bark()