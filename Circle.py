from math import pi

class Circle:


    def __init__(self, radius):
        """ Loo klass koos raadiusega """
        # print('Object created')
        self.radius = radius

    def radius(self):
        # print('Return radious')
        # ei ole vaja seda meetotit
        return self.radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        # pi * pow(self.radius, 2)  # import pow  , 2 on see mitmendasse astmesse võtad
        return pi * self.radius ** 2

    def perimeter(self):
        return  2 * pi * self.radius

    def show_circle_data(self):
        print('Radius:', self.radius)
        print('Diameter:', self.get_diameter())
        print('Area:', self.get_area())
        print('Perimeter:', self.get_perimeter())
