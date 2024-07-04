from typing import Any
from _15_ClassStructure import Car

class Garage:
    def __init__(self) -> None:
        self.__cars = []

    def addCar(self, car):
        self.__cars.append(car)

    def rmCar(self, car):
        self.__cars.remove(car)

    def display(self):
        cars = [str(car) for car in self.__cars]
        return cars
    
    def __getitem__(self, index):
        return self.__cars[index]
    
    def __call__(self, idx = None) -> Any:
        if idx == None:
            return [car.make  for car in self.__cars]
        else:
            return self.__cars[idx].make

class cmpCarYear:
    def __call__(self, first: Car, second: Car):
        if first.year > second.year:
            return True
        return False

class cmpCarMake:
    def __call__(self, first: Car, second: Car):
        if first.make > second.make:
            return True
        return False

'''
Sort(gr, cmpCarYear)
Sort(gr, cmpCarMake)

cmpCarYear(c1, c2)
'''

gr = Garage()
car1 = Car("Honda", "Accord", 2024, "Blue")
car2 = Car("Toyota", "Camry", 2021, "Red")
gr.addCar(car1)
gr.addCar(car2)


print(gr.display())

print(gr[1])        # Overload the subscriptoperator  -->  __getitem__
# gr[1] = Car("Mazda", "Miata", 2020, "Yellow")# To set  --> __setitem__
# del gr[0]                                   # To delete--> __delitem__


print(gr()) # ('Honda', 'Toyota')
print(gr(0)) # ('Honda', 'Toyota')
print(gr(1)) # ('Honda', 'Toyota')