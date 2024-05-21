import string

input = input("please enter a series of numbers, letters and question marks:\n")
my_list = [input]


def extract_elements(lst):
    # Initialize empty lists for numbers, letters, and punctuation
    numbers = []
    letters = []
    punctuation = []

    for item in lst:
        # Check if item is a digit
        if str(item).isdigit():
            numbers.append(item)
        # Check if item is a letter
        elif str(item).isalpha():
            letters.append(item)
        # Check if item is a punctuation character
        elif str(item) in string.punctuation:
            punctuation.append(item)

    # Create variables for each category
    numbers_var = numbers
    letters_var = letters
    punctuation_var = punctuation

    return numbers_var, letters_var, punctuation_var


# Example usage
# my_list = [1, 'a', '!', 2, 'b', '?', 3, 'c', '.']
num, let, punct = extract_elements(my_list)

# Print the variables
print("Numbers:", num)
print("Letters:", let)
print("Punctuation:", punct)

s = input("please enter a series of numbers, letters and question marks:\n")

def QuestionMarks(s):
    qnum = 0
    dig = 0
    has_10 = False
    for ch in s:
        if ch.isdigit():
            if int(ch) + dig == 10:
                if qnum != 3:
                    return 'false'
                has_10 = True
            dig = int(ch)
            qnum = 0
        elif ch == '?':
            qnum += 1
    return 'true' if has_10 else 'false'

result = QuestionMarks(s)
print(result)

import mysql.connector

try:
    my_conn = mysql.connector.connect(host="eman-mysql.mysql.database.azure.com",
                                      database="world",
                                      user="eman",
                                      password="Bri@rwood2()")

    my_cursor = my_conn.cursor()
    print("You are connected to the world database successfully!")

except Exception as e:
    print("Error", e)

my_conn.close()
print("Connection Closed!!")


nums = [1,2,3,4]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

