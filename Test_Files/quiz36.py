class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade
    def get_grade(self):
        return self.grade
    
class Classroom:
    def __init__(self, students: list = []):
        self.students = students

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise ValueError("Student not in the classroom")

    def get_average_score(self):
        if len(self.students) == 0:
            raise ValueError("No students in the classroom")
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        return sum/len(self.students)
    
classroom = Classroom()
student1 = Student("John", 18, 90)
student2 = Student("Jane", 19, 80)
classroom.add_student(student1)
classroom.add_student(student2)
print(classroom.get_average_score() == (90 + 80) / 2)
