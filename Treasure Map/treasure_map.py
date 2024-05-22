
line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.\nA, B, C are the columns and 1, 2, 3 are the rows.")
position = input("Where do you want to put the treasure? ")

letter = position[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"\n{line1}\n{line2}\n{line3}")
