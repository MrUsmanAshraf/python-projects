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
        avg_marks=self.calculate_avg()
        if avg_marks >= 40:
            print(f"{self.name.upper()} is passed")
        else:
            print(f"{self.name.upper()} needs improvement")
class PerformanceTracker (Student):
    def __init__ (self, students: dict):     #dict must contain name of student as key and objects as value.
        super().__init__(name, score)
        self.students = students 

    def add_student(self):
        name = input ("Enter the name of student: ")
        subjects = int(input ("Enter number of subjects to add their marks: "))
        score = []
        for subject in range (1, subjects+1):
            marks = int(input (f"Enter the marks of subject {subject}: "))
            score.append (marks)
    def calculate_class_avg(self):
        avg=0
        for value in students.values ():
            s_avg=value.calculate_avg()
            # obj1=students.values ()
            # obj1.calculate_avg()
            avg = avg+ s_avg
            # avg+= avg
        class_avg= avg/len(students.keys())
        return class_avg
    def display_student_performance (self):
        for key, value in students.items():
            print(f"The average score of {key.upper()} is {value.calculate_avg():.2f}")
            value.is_passing()
students: dict ={} #this dictionary will be added as attribute to the performance tracker class.
while True: #loop to take input from user to add student name and list of numbers. these 2 attributes will be added to make objects of subject class.
    name= input ("enter name of student: ")
    subjects = ["Math", "Science", "English"]
    score = []
    for subject in subjects:
        marks = int(input (f"Enter the marks of subject {subject}: "))
        score.append (marks)
    obj= Student(name, score) #object created every time loop run.
    students[name]= obj # student name and object of student class is added to the the "students" dict as key and value respectively. 
    choice = input ("Do you want to add another student (yes/no): ")
    if choice =="no":
        break
p1= PerformanceTracker(students)
p1.display_student_performance()
