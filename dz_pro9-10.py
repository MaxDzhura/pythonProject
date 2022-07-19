
# 1) Создайте декоратор, который будет подсчитывать, сколько раз была
# вызвана декорируемая функция.

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper



@counter
def my_func(a):
    return a ** 2


my_func(22)
my_func(52)
my_func(10)
my_func(44)

print(my_func.count)



# 2) Создайте декоратор, который зарегистрирует декорируемую функцию в
# списке функций, для обработки последовательности.


list_regist_func = []

def add_func(f):
    list_regist_func.append(f)
    return f

@add_func
def sum(x, y):
    return x + y

@add_func
def mul(x, y):
    return x * y

@add_func
def my_f(x, y):
    return x ** y

print(list_regist_func)


# 3) Предположим, в классе определен метод __str__, который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода,
# чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.


def decorator(func):
    def write_file(args):
        with open(args.__class__.__name__ + '.txt', 'a') as file:
            file.write(func(args))
        return func(args)
    return write_file


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @decorator
    def __str__(self):
        return f'Название авто : {self.brand}, Модель: {self.model} \n'

car1 = Car('Toyota', "Corolla")
car2 = Car('Honda', "Accord")
print(car1, car2, sep='')

with open('Car.txt','r') as f:
    print(f.read())



# 4) Создайте декоратор с параметрами для проведения хронометража работы
# той или иной функции. Параметрами должны выступать то, сколько раз нужно
# запустить декорируемую функцию и в какой файл сохранить результаты
# хронометража. Цель - провести хронометраж декорируемой функции.


import time


def func_parametr(zapuski, name_file):
    def func_decorator(f):
        def hronometr(*args, **kwargs):
            index = 0
            while index < zapuski:
                index += 1
                start = time.time()
                result = f(*args, **kwargs)
                end = time.time()
                with open(name_file + '.txt', 'w') as file:
                    file.writelines(f"Количество запусков: {index}\nРезультат: {result}\nВремя работы : {end - start}\n")
            return f(*args, **kwargs)
        return hronometr
    return func_decorator



@func_parametr(3, 'func_mul')
def mul(a, b):
    return a * b


@func_parametr(3, 'func_plus')
def plus(a, b):
    return a + b


print(mul(4, 2))
print(plus(2, 5))



#------------ЗАДАНИЕ С 10 ЛЕКЦИИ:

# 1) Создайте декоратор, который зарегистрирует декорируемый класс в
# списке классов.

list_class = []

def add_class(cls):
    list_class.append(cls)
    return cls


@add_class
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}"

@add_class
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"

dog1 = Dog('Chapa', 8)
cat1 = Cat('Barsik', 2.5)

print(dog1)
print(cat1)
print(list_class)





# 2) Создайте декоратор класса с параметром. Параметром должна быть
# строка, которая должна дописываться (слева) к результату работы метода
# __str__.

def add_str(string):
    def decorator(cls):
        def wrapp(*args, **kwargs):
            return string + str(cls(*args, **kwargs))
        return wrapp
    return decorator



class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @add_str('Класс с котами: ')
    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"



cat1 = Cat('Bobik', 2)
print(cat1)





# 3) Для класса Box напишите статический метод, который будет подсчитывать
# суммарный объем двух ящиков, которые будут его параметрами.


class Box:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Box: a = {self.a}, b = {self.b}, c = {self.c}"

    def volume_box(self):
        return self.a * self.b * self.c

    @staticmethod
    def volume2_box(a1, b1, c1, a2, b2, c2):
        return a1 * b1 * c1 + a2 * b2 * c2


box_1 = Box(2, 3, 4)
box_2 = Box(5, 6, 7)
box_3 = Box.volume2_box(2, 3, 4, 5, 6, 7)
print(box_1.volume_box())
print(box_2.volume_box())
print(box_1, box_2, box_3, sep='\n')
