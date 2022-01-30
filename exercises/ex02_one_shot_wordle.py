"""Six letter wordle!"""
__author__ = 730480631


secret: str = "python" 
guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"  
i: int = 0 
emoji: str = "" 
letters: int = len(guess)

while len(guess) != len(secret): 
    guess = input(f"That was not {len(secret)} letters! Try again: ")


while i < len(secret): 
    if guess[i] == secret[i]: 
        emoji += GREEN_BOX 
    else:  
        exist_or_not: bool = False  
        alter_i: int = 0 
        while not exist_or_not and alter_i < len(secret): 
            if secret[alter_i] == guess[i]:  
                exist_or_not = bool(True) 
            else: 
                alter_i += 1 
        if exist_or_not:  
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX 
    i += 1 
print(emoji) 


if guess == secret:
    print("Woo! You got it!")
else: 
    input("Not quite. Play again soon! ") 




