# Code to practice using for loops
student_heights = input("Input a list of student heights ").split()
int_student_heights = []
for n in range(0, len(student_heights)):
    int_student_heights.append(int(student_heights[n]))


total_height = 0
for height in int_student_heights:
    total_height += height

number_students = 0
for students in student_heights:
    number_students += 1

avg_height = (round(total_height/number_students))

print(
    f"total height = {total_height}\nnumber of students = {number_students}\naverage height = {avg_height}")
