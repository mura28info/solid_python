"""
The principle was introduced by Barbara Liskov in 1987 and according to this principle “Derived or
child classes must be substitutable for their base or parent classes“. This principle ensures that
any class that is the child of a parent class should be usable in place of its parent without any
unexpected behavior.You can understand it in a way that a farmer’s son should inherit farming skills
from his father and should be able to replace his father if needed. If the son wants to become a farmer
then he can replace his father but if he wants to become a cricketer then definitely the son
can’t replace his father even though they both belong to the same family hierarchy.
One of the classic examples of this principle is a rectangle having four sides.
A rectangle’s height can be any value and width can be any value.
A square is a rectangle with equal width and height.
So we can say that we can extend the properties of the rectangle class into square class.
In order to do that you need to swap the child (square)
class with parent (rectangle) class to fit the definition of a square having four equal
sides but a derived class does not affect the behavior of the parent class
so if you will do that it will violate the Liskov Substitution Principle.
Refer: https://www.geeksforgeeks.org/solid-principle-in-programming-understand-with-real-life-examples/
"""
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
