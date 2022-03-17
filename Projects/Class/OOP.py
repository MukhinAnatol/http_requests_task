class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.eval:
                lecturer.eval[course] += [grade]
            else:
                lecturer.eval[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = 0
        length = 0
        for value in self.grades.values():
            total += sum(value)
            length += len(value)
        return round(float(total / length), 2)


    def __str__(self):
        text = f"Имя: {self.name} " \
               f"\nФамилия: {self.surname} " \
               f"\nСредняя оценка за домашние задания: {self.average_grade()} " \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}" \
               f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return text

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return 'Error'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        else:
            return 'Error'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):

    def rate_hw (self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname}"
        return text

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.eval = {}

    def average_eval(self):
        total = 0
        length = 0
        for value in self.eval.values():
            total += sum(value)
            length += len(value)
        return round(float(total / length), 2)

    def __str__(self):
            text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_eval()}"
            return text

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_eval() < other.average_eval()
        else:
            return 'Error'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_eval() > other.average_eval()
        else:
            return 'Error'

student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Введение в программирование']

student_2 = Student('John', 'Snow', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

first_reviewer.rate_hw(student_1, 'Введение в программирование', 7)
first_reviewer.rate_hw(student_1, 'Введение в программирование', 10)
first_reviewer.rate_hw(student_1, 'Введение в программирование', 8)

first_reviewer.rate_hw(student_2, 'Введение в программирование', 5)
first_reviewer.rate_hw(student_2, 'Введение в программирование', 9)
first_reviewer.rate_hw(student_2, 'Введение в программирование', 9)

first_reviewer.rate_hw(student_1, 'Python', 7)
first_reviewer.rate_hw(student_1, 'Python', 10)
first_reviewer.rate_hw(student_1, 'Python', 10)
first_reviewer.rate_hw(student_1, 'Python', 7)

second_reviewer = Reviewer('New', 'Man')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_lecturer = Lecturer('Ned', 'Stark')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

student_2.rate_lecture(first_lecturer, 'Python', 8)
student_2.rate_lecture(first_lecturer, 'Python', 5)
student_2.rate_lecture(first_lecturer, 'Python', 5)
student_2.rate_lecture(first_lecturer, 'Python', 8)

second_lecturer = Lecturer('Sirius', 'Snape')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Введение в программирование']

student_1.rate_lecture(second_lecturer, 'Python', 7)
student_1.rate_lecture(second_lecturer, 'Python', 6)
student_1.rate_lecture(second_lecturer, 'Python', 9)
student_2.rate_lecture(first_lecturer, 'Python', 8)

second_reviewer.rate_hw(student_2, 'Python', 9)
second_reviewer.rate_hw(student_2, 'Python', 10)
second_reviewer.rate_hw(student_2, 'Python', 10)
second_reviewer.rate_hw(student_2, 'Python', 10)

print(student_1.grades)
print(student_2.grades)
print(first_lecturer.eval)
print(second_lecturer.eval)
print(first_reviewer)
print(second_reviewer)
print(first_lecturer)
print(second_lecturer)
print(student_1)
print(student_2)

print(student_1 < student_2)
print(first_lecturer > second_lecturer)

students_list = [student_1, student_2]
lecturers_list = [first_lecturer, second_lecturer]

def avg_students (students : list, course):
    total = 0
    length = 0
    for student in students:
        if course in student.courses_in_progress or course in student.finished_courses:
            total += sum(student.grades[course])
            length += len(student.grades[course])
    return f"Средняя оценка студентов за курс {course}: {round(total / length, 2)}"

def avg_lecturers(lecturers: list, course):
    total = 0
    length = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total += sum(lecturer.eval[course])
            length += len(lecturer.eval[course])
    return f"Средняя оценка лекторов за лекции по курсу {course}: {round(total / length, 2)}"


print(avg_lecturers(lecturers_list, 'Python'))
print(avg_students(students_list, 'Python'))
print(avg_students(students_list, 'Введение в программирование'))