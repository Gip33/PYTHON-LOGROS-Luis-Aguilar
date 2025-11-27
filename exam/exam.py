from abc import ABC, abstractmethod
import math
#FirstBatch
"""
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available= True
    
    def lend(self):
        self.available = False
        print("Prestaste el libro")
    
    def give_back(self):
        self.available = True
        print("Te devolvieron el libro")

class Bookshelf:
    def __init__(self):
        self.booklist = []
    
    def add_book(self,book):

        book_info = {
            "title":book.title,
            "author":book.author,
            "avb":book.available
        }
        self.booklist.append(book_info)
        print(f"Se añadio el libro {book_info["title"]}")
    
    def search(self,book):
        for i in self.booklist:
            print(i)
            if book == i["title"] and i["avb"] == True:
                return f"El libro {i["title"]} fue encontrado y esta disponible"
            elif book == i["title"] and i["avb"] == False:
                return f"El libro {i["title"]} fue encontrado pero no esta disponible"
        print("El libro no fue encontrado")


book = Book("o","o",)
bookshelf = Bookshelf()

book.lend()
book.give_back()

bookshelf.add_book(book)
print(bookshelf.search("o"))


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
#SecondBatch

from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
print(formatted_date)