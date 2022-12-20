class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'fullname: {self.fullname}, age: {self.age}, married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = dict(marks)

    def average_mark(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)


class Teacher(Person):
    salary = 10000

    def __init__(self, fullname, age, is_married, experience):

        super().__init__(fullname, age, is_married)
        self.experience = experience

    def sal(self, experience):
        if experience > 3:
            c = 0
            while c != experience - 3:
                c += 1
                s = round(self.salary + self.salary * 0.05, 2)
                self.salary = s
                if experience - 3 > 1:
                    self.salary = s


teach = Teacher('Forrest Gump', 45, 'yes', 6)
teach.sal(6)
teach.introduce_myself()
print(f'experience: {teach.experience}, salary: {teach.salary}')


def create_students():
    list_students = []
    student_Will = Student("Will Smith", 22, "not", {"Technology": 3, "math": 5, "history": 4, "english": 5})
    student2 = Student("Jim Carrey", 20, "not", {"Music": 5, "math": 5, "science": 3})
    student3 = Student("Adam Sandler", 21, "yes", {"Geography": 3, "Technology": 3, "history": 4})
    list_students.extend([student_Will, student2, student3])
    return list_students


for i in create_students():
    i.introduce_myself()
    print(f'subjects and marks: {i.marks}, average mark: {i.average_mark()}')
