from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, last_name, id):
        self.name = name
        self.last_name = last_name
        self.id = id

    @abstractmethod
    def calc_salary(self):
        pass
    @abstractmethod
    def describe_role(self):
        pass
    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.name} {self.last_name}"

class Vet(Employee):
    def __init__(self, name, last_name, id, role):
        super().__init__(name, last_name, id)
        self.role = role
        self.base_salary = 0
        self.bonus = 0
        self.surgery_amount = 0
    
    def describe_role(self):
        if self.role == "veterinarian":
            self.base_salary = 1000
            self.bonus = 100
        elif self.role == "auxiliar":
            self.base_salary = 1000
            self.bonus = 50
        elif self.role == "manager":
            self.base_salary = 2000
    def surgeries(self, amount):
        self.surgery_amount += amount
        print(f"The {self.role}, {self.name} {self.last_name} has done {self.surgery_amount} surgeries.")
    def calc_salary(self):
        salary = self.base_salary + (self.surgery_amount*self.bonus)
        print(f"The base salary of the {self.role}, {self.name} {self.last_name}, is {self.base_salary}, alongside {self.surgery_amount*self.bonus} from their {self.surgery_amount} surgeries. Total Salary of {salary}")
        return salary

class Auxiliar(Employee):
    def __init__(self, name, last_name, id, role):
        super().__init__(name, last_name, id)
        self.role = role
        self.base_salary = 0
        self.bonus = 0
        self.shifts = 0
    
    def describe_role(self):
        if self.role == "veterinarian":
            self.base_salary = 1000
            self.bonus = 100
        elif self.role == "auxiliar":
            self.base_salary = 1000
            self.bonus = 50
        elif self.role == "manager":
            self.base_salary = 2000
    def shifts_amount(self, amount):
        self.shifts += amount
        print(f"The {self.role}, {self.name} {self.last_name} has done {self.shifts} shifts.")
    def calc_salary(self):
        salary = self.base_salary + (self.shifts*self.bonus)
        print(f"The base salary of the {self.role}, {self.name} {self.last_name}, is {self.base_salary}, alongside {self.shifts*self.bonus} from their {self.shifts} shifts. Total Salary of {salary}")
        return salary

class Manager(Employee):
    def __init__(self, name, last_name, id, role):
        super().__init__(name, last_name, id)
        self.role = role
        self.base_salary = 0
        self.bonus = 0
        self.department = ""
    
    def describe_role(self):
        if self.role == "veterinarian":
            self.base_salary = 1000
            self.bonus = 100
        elif self.role == "auxiliar":
            self.base_salary = 1000
            self.bonus = 50
        elif self.role == "manager":
            self.base_salary = 2000
    def department_name(self, department):
        self.department = department
        print(f"The {self.role}, {self.name} {self.last_name} is in charge of the {self.department} department.")
    def calc_salary(self):
        print(f"The base salary of the {self.role}, {self.name} {self.last_name}, is {self.base_salary}.")
        return self.base_salary

mng1 = Manager("Pedro", "Sanchez", "M78", "manager")
vet1 = Vet("Marco", "Perez", "V23", "veterinarian")
aux1 = Auxiliar("Nicolas", "Moros", "A13", "auxiliar")

employee_list = [mng1,vet1,aux1]
vet1.surgeries(10)
aux1.shifts_amount(5)
print("-------------------------------------------")

def employee_count(employees):
    total_founds = 0
    for emp in employees:
        emp.describe_role()
        monthly_salary = emp.calc_salary()
        yearly_salary = monthly_salary*12
        total_founds += yearly_salary
        print(f"The {emp.role}, {emp.name} {emp.last_name}, has a {yearly_salary:,.2f} yearly salary.")
        print("-------------------------------------------")
    print(f"The total cost of employees is {total_founds:,.2f}")

employee_count(employee_list)