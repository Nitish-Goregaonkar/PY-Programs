class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grades):
        if len(grades) != 3:
            print("Please enter exactly 3 grades.")
            return
        self.students[student_id] = {"name": name, "age": age, "grades": grades}
        print("Student added!")

    