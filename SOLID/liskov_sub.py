class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        print("Area of height {} and width {} is {}".
              format(str(self.height), str(self.width), str(self.height * self.width)))

class Square(Rectangle):
    def __init__(self, width):
        super(Square, self).__init__(height=width, width=width)

if __name__ == '__main__':
    s = Square(10)
    s.calculate_area()
    print("Completed")