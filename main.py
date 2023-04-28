class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        total = 0
        length = 0
        for value in self.grades.values():
            length += len(value)
            for grade in value:
                total += grade
        res = total / length
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student!'
        return self._average_grade() < other._average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_lect(self):
        total = 0
        length = 0
        for value in self.grades.values():
            length += len(value)
            for grade in value:
                total += grade
        res = total / length
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_lect()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer!'
        return self._average_lect() < other._average_lect()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

some_lecturer = Lecturer('Yulia', 'Galkovskaya')
some_lecturer.courses_attached.append('Git')
some_lecturer.courses_attached.append('Python')

some_student = Student('Alina', 'Belimenko', 'female')
some_student.courses_in_progress.append('Git')
some_student.finished_courses.append('Python')
some_student.courses_in_progress.append('API')


some_student.rate_lect(some_lecturer, 'Git', 10)
some_student.rate_lect(some_lecturer, 'Git', 10)
some_student.rate_lect(some_lecturer, 'Git', 9)

another_student = Student('Ivan', 'Popov', 'male')
another_student.courses_in_progress.append('Python')
another_student.finished_courses.append('Git')
another_student.courses_in_progress.append('API')

some_reviewer = Reviewer('Marina', 'Chihanova')
some_reviewer.courses_attached.append('Git')
some_reviewer.courses_attached.append('Pythom')
some_reviewer.courses_attached.append('API')

some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'API', 8)
some_reviewer.rate_hw(some_student, 'API', 6)
some_reviewer.rate_hw(some_student, 'API', 9)
some_reviewer.rate_hw(another_student, 'API', 7)
some_reviewer.rate_hw(another_student, 'API', 10)
some_reviewer.rate_hw(another_student, 'API', 9)

another_reviewer = Reviewer('Olga', 'Zlobina')
another_reviewer.courses_attached.append('Python')
another_reviewer.rate_hw(another_student, 'Python', 9)
another_reviewer.rate_hw(another_student, 'Python', 8)
another_reviewer.rate_hw(another_student, 'Python', 9)

another_lecturer = Lecturer('Maria', 'Maltseva')
another_lecturer.courses_attached.append('Git')
another_lecturer.courses_attached.append('Python')
some_student.rate_lect(another_lecturer, 'Git', 8)
some_student.rate_lect(another_lecturer, 'Git', 6)
some_student.rate_lect(another_lecturer, 'Git', 7)
another_student.rate_lect(another_lecturer, 'Python', 10)
another_student.rate_lect(another_lecturer, 'Python', 8)
another_student.rate_lect(another_lecturer, 'Python', 7.5)
another_student.rate_lect(some_lecturer, 'Python', 9)
another_student.rate_lect(some_lecturer, 'Python', 6)
another_student.rate_lect(some_lecturer, 'Python', 7.5)

print(some_student)
print(some_student.grades)
print(another_student)
print(another_student.grades)
print(some_student < another_student)
print(some_student > another_student)
print(some_reviewer)
print(some_reviewer.courses_attached)
print(another_reviewer)
print(another_reviewer.courses_attached)
print(some_lecturer)
print(some_lecturer.grades)
print(another_lecturer)
print(another_lecturer.grades)
print(some_lecturer < another_lecturer)
print(some_lecturer > another_lecturer)

def average_lect_course(lecturers, course):
  total = 0
  length = 0
  for l in lecturers:
    if not isinstance(l, Lecturer):
      return 'Not lecturers'
    for value in l.grades[course]:
      total += value
    length += 1
  res = total / length
  return res

lecturers = []
lecturers.append(some_lecturer)
lecturers.append(another_lecturer)

print(average_lect_course(lecturers, 'Git'))

def average_grade_course(students, course):
  total = 0
  length = 0
  for s in students:
    if not isinstance(s, Student):
      return 'Not students'
    for value in s.grades[course]:
      total += value
    length += 1
  res = total / length
  return res

students = []
students.append(some_student)
students.append(another_student)

print(average_grade_course(students, 'API'))
    




