from student import Student


class StudentService:

    def __init__(self):
        self.students = []

    def printList(self):
        print("Students:")
        for student in self.students:
            print(f"- {student.id}: {student.nom}")

    def addStudent(self, student):
        self.students.append(student)
        print(f"Student '{student.nom}' added.")

    def removeStudent(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print(f"Student with id '{student_id}' removed.")
                return
        print("Student not found.")
