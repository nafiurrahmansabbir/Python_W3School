class Student:
    def __init__(self):
        self.students = []

    def accept(self, name, roll_number, marks1, marks2):
        student = {'name': name, 'roll_number': roll_number, 'marks1': marks1, 'marks2': marks2}
        self.students.append(student)

    def display(self):
        if not self.students:
            print("No students in the list.")
        for student in self.students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Marks1: {student['marks1']}, Marks2: {student['marks2']}")

    def search(self, roll_number):
        for student in self.students:
            if student['roll_number'] == roll_number:
                print(f"Found: Name: {student['name']}, Roll Number: {student['roll_number']}, Marks1: {student['marks1']}, Marks2: {student['marks2']}")
                return
        print("Student not found.")

# Exception Handling example
try:
    sm = Student()
    sm.accept("Alice", 1, 85, 90)
    sm.accept("Bob", 2, 78, 82)
    sm.display()
    sm.search(2)
    sm.search(3)  # This will trigger "Student not found."
except Exception as e:
    print(f"An error occurred: {e}")
