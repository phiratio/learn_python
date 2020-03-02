## animal is-a object


class Animal(object):
    @staticmethod
    def speak():
        print('balo')


# ??
class Dog(Animal):
    """very dog!"""
    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

    @staticmethod
    def sayhi(name):
        print(name)


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        super(Employee, self).sayhi(name)
        self.salary = salary


class Fish(object):
    pass


class Salomon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog('rover')
stan = Cat('stan')
stan.speak()
mary = Person('mary')
mary.pet = stan
frank = Employee('frank', 1234)
frank.pet = rover
flipper = Fish()
crouse = Salomon()
harry = Halibut()
