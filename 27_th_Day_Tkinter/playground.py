# *****************************
# *args -- unlimited arguments or unlimited positional arguments
# *****************************
def add(*args):
    print(type(args))
    result = 0
    for n in args:
        result = result + n
    return result


print(add(1, 2, 3, 4, 5, 6))


# *****************************
# **kwargs -- Many Keyword arguments or Optional Keyword arguments
# *****************************

def calculate(n, **kwargs):
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)



class Car:
    def __init__(self,**kwargs):
        self.make=kwargs.get("make")
        self.model = kwargs["model"]

my_car=Car(make="Nissan",model="GT-R")
print(my_car.make)