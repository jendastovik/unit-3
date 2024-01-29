# Quiz 36
## Python code
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def get_grade(self):
        return self.grade
    
class Classroom:
    def __init__(self, students: list = []):
        self.students = students

    def add(self, student: Student):
        self.students.append(student)

    def remove(self, student: Student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise ValueError("Student not in the classroom")

    def get_average_grade(self):
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        return sum/len(self.students)
```
## UML diagram
![](/UML/q36.png)

## Output
![](/Assets/q36.png)

