class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name:{self.name},Age:{self.age}")

s1 =  Student("Chandru",23)

s1.display()

#===================================================================================================

# with constructor(__init__)

class Employee:

    def __init__(self,name,aadhaar):
        self.name = name
        self.aadhaar = aadhaar


    def enter_office(self):
        print(f"{self.name} enters using aadhaar {self.aadhaar}.")

    def open_bank_account(self):
        print(f"Bank account opened for {self.name} with aadhaar {self.aadhaar}.")


emp1 = Employee("Kathiravan","1234-4567-8912")

emp1.enter_office()

emp1.open_bank_account()

# =============================================================================================
# without constructor


class MathTools:

    def square(self,n):
        return n * n

    def cube(self,n):
        return n * n * n

tool = MathTools()

print(tool.cube(7))
print(tool.square(7))

# ===============================================================================================
# example -1

class dad:

    def house(self):
        print("I am from dad class")

class son(dad):

    def factory(self):
        print("I have one factory")

s =son()

s.house()
s.factory()


# example -2

class app1:

    def v1(self):
        print("Some logic implemented")

class app1_1(app1):

    def v1_1(self):
        print("New logic defined")

version = app1_1()

version.v1()
version.v1_1()

# example - 3:

class dad:

    def house(self):
        print("RED")

    def cars(self):
        print("BMW")

class son(dad):
    def factory(self):
        print("Briyani")

    def house(self):
        print("Lavender")

    def cars(self):
        print("RollsRoyce")

sn = son()

sn.factory()
sn.house()
sn.cars()

# =======================================================================================

# MULTI LEVEL INHERITANCE

class mayavan:

    def cars(self):
        print("BMW")

    def land(self):
        print("4 acres")

    def cash(self):
        print("8 crores")

class deivanayagan(mayavan):

    def cars1(self):
        print("RollsRoyce, BMW, Bugatti")

    def land1(self):
        print("1 ground")

    def cash1(self):
        print("4 crores")

class Mother:   # Multiple level Inheritance

    def Building(self):
        print("Business")

class chandru(deivanayagan,Mother):
    def AIcompany(self):
        print("product based company")

    def AiStartup(self):
        print("startup company")

class kathiravan(deivanayagan): #hierarchy - seperate object
    def Ecommerce(self):
        print("Service based company")

    def digital_marketing(self):
        print("BlackBox")

son = chandru()

son.cash()
son.land()
son.cars()
son.cars1()
son.cash1()
son.land1()

# =============================================================================================


