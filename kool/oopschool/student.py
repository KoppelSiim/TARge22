"""Student class with student name and grades."""
"""
Loo järgmised meetodid:

        def __init__(self, name: str) - konstruktor, kuhu saab kaasa anda õpilase nime. 
        Siin on vaja luua muutuja(d) õpilase hinnete hoidmiseks.
        Lisaks tuleb luua muutuja õpilase id jaoks, mille väärtust alguses peab olema None.

        def set_id(self, id: int) - õpilasele määratakse unikaalne identifikaator. 
        Kui identifikaator on juba määratud, siis teist korda seda üle kirjutada ei saa
        (sellisel juhul lihtsalt ignoreeritakse uue väärtuse lisamist)

        def get_id(self) -> int - tagastab õpilase identifikaatori

        def get_grades(self) -> list[tuple[Course, int]] - tagastab järjendi õpilase tulemustest.
        Iga element on ennik (tuple), mille esimene element on kursuse objekt
        ja teine element on hinne sellel kursusel. 
        Hindeid pannakse School klassis oleva meetodiga add_student_grade().
        Mõistlik on õpilase klassi lisada mingi abistav meetod, millega hinnet lisada.

        def get_average_grade(self) - tagastab õpilase keskmise hinde. Kui õpilasel hindeid pole, tagastab meetod -1.

        def __repr__(self) -> str - tagastab objekti sõnekuju. Siin klassis tagastab õpilase nime.
        """


class Student:
    def __init__(self, name: str):
        """Student constructor with name, id and grades dictionary."""
        self.name = name
        self.id_ = None
        self.grades = dict()

    def set_id(self, id_: int):
        """Set student id if id is uniqe and not already set."""
        if self.id_ is None:
            self.id_ = id_

    def get_id(self) -> int:
        """Return student id."""
        return self.id_

    def add_grade_to_student(self, course, grade: int):
        """Add grade to student for the course."""
        self.grades[course] = grade

    def get_grades(self):
        """Return a list of tuples with student's grades, list[(Course, grade)]."""
        gradelist = []
        for key, value in self.grades.items():
            info = (key, value)
            gradelist.append(info)
        return gradelist

    def get_average_grade(self):
        """Return student's average grade or -1 if there are no grades."""
        total = 0
        list_of_grades = self.get_grades()
        nrof_grades = len(list_of_grades)
        if nrof_grades > 0:
            for i in list_of_grades:
                total += i[1]
            return float(total / nrof_grades)
        else:
            return -1

    def __repr__(self) -> str:
        """Return student name in string form."""
        return f"{self.name}"