##Animal is-a object(yes, sort of confusing ) look at the extra credit
class Animal(object):
    pass

##Dog is-a object of Animal
class Dog(Animal):
    def __init__(self, name):
        ##??
        self.name = name
        
##Cat is-a object of Animal
class Cat(Animal):
    def __init__(self, name):
        ##??
        self.name = name
        
##Person is an object
class Person(object):
    def __init__(self, name, salaty):
        ##??hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##??
        self.salary =salary
        
##Fish is-a object
class Fish(object):
    pass

##Salmon is-a object of Fish
class Salmon(Fish):
    pass

##Halibut is-a object of Fish 
class Halibut(Fish):
    pass

##??rover is-a Dog
rover = Dog("Rover")

##??
satan = Cat("Satan")

##??
mary = Person("Mary")

##??
mary.pet = satan

##??
frank = Employee("Frank", 120000)

##??
frank.pet = rover

##??
flipper = Fish()

##??
crouse = Salmon()

##??
harry = Halibut()