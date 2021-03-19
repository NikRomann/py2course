class Calculator:
    def add(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    def minus(self, x, y):
        self.x = x
        self.y = y
        return self.x - self.y

    def divide(self, x, y):
        self.x = x
        self.y = y

        if y == 0:
            return "You can't divide by zero!"
        else:
            return self.x / self.y

    def multiply(self, x, y):
        self.x = x
        self.y = y
        return self.x * self.y