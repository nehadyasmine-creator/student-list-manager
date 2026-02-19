from student import Student
import json

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

    def export(self, format, file_path):
        if format == "json":
            data = [{"id": s.id, "nom": s.nom} for s in self.students]
            with open(file_path, "w") as file:
                json.dump(data, file)
            print("Exported to JSON.")
        else:
            print("Unsupported format.")

