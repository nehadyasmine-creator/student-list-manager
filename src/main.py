from student import Student
from student_service import StudentService


def main():
    service = StudentService()

    print("Student List Manager")
    print("Type 'help' to show commands.")

    while True:
        command = input("> ").strip()

        if command == "list":
            service.printList()

        elif command.startswith("add"):
            parts = command.split()
            if len(parts) >= 3:
                student_id = parts[1]
                name = " ".join(parts[2:])
                service.addStudent(Student(student_id, name))

        elif command.startswith("remove"):
            parts = command.split()
            if len(parts) == 2:
                service.removeStudent(parts[1])

        elif command.startswith("export"):
            parts = command.split()
            if len(parts) == 3:
                service.export(parts[1], parts[2])

        elif command == "help":
            print("Available commands:")
            print("  list")
            print("  add <id> <name>")
            print("  remove <id>")
            print("  export <format> <file_path>")
            print("  help")
            print("  quit")

        elif command == "quit":
            print("Bye.")
            break

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
