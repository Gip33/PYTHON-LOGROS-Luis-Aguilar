class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hola! Mi nombre es {self.name} y tengo {self.age} años!")
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def give_class(self):
        print(f"El profesor {self.name} esta dando la clase de {self.subject}")

teacher1 = Teacher("Marco",45, "Ingles")
person1 = Person("Pedro", 50)
person1.greeting()
print("---------------")
teacher1.greeting()
teacher1.give_class()