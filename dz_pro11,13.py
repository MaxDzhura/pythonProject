# 1) Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.


class Descriptor:

    def __get__(self, instance, owner):
        return instance.name, instance.age

    def __set__(self, instance, value):
        raise AttributeError()

    def __delete__(self, instance):
        raise AttributeError()


class Cat:

    value = Descriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Cat:  {self.name},  {self.age}"


cat1 = Cat('Bob', 2)
print(cat1)


# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.


class Figure:


    def __init__(self, height, width, long):
        self.height = height
        self.width = width
        self.long = long

    def __str__(self):
        return f" {self.height}, {self.width}, {self.long}"

    def __setattr__(self, key, value):
        if isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise AttributeError()

fig1 = Figure(10, 10, 20)

print(fig1)



# 3) Реализуйте свойство класса, которое обладает следующим
# функционалом: при установки значения этого свойства в файл с заранее
# определенным названием должно сохранятся время (когда устанавливали
# значение свойства) и установленное значение.


from datetime import datetime

class Town:

    def __init__(self, city, __year):
        self.city = city
        self.__year = __year

    def __str__(self):
        return f" {self.city}, {self.__year}"

    year = property()

    @year.getter
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value
        with open('year.txt', 'a') as f:
            f.write(f' {value}, : {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}\n')


t = Town('Odessa', 2022)
print(t)

