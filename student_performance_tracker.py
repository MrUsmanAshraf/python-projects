class Custom_Error(Exception):
    pass
class Student():
    def __init__(self, name: str, score: list):
        self.name = name
        self.score = score
    def calculate_avg(self):
        sum =0 
        for mark in self.score:
            sum =sum + mark
        avg_marks= sum/len(self.score)
        return avg_marks
    def is_passing(self):
        if any (num < 40 for num in self.score):
            return f"{self.name} Needs improvement in a few subjects."
        else:
            return f"{self.name} passed."
class PerformanceTracker (Student):
    def __init__ (self, students: dict):     #dict must contain name of student as key and objects as value.
        super().__init__(name, score)
        self.students = students 

    def add_student(self):
        name = input ("Enter the name of student: ")
        subjects = ["Math", "Science", "English"]
        score = []
        for subject in subjects:
            marks = int(input (f"Enter the marks of subject {subject}: "))
            score.append (marks)
    def calculate_class_avg(self):
        avg=0
        for value in students.values ():
            s_avg=value.calculate_avg()
            avg = avg+ s_avg
        class_avg= avg/len(students.keys())
        print(f"The average of whole class is {class_avg:.2f}")
    def display_student_performance (self):
        for key, value in students.items():
            print(f"The average score of {key.upper()} is {value.calculate_avg():.2f}")
            print(value.is_passing())
students: dict ={} #this dictionary will be added as attribute to the performance tracker class.
while True: #loop to take input from user to add student name and list of numbers. these 2 attributes will be added to make objects of subject class.
    while True:
        try:
            name: str= input ("enter name of student: ")
            if name.isdigit():
                raise Custom_Error ("name of student can not not be digits.")
            if not name.isalpha():
                raise Custom_Error ("name of student can have string only.")
            else:
                break
        except Custom_Error as err:
            print(err)
    subjects = ["Math", "Science", "English"]
    score = []
    for subject in subjects:
        marks = int(input (f"Enter the marks of subject {subject}: "))
        score.append (marks)
    obj= Student(name, score) #object created every time loop run.
    students[name]= obj # student name and object of student class is added to the the "students" dict as key and value respectively. 
    while True:
        try:
            choice = input ("Do you want to add another student (yes/no): ")
            if choice.lower() not in ["yes","no"]:
                raise Custom_Error ("only yes or no is allowed")
            else:
                break
        except Custom_Error as err:
            print(err)
    if choice.lower() =="no":
        break
p1= PerformanceTracker(students)
p1.display_student_performance()
p1.calculate_class_avg()
# p1.add_student()