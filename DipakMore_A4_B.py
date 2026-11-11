#PART B - OOP BASICS (25 marks) 

MY_NAME = "Dipak More"
# B1. Write a class Student with:
#  - a constructor that takes name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks # marks stored as a private attribute using two underscores
       # print("Student Details: ") - Checked initialization

    #a method  that refuses anything below 0 or above 100 and prints a clear message
    def set_marks(self, value):
         if value<0 or value >100:
            print(f"Invalid Entry ({value}). Marks must be between 0 and 100.")
         else:
            self.__marks = value

    # - a method get_marks() that returns the marks
    def get_marks(self):
        return self.__marks

    # - a method grade() that returns A for 80 and above, B for 60 to 79, C for 40 to 59, and Fail below 40
    def grade(self, value):
        if value >= 80:
            return "A"
        elif value >= 60:
            return "B"
        elif value >= 40:
            return "C"
        else:
            return "Fail"        

    # - a __str__ method, as covered in the Session 6 notes, so that printing the object shows the name, the marks and the grade

    def __str__(self):
         # return  f"Name: '{self.name}', Marks: {self.__marks}, Grade: {self.grade(self.__marks)}"
        print(f"Name: '{self.name}', Marks: {self.__marks}, Grade: {self.grade(self.__marks)}")

#B2. Create three Student objects. The first one must use MY_NAME. Print all three.
student1 = Student(MY_NAME,80)
student2 = Student("Ajay",35)
student3 = Student("Ram",150)

student1.__str__()
student2.__str__()
student3.__str__()
#Note: If I want to use below print functions, then I have to comment print from __str__ and uncomment return
# print(student1)
# print(student2)
# print(student3)

#B3. Prove your validation works. Try to set marks to 150 and show in your output that it was refused and the old value kept.
student1.set_marks(150)
print(f"Original marks for {student1.name}: {student1.get_marks()}")