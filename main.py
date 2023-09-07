import random
import sys
import pdb
from termcolor import colored

def read_random_word():
    with open(
        "/Users/brendan/Documents/Programming/Tutorials/Python/wordle/words.txt"
    ) as f:
        words = f.read().splitlines()
        return random.choice(words)

def game():
    play = input("Would you like to play Wordle? press any key or \"q\" to quit. ").lower()
    #pdb.set_trace()
    while play != "q":
        word = read_random_word()
        for attempt in range(1, 7):
            guess = input("\nPlease enter a 5 letter word: ").lower()

            sys.stdout.write("\x1b[1A")
            sys.stdout.write("\x1b[2K")

            for i in range(min(len(guess), 5)):
                if guess[i] == word[i]:
                    print(colored(guess[i], "green"), end="")
                elif guess[i] in word:
                    print(colored(guess[i], "yellow"), end="")
                else:
                    print(guess[i], end="")
            print()

            if guess == word:
                print(colored(f"\nCONGRATS, you got the wordle in {attempt}", "red"))
                play = input("\ndo you want to play again? \"q\" to exit").lower()
                if play == "q":
                    exit()
                else:
                    #pdb.set_trace()
                    break
            elif attempt == 6:
                print(colored(f"Sorry, the word was {word}", "Orange"))
                play = input("\ndo you want to play again? \"q\" to exit").lower()
                if play == "q":
                    exit()
                else:
                    #pdb.set_trace()
                    break
                

game()
