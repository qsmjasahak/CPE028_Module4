import Student
import Grades

p1 = Student.Student("Steve Michael Joshua Sahak", 22)
p1_grades = Grades.Grades("CPE028 ", 4, 70)
print(p1)
print("Name: ", p1.name)
print("Age: ", p1.age)


print("Course Code: ", p1_grades.Course_Code)
print("Course Grades: ", p1_grades.Course_Grade)
print("Course Units: ", p1_grades.Course_Units)