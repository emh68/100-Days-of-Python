# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#      print(key, value)

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (student, score) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import row as row

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input(f"Please enter a word: ").upper()

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)




