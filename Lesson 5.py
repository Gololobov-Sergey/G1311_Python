
class Human:
    def __init__(self, name, height):
        self.__name = name
        self.__height = height

    def setHeight(self, new_height):
        if new_height < 0 or new_height > 200:
            return
        self.__height = new_height

    def info(self):
        print("Name   -", self.__name)
        print("Height -", self.__height)

class Student(Human):
    def __init__(self, name, height, progress):
        Human.__init__(self, name, height)
        self.__progress = progress


    def info(self):
        print("Student info")
        super().info()
        print("Progress -", self.__progress)

class Worker(Human):
    pass


# h = Human("Vasya", 170)
# h.info()

s = Student("Petya", 160, 100)
s.info()
s.setHeight(180)
print()
s.info()

# w = Worker()
# w.info()