class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grades):
        if len(grades) != 3:
            print("Please enter exactly 3 grades.")
            return
        self.students[student_id] = {"name": name, "age": age, "grades": grades}
        print("Student added!")

    def update_student(self, student_id, name=None, age=None, grades=None):
        if student_id in self.students:
            if name: 
                self.students[student_id]["name"] = name
            if age: 
                self.students[student_id]["age"] = age
            if grades:
                if len(grades) != 3:
                    print("Please enter exactly 3 grades.")
                    return
                self.students[student_id]["grades"] = grades
            print("Student updated!")
        else:
            print("Student not found!")

    def remove_student(self, student_id):
        if self.students.pop(student_id, None):
            print("Student removed!")
        else:
            print("Student not found!")

    def view_students(self):
        for id, data in self.students.items():
            print(f"ID: {id}, Name: {data['name']}, Age: {data['age']}, Grades: {data['grades']}")

    def average_grade(self, student_id):
        if student_id in self.students:
            grades = self.students[student_id]["grades"]
            avg_grade = sum(grades) / 3
            print(f"Average Grade: {avg_grade:.2f}")
        else:
            print("Student not found!")

sms = StudentManagementSystem()

