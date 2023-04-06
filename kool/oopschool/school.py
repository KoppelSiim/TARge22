
"""School class which stores information about courses and students."""
from oopschool.student import Student
from oopschool.course import Course
"""
def __init__(self, name) - konstruktor, kuhu saab kaasa anda kooli nime. 
Kooli nimi tuleb salvestada muutujasse self.name. 
Lisaks on mõistlik luua üks muutuja õpilaste ja üks muutuja kursuste hoidmiseks.

def add_course(self, course: Course) - kursus lisatakse kooli. 
Kui selline kursus on juba olemas, siis seda teistkordselt ei lisata.

def add_student(self, student: Student) - õpilane lisatakse kooli.
Kui selline õpilane on juba olemas, siis teda teistkordselt ei lisata.
Ühtlasi kui õpilane lisatakse kooli, siis määratakse talle unikaalne id (set_id() meetod õpilasel).

def add_student_grade(self, student: Student, course: Course, grade: int) - 
lisatakse hinne õpilasele konkreetse kursuse eest.
Hinne lisatakse ainult siis, kui õpilane on selles koolis ja kursus on selles koolis olemas.
Hinne peaks minema ka õpilase ja kursuse külge (selleks, et nende kaudu saada hindeinfot kätte).
Seega siin on mõistlik välja kutsuda vastavalt õpilasel ja kursusel mingeid oma loodud meetodeid,
mis salvestavad hinded nende objektide külge. Siin ei pea arvestama olukorraga,
kui lisatakse hinne kursusele, kus juba on hinne (sellist olukorda ei testita).
Kui on soovi, võid proovida sellises olukorras uut hinnet ignoreerida või kirjutad vana üle.
Hinde väärtust kontrollima ei pea. See on täisarv vahemikus 1-5 (kaasa arvatud).

get_students(self) -> list[Student] - tagastab õpilaste järjendi.
Elemendid on Student objektid ning elemendid on järjendis nende lisamise järjekorras.

get_courses(self) -> list[Course] - tagastab kursuste järjendi. 
Elemendid on Course objektid ning elemendid on järjestatud nende lisamise järjekorras.

def get_students_ordered_by_average_grade(self) -> list[Student] - tagastab õpilaste järjendi järjestatuna
keskmise hinde järgi nii, et eespool on õpilane,
kelle keskmine hinne on kõrgem. Siin ei pea midagi erilist tegema õpilastega, 
kelle keskmine hinne on sama (need võivad jääda samasse järjekorda).
"""

class School:

    def __init__(self, name):
        """Constructor with name, list of: courses, students, grades"""
        self.name = name
        self.courses = []
        self.students = []
        self.grades = []
        self.next_id = 0

    def add_course(self, course):
        """Check if course is already in courselist, if not, then add it."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        """Adds student to school if he/she has not already been added.
        Calls student set_id method with id as a parameter."""
        if student not in self.students:
            self.next_id += 1
            id_ = int(self.next_id)
            Student.set_id(student, id_)
            self.students.append(student)

    def add_student_grade(self, student, course, grade: int):
        """Check if the student and course exist in school, if yes, then add grade.
        Calls the Student add_grade_to_student method to correlate grade with student
        and Course method add_student_grade_to_course to correlate student's grade with course."""
        if student in self.students and course in self.courses:
            Student.add_grade_to_student(student, course, grade)
            Course.add_student_grade_to_course(course,student,grade)

    def get_students(self):
        """Return list of all students."""
        return self.students

    def get_courses(self):
        """Return list of all the courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self):
        students = self.get_students()
        s2 = sorted(students, reverse=True, key= lambda student: student.get_average_grade())
        return s2