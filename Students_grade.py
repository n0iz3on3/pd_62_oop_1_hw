class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grade(self):
        self.average = [round(sum(values)/len(values), 1) for values in self.grades.values()]
        return self.average[0]
            
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._avg_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')
            
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет!')
            return
        if self._avg_grade() < other._avg_grade():
            return f'Средний балл студента {other.name} лучше, чем у {self.name}'
        else:
            return f'Средний балл студента {self.name} лучше, чем у {other.name}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] 

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        self.average = [round(sum(values)/len(values), 1) for values in self.grades.values()]
        return self.average[0]

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._avg_grade()}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет!')
            return
        if self._avg_grade() < other._avg_grade():
            return f'Средний балл лектора {other.name} лучше, чем у {self.name}'
        else:
            return f'Средний балл лектора {self.name} лучше, чем у {other.name}'
                
class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Go']
best_student.finished_courses = ['Введение в программирование']

good_but_not_the_best_student = Student('Miom', 'Myiom', 'male')
good_but_not_the_best_student.courses_in_progress += ['Python', 'Go']
good_but_not_the_best_student.finished_courses = ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

lool_reviewer = Reviewer('Once', 'Toldme')
lool_reviewer.courses_attached += ['Go']

cool_lecturer = Lecturer('Nice', 'One')
cool_lecturer.courses_attached += ['Python']

lool_lecturer = Lecturer('Slice', 'Twice')
lool_lecturer.courses_attached += ['Go']

cool_reviewer.rate_student(best_student, 'Python', 9)
cool_reviewer.rate_student(best_student, 'Python', 9)
cool_reviewer.rate_student(best_student, 'Python', 10)

lool_reviewer.rate_student(best_student, 'Go', 7)
lool_reviewer.rate_student(best_student, 'Go', 9)
lool_reviewer.rate_student(best_student, 'Go', 10)

cool_reviewer.rate_student(good_but_not_the_best_student, 'Python', 9)
cool_reviewer.rate_student(good_but_not_the_best_student, 'Python', 7)
cool_reviewer.rate_student(good_but_not_the_best_student, 'Python', 8)

lool_reviewer.rate_student(good_but_not_the_best_student, 'Go', 6)
lool_reviewer.rate_student(good_but_not_the_best_student, 'Go', 9)
lool_reviewer.rate_student(good_but_not_the_best_student, 'Go', 6)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)

best_student.rate_lecturer(lool_lecturer, 'Go', 7)
best_student.rate_lecturer(lool_lecturer, 'Go', 9)
best_student.rate_lecturer(lool_lecturer, 'Go', 9)

good_but_not_the_best_student.rate_lecturer(cool_lecturer, 'Python', 10)
good_but_not_the_best_student.rate_lecturer(cool_lecturer, 'Python', 8)
good_but_not_the_best_student.rate_lecturer(cool_lecturer, 'Python', 9)

good_but_not_the_best_student.rate_lecturer(lool_lecturer, 'Go', 9)
good_but_not_the_best_student.rate_lecturer(lool_lecturer, 'Go', 9)
good_but_not_the_best_student.rate_lecturer(lool_lecturer, 'Go', 10)

students_list = [
    {'name': best_student.name, 'surname': best_student.surname, 'gender': best_student.gender, 
    'finished_courses': best_student.finished_courses, 'courses_in_progress': best_student.courses_in_progress, 
    'grades': best_student.grades},
    {'name': good_but_not_the_best_student.name, 'surname': good_but_not_the_best_student.surname, 'gender': good_but_not_the_best_student.gender, 
    'finished_courses': good_but_not_the_best_student.finished_courses, 'courses_in_progress': good_but_not_the_best_student.courses_in_progress, 
    'grades': good_but_not_the_best_student.grades}
]

lecturers_list = [
    {'name': cool_lecturer.name, 'surname': cool_lecturer.surname, 'courses_attached': cool_lecturer.courses_attached, 'grades': cool_lecturer.grades},
    {'name': lool_lecturer.name, 'surname': lool_lecturer.surname, 'courses_attached': lool_lecturer.courses_attached, 'grades': lool_lecturer.grades}
]

def get_avg_rate_student(students, course):
    sum_hw = 0
    for student in students:
        for courses, grades in student['grades'].items():
             if courses == course:
                sum_hw += sum(grades) / len(grades)
    
    return f'Средний балл студентов по курсу {course}: {round((sum_hw)/2, 2)}'

def get_avg_rate_lecturer(lecturers, course):
    sum_lct = 0
    for lecturer in lecturers:
        for courses, grades in lecturer['grades'].items():
             if courses == course:
                sum_lct += sum(grades) / len(grades)
    
    return f'Средний балл лекторов по курсу {course}: {round(sum_lct, 2)}'
       
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(lool_reviewer)
print()
print(lool_lecturer)
print()
print(good_but_not_the_best_student)
print()
print(best_student < good_but_not_the_best_student)
print(lool_lecturer < cool_lecturer)
print()
print(get_avg_rate_student(students_list, "Python"))
print(get_avg_rate_student(students_list, "Go"))
print()
print(get_avg_rate_lecturer(lecturers_list, "Python"))
print(get_avg_rate_lecturer(lecturers_list, "Go"))