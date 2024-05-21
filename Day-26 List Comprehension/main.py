# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)


# result = [num for num in numbers if num % 2 == 0]
# print(result)

# with open("file1.txt") as f1, open("file2.txt") as f2:
#     list1 = f1.readlines()
#     list2 = f2.readlines()
#
# result = [int(num) for num in list2 if num in list1]
# print(result)
#
#
# numbers_list = [num for num in list1]
# print(numbers_list)
#
# list2 = file2.readlines()
# print(list1)
#
#
# file1 = open("file1.txt", "r")
# list1 = file1.readlines()
#
#
# file2 = open("file2.txt", "r")
# list2 = file2.readlines()
#
# repeat_numbers = [new_item for num in list1, list2]


# List Comprehension:

# x = [new_item for item in list if test]
#
# List Comprehension for Dictionaries:
#
# new_dictionary = {new_key:new_value for (key, value) in dict.items()}
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
#
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# {'Alex': 36, 'Beth': 18, 'Caroline': 95, 'Dave': 87, 'Eleanor': 70, 'Freddie': 60}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)


# Looping through dictionaries:
# for (key, value) in student_dict.items():
#   print(value)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# Looping through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


# {new_key: new_value for (index, row) in df.iterrows()}