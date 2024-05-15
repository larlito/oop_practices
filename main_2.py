#1
# coding=utf-8
class Patient:
    def __init__(self,full_name: str, age: int, disease: str):
        self.full_name = full_name
        self.age = age
        self.disease = disease

    @staticmethod
    def make_appointment(mounth: str,day: int, time: str):
        print(f'Вы записались на прием({mounth}-{day}-{time})')


    def info(self):
        print(f'Информация о пациенте:\nФИО: {self.full_name}\nВозраст: {self.age}\nЗаболевание: {self.disease}')


#2
class TouristSpot:

    def __init__(self, place: str, country: str, type_attraction: str):
        self.place = place
        self.country = country
        self.type_attraction = type_attraction

    @staticmethod
    def visit_place(name):
        print(f'Турист {name} посетил туристическое место!')

    def info(self):
        print(f'Информация о туристическом месте:\nМесто: {self.place}\nСтрана: {self.country}\nТип достопримечательности: {self.type_attraction}')


class ModelWindow:

    def __init__(self, title: str, left_upp_corner_x: int, left_upp_corner_y: int,horizontal_size: int, vertical_size: int, color: str, visibility: bool, border: bool,height):
        self.title = title
        self.left_upp_corner_x = left_upp_corner_x
        self.left_upp_corner_y = left_upp_corner_y
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.color = color
        self.visibility = visibility
        self.border = border
        self.height = height

    def set_horizontal(self, new_horizontal_size: int):
        self.horizontal_size = new_horizontal_size


    def set_vertical(self, new_vertical_size: int):
        if not isinstance(new_vertical_size, int): raise TypeError('Введенно неправильное значение!')
        self.vertical_size = new_vertical_size

    def set_height_window(self, new_height: int):
        if not isinstance(new_height,int):raise TypeError('Введенно неправильное значение!')
        self.height = new_height
    def set_color(self, new_color: str):
        if not isinstance(new_color, str): raise TypeError('Введенно неправильное значение!')
        self.color = new_color



    def set_state(self, new_visibility: bool, new_border: bool):
        if not isinstance(new_visibility, int): raise TypeError('Введенно неправильное значение!')
        if not isinstance(new_border, int): raise TypeError('Введенно неправильное значение!')
        self.visibility = new_visibility
        self.border = new_border

    def get_status_visibility(self):
        return self.visibility

    def get_status_border(self):
        return self.border

    def __str__(self):
        return (f'Заголовок: {self.title}'
                f'Координата левого верхнего угла ось x: {self.left_upp_corner_x}'
                f'Координата левого верхнего угла ось y : {self.left_upp_corner_y}'
                f'Размер по горизонтали: {self.horizontal_size}'
                f'Размер по вертикали: {self.vertical_size}'
                f'Цвет: {self.color}'
                f'Видимость окна:{self.visibility}'
                f'Состояние окна:{self.border}')



class ArrayUtils:

    @staticmethod
    def sum(array: list):

        sum = 0
        for i in range(0, len(array)):
            sum += array[i]

        return sum

    @staticmethod
    def multi(array: list):

        multi = 1
        for i in range(0, len(array)):
            multi = multi * array[i]

        return multi

    @staticmethod
    def inversion(array: list):

        inversed_array = []
        for i in range(len(array) -1, -1, -1):
            inversed_array.append(array[i])

        return inversed_array

    @staticmethod
    def max(array: list):

        max = array[0]
        for i in range(0, len(array)):
            if max < array[i]:
                max = array[i]

        return max

    @staticmethod
    def min(array: list):

        min = array[0]
        for i in range(0, len(array)):
            if min > array[i]:
                min = array[i]

        return min

class Vector:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z

        return Vector(new_x, new_y, new_z)




    def calculate_len(self):
        len = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return len
    def __str__(self):
        return f'{self.x, self.y, self.z}'


class Fraction:
    def __init__(self, numerator: int, denumerator: int):
        self.numerator = numerator
        self.denumerator = denumerator

    def __add__(self, other):

        if self.is_denumerator_zero(other):
            return

        new_numerator = self.numerator * other.denumerator + other.numerator * self.denumerator
        new_denumerator = self.denumerator * other.denumerator

        return Fraction(new_numerator, new_denumerator)

    def __sub__(self, other):

        if self.is_denumerator_zero(other):
            return

        new_numerator = self.numerator * other.denumerator - other.numerator * self.denumerator
        new_denumerator = self.denumerator * other.denumerator

        return Fraction(new_numerator, new_denumerator)

    def __mul__(self, other):

        if self.is_denumerator_zero(other):
            return

        new_numerator = self.numerator * other.numerator
        new_denumerator = self.denumerator * other.denumerator

        return Fraction(new_numerator, new_denumerator)

    def is_denumerator_zero(self, other):

        if self.denumerator == 0 or other.denumerator == 0:
            print('Знаменатель не может быть нулем.')
            return True

        else:
            return

    def __str__(self):

        if self.denumerator == 1:
            return f'{self.denumerator}'

        else:
            return f'{self.numerator}/{self.denumerator}'


class Program:

    @staticmethod
    def main():

        sick = Patient('Антон', 14, 'Грипп')

        sick.make_appointment('Июнь',13,'19:30')
        sick.info()




        spot = TouristSpot('Парк', 'Россия', 'культура')

        spot.visit_place('Антон')
        spot.info()




        window = ModelWindow('Окно', 1000, 600, 210,
                             210, 'Белый', True, True,1000)

        window.set_horizontal(100)
        window.set_vertical(111)
        window.set_height_window(4000)
        window.set_color('Синий')
        window.set_state(True, True)
        window.get_status_border()
        window.get_status_visibility()
        print(window)


        array = [1,2,3,4,5,6,7,8,9,10]
        print(f'Исходный массив: {array}')

        sum = ArrayUtils.sum(array)
        print(f'Сумма:{sum}')

        multi = ArrayUtils.multi(array)
        print(f'Произведение:{multi}')

        inversion = ArrayUtils.inversion(array)
        print(f'Инверсия:{inversion}')

        max = ArrayUtils.max(array)
        print(f'Максимальный элемент:{max}')

        min = ArrayUtils.min(array)
        print(f'Минимальный элемент:{min}')



        vector_1 = Vector(1, 2, 3)
        vector_2 = Vector(3, 2, 1)
        print(f'1 вектор:{vector_1}')
        print(f'2 вектор:{vector_2}')

        vector_3 = vector_1 + vector_2
        print(f'Сложение:{vector_3}')

        vector_3 = vector_1 - vector_2
        print(f'Вычитание:{vector_3}')

        vector_3 = vector_1 * vector_2
        print(f'Произведение:{vector_3}')

        length = vector_2.calculate_len()
        print(length)


        first_frac = Fraction(62,31)
        second_frac = Fraction(24,6)
        print(f'Первая дробь:{first_frac}')
        print(f'Вторая дробь:{second_frac}')

        third_frac = first_frac + second_frac
        print(f'Сложение:  {third_frac}')

        third_frac = first_frac - second_frac
        print(f'Вычитание:{third_frac}')

        third_frac = first_frac * second_frac
        print(f'Произведение:{third_frac}')

Program.main()



