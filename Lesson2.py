class Student:
    count = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        #print("Я народився")
        Student.count += 1

    def setAge(self, age):
        if age > 100:
            return
        self.age = age

    # def print(self):
    #     print(f"Студент {self.name}, вік: {self.age} років, зріст {self.height} см\n")

    def __str__(self):
        return f"Студент {self.name}, вік: {self.age} років, зріст {self.height} см\n"

    def __del__(self):
        Student.count -= 1
        print("Студент пішов...")

    def grow(self):
        if self.height + 5 <= 200:
            self.height += 5


print(Student.count)

student1 = Student("Ilya", 13, 155)
student1.setAge(16)
print(student1)

print(Student.count)

student2 = Student("Mark", 14, 160)
print(student2)
student2.grow()
print(student2)

print(Student.count)
