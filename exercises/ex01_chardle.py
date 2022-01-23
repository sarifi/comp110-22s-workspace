"""EX01 - Chardle - A cute step toward Wordle.""" 
__author__ = "730480631" 

five_letter_word: str = input("Enter a 5-character word: ")
if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character must be a single characters")
    exit()
count: int = 0

print("Searching for " + single_char + " in " + five_letter_word)
 
if five_letter_word[0] == single_char:
    print(single_char + " found at index 0")
    count = count + 1

if five_letter_word[1] == single_char:
    print(single_char + " found at index 1")
    count = count + 1

if five_letter_word[2] == single_char:
    print(single_char + " found at index 2")
    count = count + 1

if five_letter_word[3] == single_char:
    print(single_char + " found at index 3")
    count = count + 1

if five_letter_word[4] == single_char:
    print(single_char + " found at index 4")
    count = count + 1 

if count == 1: 
    print(str(count) + " instance of " + single_char + " found in " + five_letter_word)
else: 
    if count > 1:
        print(str(count) + " instances of " + single_char + " found in " + five_letter_word)

if count == 0: 
    print("No instances of " + single_char + " found in " + five_letter_word)