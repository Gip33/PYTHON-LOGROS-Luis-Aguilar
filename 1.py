
class Component:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self,new_price):
        self.price = new_price
    def add_stock(self,amount):
        self.stock += amount
    def sell(self,amount):
        if amount > self.stock:
            print("La cantidad del pedido supera la cantidad en inventario")
            print(f"Cantidd en inventario {self.stock}")
        else:
            self.stock -= amount
    def show_info(self):
        print(f"Nombre: {self.name}")
        print(f"Precio: {self.price}")
        print(f"Stock : {self.stock}")

gpu = Component("ryzen", 500, 10)
gpu.show_info()
gpu.update_price(550)
gpu.show_info()
gpu.add_stock(10)
gpu.show_info()
gpu.sell(10)
gpu.show_info
gpu.sell(50)


class Cafe:
    def __init__(self, max_amount,water,grounded_cofeebeans):
        self.max_amount = max_amount
        self.actual_amount = water
        self.grounded_coffeebeans = grounded_cofeebeans
    
    def fill(self, water):
        if water > self.max_amount:
            self.actual_amount = self.max_amount
            print("Lleno la taza hasta el tope")
        else:
            self.actual_amount += water
            print(f"Añadio {water}ml de agua a la taza, ahora la taza tiene {self.actual_amount}ml de agua")
    def add_cofee(self):
        self.grounded_coffeebeans = True
        print("Añadio cafe al agua")
    def serve(self):
        if self.actual_amount >= 250 and self.grounded_coffeebeans == True:
            self.actual_amount -= 250
            self.grounded_coffeebeans = False
            print("Se sirvio el cafe")
            print(f"Qudan {self.actual_amount}ml de agua y ya no hay cafe")
        elif self.actual_amount < 250:
            print("No hay suficiente agua")
        elif self.grounded_coffeebeans == False:
            print("No hay cafe")
    def show(self):
        print(f"Cantidad Maxima: {self.max_amount}")
        print(f"Cantidad Actual: {self.actual_amount}")
        print(f"Tiene Cafe?: {self.grounded_coffeebeans}")

Coffee1 = Cafe(1000,0,False)
Coffee1.fill(300)
Coffee1.show()
Coffee1.add_cofee()
Coffee1.show()
Coffee1.serve()
Coffee1.serve()