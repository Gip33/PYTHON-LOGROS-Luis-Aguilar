from abc import ABC, abstractmethod
import math

"""
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class Creditcard(PaymentMethod):
    def __init__(self, number, cvv):
        self.number = number
        self.cvv = cvv
        self.balance = 0

    def process_payment(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"El pago fue realizado con exito, el saldo restante es de {self.balance}.")
        else:
            print(f"La tarjeta no tiene fondos suficientes.")


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
        self.balance = 0

    def process_payment(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"El pago fue realizado con exito, el saldo restante es de {self.balance}.")
        else:
            print(f"Tu cuenta de PayPal no tiene fondos suficientes.")

creditcard = Creditcard(33272644,147)
creditcard.balance = 5000
paypal = PayPal("gip33.leap@gmail.com")
paypal.balance = 1000

def pay(method,amount):
    if method == "creditcard":
        creditcard.process_payment(amount)        
    elif method == "paypal":
        paypal.process_payment(amount)

pay("creditcard",500)
pay("paypal",400)
"""
"""
class Shape(ABC):
    @abstractmethod
    def calc_area():
        pass
    @abstractmethod
    def calc_perimeter():
        pass

class Rectangle(Shape):
    def __init__(self, height, lenght):
        self.height = height
        self.lenght = lenght
    def calc_area(self):
        area = self.height*self.lenght
        return area
    def calc_perimeter(self):
        perimeter = self.height*self.lenght
        return perimeter
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calc_area(self):
        area = math.pi * self.radius**2
        return area
    def calc_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


rectangle1 = Rectangle(5,5)
circle1 = Circle(5)
rectangle2 = Rectangle(8,8)

shapes = [rectangle1,circle1,rectangle2]

def calc(object_list):
    for objects in object_list:
        area = objects.calc_area()
        perimeter = objects.calc_perimeter()
        print(f"El area del objeto es {area:,.2f} y su perimetro es {perimeter:,.2f}")

calc(shapes)
"""
"""
class Employees(ABC):
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
    @abstractmethod
    def calc_salary(self):
        pass
    def greet(self):
        print(f"Hola, mi nombre es {self.name} {self.last_name}")

class RegularEmployee(Employees):
    def __init__(self, name, last_name, monthly_salary):
        super().__init__(name, last_name)
        self._monthly_salary = monthly_salary
    
    def calc_salary(self):
        return self._monthly_salary

class Freelancer(Employees):
    def __init__(self, name, last_name, hours, payment):
        super().__init__(name, last_name)
        self._hours = hours
        self._payment = payment
    
    def calc_salary(self):
        return self._hours*self._payment

regualar_employee = RegularEmployee("Samuel","Martinez",1500)
freelancer = Freelancer("Juan","Finol",50,100)

employees = [regualar_employee,freelancer]

class Management:
    def __init__(self,employee_list):
        self.employee_list = employee_list
    
    def calc_all_salaries(self):
        total_salary = 0
        for emp in self.employee_list:
            total_salary += emp.calc_salary()
            print(f"El empleado {emp.name} gana {emp.calc_salary()}")
        return total_salary

management = Management(employees)
    
print(management.calc_all_salaries())
"""