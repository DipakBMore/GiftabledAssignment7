
import csv
import json
MY_NAME = "Dipak More"

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
          return  f"Name: '{self.name}', Marks: {self.__marks}, Grade: {self.grade(self.__marks)}"
        


# Create three Student objects. The first one must use MY_NAME. Print all three.
student1 = Student(MY_NAME,80)
student2 = Student("Ajay",35)
student3 = Student("Ram",150)

student_information_list = [student1, student2, student3]

# print(student1)
# print(student2)
# print(student3)

# C1. Text file (10 marks)
# Write the three students to a file called students.txt, one line per student, in the form name,marks
# Then open the same file, read it back and print each line.

with open("Mystudents.txt", "w", encoding = "utf-8") as file:
     for student in student_information_list:
        file.write(f"Name: {student.name}, Marks: {student.get_marks()}\n")        
print("created txt file")

with open("Mystudents.txt", "r", encoding = "utf-8") as file:
    print("***Data read from file, Mystudents.txt: ***")
    #for student in file:
    StudentData =  file.read()
    print(StudentData)

# C2. CSV file (10 marks)
# Using the csv module, write the same three students to students.csv with a header row of name and marks.
# Then read students.csv back using the csv module and print each row.

# students = [
#     {"Name: ": "Dipak", "Marks: ": 80},
#     {"Name: ": "Ajay", "Marks: ": 74}
#     ]
students = []

for student in student_information_list:
    students.append ( {"Name: ":student.name, "Marks: ": student.get_marks()}) #here is the issue, it is not able to get the marks
  
#print(students[1:])


with open("Mystudents.csv", "w",newline="", encoding = "utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name: ", "Marks: "])
    writer.writeheader()
    writer.writerows(students)

with open("Mystudents.csv", "r", encoding = "utf-8") as file:
     print("***Data read from csv file, Mystudents.csv: ***")
     #for student in student_information_list:
     StudentData =  file.read()
           
print(StudentData)

    #  for student in student_information_list:
    #     writer = csv.DictWriter(file, fieldnames=["Name", "Marks"])
    #     file.write(f"Name: {student.name}, Marks: {student.get_marks()}\n")

# C3. JSON file (10 marks)
# Build a list of dictionaries, one per student, each with the keys name, marks and grade.
# Write it to students.json using json.dump.
# Then read it back with json.load and print the name and grade of each student.
dictlist_student = [
                    {"Name": "Dipak", "Marks": 80, "Grade": "A"},
                    {"Name": "Ajay",  "Marks": 35, "Grade": "Fail"},
                    {"Name": "Abhee", "Marks": 67, "Grade": "B"}
]



with open("Mystudents.json", "w",newline="", encoding = "utf-8") as file:
    json.dump(dictlist_student, file, indent = 2)
    print("Student list created with JSON")

with open("Mystudents.json", "r", encoding = "utf-8") as file:
     print("***Data read from JSON file, Mystudents.json: ***")
     #for student in student_information_list:
     StudentData =  json.load(file)

     #print(StudentData)
     for student in StudentData:
         print(f"{student["Name"]}: {student["Grade"]}")
         #print(student["Marks"])
        # print(student["Grade"])