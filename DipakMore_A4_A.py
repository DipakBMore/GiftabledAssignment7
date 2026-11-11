#Assignment 4 - OOP Basics, Files and Exceptions

#MY_NAME = "Dipak More"

#Block 1
# class Student:
#     def __init__(self, name):
#         self.name = name
        
# a = Student("Ravi")
# b = Student("Priya")
# print(a.name)
# print(b.name)


#Block 2
# class Student:
#     def __init__(self, name):
#         print("starting up")
#         self.name = name

# s = Student("Ravi")

# Block 3
# class Account:
#     def __init__(self):
#        self.__balance = 500
       
# a = Account()
# print(a.__balance)

# Block 4
try:
    f = open("no_such_file.txt")
except FileNotFoundError:
         print("file missing")
finally:
         print("done")
