class Rectangle:
    def __init__(self, lenght,  width):
        self.length = lenght
        self.width = width
        
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.width * self.length)

    def print_info(self):
        print(f"({self.length}, {self.width}, {self.area()}, {self.perimeter()})")


r = Rectangle(4, 5)
print(r.area())
print(r.perimeter())
r.print_info()