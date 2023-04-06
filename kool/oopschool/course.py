"""Course class with name and grades."""


class Course:
    """Course class with name and grades."""
    def __init__(self, name: str):
        """Constructor with name and grades dictionary, dict[student.name] = grade."""
        self.name = name
        self.grades = dict()

    def add_student_grade_to_course(self, student, grade: int):
        """Add student grade to course."""
        self.grades[student] = grade

    def get_grades(self):
        """Loop the grade dictinary, store student name and grade to tuple, add tuple to list, return list."""
        student_grades = []
        for key, val in self.grades.items():
            info = (key, val)
            student_grades.append(info)
        return student_grades

    def get_average_grade(self) -> float:
        """Calculate the course average grade and return in float."""
        total = 0
        sgrades = self.get_grades()
        total_grades = len(sgrades)
        for i in sgrades:
            total += i[1]
        return float(total/total_grades)

    def __repr__(self):
        """Return course name as string."""
        return f"{self.name}"
