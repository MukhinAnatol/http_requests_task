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