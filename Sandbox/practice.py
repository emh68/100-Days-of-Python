import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
for letter in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
        display[letter] = guess
    else:
        print("Wrong")

print(display)
