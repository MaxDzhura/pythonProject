class People:

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.surname}--{self.name}--{self.age}"


class Student(People):

    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)

    def __str__(self):
        return super().__str__()


class Group:

    def __init__(self ,curs):
         self.students = []
         self.curs = curs

    def search(self, poisk):
        self.poisk = poisk
        for i, item in enumerate(self.students):
            if self.poisk in item.surname:
                print(self.students[i])




    def __str__(self):
        res = f"{self.curs}:\n"
        res += "\n".join(map(str, self.students))
        return res


st1 = Student("Бобер", "Альберто", "22")
st2 = Student("Боберcaн", "Алекс", "19")
st3 = Student("Бобиков", "Вася", "23")
st4 = Student("Гномов", "Витя", "18")
st5 = Student("Таппнок", "Коля", "20")

gr1 = Group("Python")

gr1.students.append(st1)
gr1.students.append(st2)
gr1.students.append(st3)
gr1.students.append(st4)
gr1.students.append(st5)

gr1.students.remove(st1)

print(gr1.search("Бобиков"))
print(gr1.curs)



