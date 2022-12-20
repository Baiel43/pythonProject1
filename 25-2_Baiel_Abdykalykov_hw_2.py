class Figure:
    unit = 'см'

    def __init__(self, perimeter=0):
        self.__perimeter = perimeter

    def calculate_area(self):
        pass

    def info(self):
        raise NotImplementedError('Method info must be implement')


class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        if not isinstance(radius, int) or radius <= 0:
            raise ValueError('Age attribute must be positive number')
        else:
            self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius ** 2

    def info(self):
        return f'Circle radius: {self.__radius}{self.unit} area: {self.calculate_area()}{self.unit}'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        if not isinstance(side_a, int) or side_a <= 0:
            raise ValueError('Age attribute must be positive number')
        else:
            self.__side_a = side_a
            if not isinstance(side_b, int) or side_b <= 0:
                raise ValueError('Age attribute must be positive number')
            else:
                self.__side_b = side_b

    def calculate_area(self):
        return self.__side_a * self.__side_b * 0.5

    def info(self):
        return f'RightTriangle side_a: {self.__side_a}{self.unit} side_b: {self.__side_b}{self.unit} ' \
               f'area: {self.calculate_area()}{self.unit}'


Circle1 = Circle(2)
Circle2 = Circle(5)
RightTriangle1 = RightTriangle(3, 4)
RightTriangle2 = RightTriangle(5, 8)
RightTriangle3 = RightTriangle(5, 7)

Figure_list = [Circle1, Circle2, RightTriangle1, RightTriangle2, RightTriangle3]
for i in Figure_list:
    print(i.info())