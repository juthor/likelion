class Rectangle:
    width=0
    height=0
    color=""

    def __init__(self, width, height):
        self.width=width
        self.height=height

    def calc_area(self):
        area=self.width*self.height
        return area

    @staticmethod
    def is_square(rect_width, rect_height):
        return rect_width==rect_height

rect1=Rectangle(40, 42)
print(rect1.width, rect1.height)
print(rect1.width)
print(rect1.height)
print(rect1.calc_area())

rect2=Rectangle(23, 53)
rect3=Rectangle(12, 35)
rect1.color="blue"
rect2.color="pink"
rect3.color="skyblue"

print(rect1.color, rect2.color, rect3.color)

squar=Rectangle.is_square(34, 40)
print(square)
