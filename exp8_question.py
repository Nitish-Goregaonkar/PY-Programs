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

   