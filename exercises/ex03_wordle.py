"""Six letter wordle!"""
__author__ = "730480631"

secret: str = "codes"
# this is where the secret word is stored 


def contains_char(word_string: str, char: str) -> bool: 
    """Searching for a specific letter."""
    assert len(char) == 1
    i: int = 0
    while i < len(word_string):
        # the while loop is to ensure that the second string(char) is found at any index of the first string(word_string)
        if word_string[i] == char: 
            return True
        # function responsible for checking whether a specific letter exists or not in the secret word
        i += 1 
    return False
    # if it does it will return true otherwise it will return false


def emojified(guess: str, secret: str) -> str:
    """Calling to test for yellow, white or green box emoji."""
    assert len(guess) == len(secret)
    i: int = 0 
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # emoji variables that are used in the while loop below 
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX 
        # green if the letter exists and it is at the right index 
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        # if letter exist but it is not in the right index
        else: 
            emoji += WHITE_BOX 
        # white if the letter doesn't exist in the secret word
        i += 1 
    return emoji 


def input_guess(expected_len: int) -> str: 
    """Asks the user for a guess until they provide a guess of the expected length."""
    guess: str = input(f"Enter a {str(expected_len)} character word: ")
    while len(guess) != (expected_len): 
        # if the input doesn't equal to the expected length, then it will print notifying the user that was not the expected letters. 
        guess = input(f"That wasn't {str(expected_len)} chars! Try again: ")  
    return guess 
# keeps asking the user for a guess until it meets the desired or expected length of the secret word.


def main() -> None: 
    """The entrypoint and main game loop that keeps track of turns or whether if the user has won or not."""
    track: int = 1 
    won: bool = False
    # won variable is a bool set to false that is later used in the while loop 
    # it will either return true or false whether the user won the game or not 
    while track < 7 and not won:
        # main keeps track of turns or guesses left or used 
        print(f"=== Turn {track}/6 ===")
        guess: str = input_guess(len(secret))  
        print(emojified(guess, secret))
        if guess == secret:
            # keeps track of whether the user has won or not
            print(f"You won in {track}/6 turns!")
            won = True 
        else: 
            track += 1 
    if won is False: 
        print("X/6 - Sorry, try again tomorrow!")
# if the user has not won and no more turns left, then it will print this 


if __name__ == "__main__":
    main() 
# to run the game as a module