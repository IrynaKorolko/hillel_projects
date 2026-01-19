class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(gender, age, first_name, last_name)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        self.group.append(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                return True
        return False

    def __str__(self):
        all_students = " "
        for student in self.group:
            all_students += f"{student.last_name} {student.first_name}\n"
        return f'Номер групи:{self.number}\n {all_students}'