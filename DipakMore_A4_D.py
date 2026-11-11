"""PART D - EXCEPTIONS (15 marks) - file: YourName_A4_D.py

D1. Write a function read_marks_file(filename) that opens a file, reads a mark from it and converts it to an integer.

Wrap the whole thing in try / except / finally:
 - catch FileNotFoundError and print a message naming the missing file
 - catch ValueError separately and print a different message saying the contents were not a number
 - the finally block must print "File operation finished."

D2. Show all three situations actually happening, in your output:
 - call it with a file that does not exist
 - call it with a file that contains the word hello instead of a number
 - call it with a file that contains 75

Create those small test files yourself from your program.
"""

# def read_marks_file(filename):
#     with open(filename, "r", encoding = "utf-8") as file:    
#         student_marks = file.readlines() 
#         for mark in student_marks:
#             print(int(mark.strip()))

# read_marks_file("Marks.txt")


def read_marks_file(filename):
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            marks = file.readlines() 
            student_marks = []
            for mark in marks:
                student_marks.append(int(mark.strip()))
        return student_marks
        
    except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            
    except ValueError:
            print("Error: The data in file that is not a number.")
           
    finally:
            print("File operation finished.")


readMarks = read_marks_file("Marks.txt")
print(readMarks)

readMarks = read_marks_file("TextMarks.txt")
print(readMarks)


readMarks = read_marks_file("TTTextMarks.txt")
print(readMarks)