'''
class BaseType:
    pass

def separator():
    return "-"*40

class MyClass(BaseType):
    def __init__(self) -> None:
        super().__init__()

    def SomeMethod(self):
        pass
'''

class Car:
    carCount = 0

    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.serial = self.generateSerial(self.make, self.model, self.year)
        Car.carCount += 1


    def start(self):
        Car.getCarCount()           # <-- Car::getCarCount
        self.getCarCount()          # <-- self.__class__.getCarCount
        print(f"Starting the {self.model}...")

    @classmethod
    def getCarCount(cls):
        print(f"Counting {cls.__name__} objects...{cls.carCount}")

    @staticmethod
    def generateSerial(make, model, year):
        from random import randint
        return str(randint(1, 100)) + "_" + make + "_" + model +"_" + str(year)

    
    def __str__(self) -> str:
        return f"[{self.make}, {self.model}, {self.year}, {self.color}, {self.serial}]"
    
    def __repr__(self) -> str:
        return f"[{self.__class__.carCount}] -> {self.__str__()}"
    

class GearedCar(Car):
    carCount = 0
    def __init__(self, make, model, year, color, gearCount) -> None:
        self.gearCount = gearCount
        GearedCar.carCount += 1
        # print(super())
        super().__init__(make, model, year, color)

    @classmethod
    def getCarCount(cls):
        print(f"Counting {cls.__name__} objects...{cls.carCount}")
        

Car.getCarCount()
car1 = Car("Honda", "Accord", 2024, "Blue")
car1.start()
car1.getCarCount()
print(car1.__class__)
print(car1.__class__.__name__)
print(car1)

Car.getCarCount()

print("-"*40)
gc1 = GearedCar("Toyota", "Camry", 2021, "Red", 5)
gc1.getCarCount()
GearedCar.getCarCount()
gc1.start()
print(gc1)
print(repr(car1))
print(str(gc1))
print(repr(gc1))
Car.y = 100
print(Car.y)


## Further study
# print("Bases -->", GearedCar.__bases__)
# print("MRO -->", GearedCar.__mro__)
# print("MRO -->", Car.__mro__)
# __slots__= []
# print(car1.__dict__)
# car1.z = 200
# print(car1.z)
# print(car1.__dict__)
