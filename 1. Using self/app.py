class Student:
    def __init__(self, name, marks, course):
        self.name = name
        self.marks = marks
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)
        print("Student Course:", self.course)

student1 = Student("Ali", 90, "Mathematics")
student2 = Student("Ramesha", 22, "Computer Science")

student1.display()
student2.display()
