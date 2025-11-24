from abc import ABC, abstractmethod

class VetEmployee(ABC):
    def __init__(self,name,lastname,id):
        self
    @abstractmethod
    def calc_salary(self):
        pass
    @abstractmethod
    def employee_rol(self):
        pass

class Vet(VetEmployee):
    def __init__(self, name, lastname, id, monthly_surgeries, rol):
        super().__init__(name, lastname, id)
        self.monthly_surgeries = monthly_surgeries
        self.rol = rol
        self.salary
        self.bonus

    def employee_rol(self,rol):
        if rol == "vet":
            self.salary = 1000
            self.bonus = 100
        elif rol == "aux":
            self.salary = 1000
            self.bonus = 100
        elif rol == "supervisor":
            self.salary = 2000
    def calc_salary(self):
        self.salary += (self.bonus*self.monthly_surgeries)
    

class Auxiliar(VetEmployee):
    def __init__(self, name, lastname, id, shifts, rol):
        super().__init__(name, lastname, id)
        self.shifts = shifts
        self.rol = rol
        self.salary
        self.bonus

    def employee_rol(self,rol):
        if rol == "vet":
            self.salary = 1000
            self.bonus = 100
        elif rol == "aux":
            self.salary = 1000
            self.bonus = 100
        elif rol == "supervisor":
            self.salary = 2000
    def calc_salary(self):
        self.salary += (self.bonus*self.shifts)

class Supervisor(VetEmployee):
    def __init__(self, name, lastname, id, department, rol):
        super().__init__(name, lastname, id)
        self.shifts = shifts
        self.rol = rol
        self.salary
        self.bonus

    def employee_rol(self,rol):
        if rol == "vet":
            self.salary = 1000
        elif rol == "aux":
            self.salary = 1000
        elif rol == "supervisor":
            self.salary = 2000
    def calc_salary(self):
        pass