# Code to practice using for loops instead of built-in max function
student_scores = input('Please enter the student scores: ').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest number is: {highest_score}")
