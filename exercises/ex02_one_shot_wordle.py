"""Six letter wordle!"""
__author__ = "730480631"


secret: str = "python" 
guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"  
# the first two variables are declared as strings, first one stores the secret word 
# the second variable is guess which is the input and it has the len of the secret word to tell the user how many letter word the secret word is. 
# these are the emojis like the boxes where they will go into the emoji string 


while len(guess) != len(secret): 
    guess = input(f"That was not {len(secret)} letters! Try again: ")
# this while loop is simply checking to make sure that the length of the guess and the secret word matches. 


i: int = 0 
emoji: str = "" 
# line 16 is for the index which has to be set to 0 and the line after is the emoji which is an empty string and the resulting emoji will be put it in here. 


while i < len(secret): 
    exist_or_not: bool = False  
    if guess[i] == secret[i]: 
        emoji += GREEN_BOX 
    else:  
        alter_i: int = 0 
        while alter_i < len(secret): 
            if secret[alter_i] == guess[i]:  
                exist_or_not = True 
            alter_i += 1 
        if exist_or_not:  
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX 
    i += 1 

print(emoji) 

# his while loop above consists of two if else statements and another while loop inside of the bigger while loop. 
# the boolean variable is checking if any of the chr exists or not anywhere in the secret word
# then if the indiex of the secret and guess word is being matched, if it is then it will result into a green box. 
# further into the loop, the what if statements is checking if the alternate index mathces the guess index
# then if the chr in guess exists anywhere in the secret then it will result into a yellow box otherwise it will print a white box. 
# lastly it will print the resulting emojis based on the input 

if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!") 

# for the final part, if the guess does indeed is the secret word, then it will print the string on line 45
# if it is not the secret word, it will print the string in line 47