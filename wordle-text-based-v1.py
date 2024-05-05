import os
import random

os.chdir(r"D:\technical\language-Python\PROJECTS\project-wordle clone game -no graphics")

def instructions():    # this function prints the game's instructions
    print("""Wordle is a single player game.
    A player must guess a five letter hidden word.
    You have six (6) attempts to guess the hidden word.
    Your progress is shown by your progress guide:
        "/" indicates the letter at that position was guessed correctly.
        "+" indicates the letter at that position is in the hidden word, 
            but is in a different position.
        "x" indicates that the letter at that position is wrong.""")

instructions()    # this calls the instructions function to print the instructions
             
def check_word():    # game's 'core': get random word, compare against guesses, report results
    with open("word_file.txt", "r") as word_file:      # opens the file
        word_list_prep = word_file.readlines()           # makes list of strings from file (yes, this includes newline character too)
        word_list = [w[:-1] for w in word_list_prep]        # list comprehension to remove '\n' last character from each string item in list
        hidden_word = random.choice(word_list)      # chooses pseudo-random item

    alphabet = {"a":False, "b":False, "c":False, "d":False, "e":False, 
        "f":False, "g":False, "h":False, "i":False, "j":False, 
        "k":False, "l":False, "m":False, "n":False, "o":False, 
        "p":False, "q":False, "r":False, "s":False, "t":False, 
        "u":False, "v":False, "w":False, "x":False, "y":False, 
        "z":False}    # local variable data structure (dict) stores alphabet letters to track guesses

    attempts = 6

    while attempts > 0:
        #  print alphabet before guess; mark each letter as guessed
        if attempts < 6:
            print("Letters that you have tried, so far: ")
            for tried_or_not in alphabet:
                if alphabet[tried_or_not] == True:
                    print (tried_or_not[0], ', ', end="")
        print("\n")

        # convert guess word to all-lower case; prevent errors due to case difference
        guess = str(input("Guess the 5-letter word: ")).lower()        
        if guess == hidden_word:
            print("\n", "You guessed the word correctly!  Congratulations!", "\n")
            break
        else:
            # TODO later - check word comes from approved list of 5-letter words (so it's not nonsense)
            #  check if guess is 5-letters only
            if (len(guess) != 5) or (guess.isalpha() != True) or ((guess) not in word_list):
                print("The word must be a valid 5 letter word.  Please try again!", "\n")

            else: 
                for letter in guess:    # update alphabet dict: 'True' for guess word's letters
                    alphabet[letter] = True
                attempts -= 1         # track the total of 6 attempts
                print()
                # print how many attempts are remaining
                print(f"You have {attempts} attempt(s) remaining.\n")         
                for char, letter in zip(hidden_word, guess):
                    #  does guess word have any letter in same position as hidden word?
                    if (letter in hidden_word) and (letter == char):
                        print(letter + "  /")
                    # does guess word have any letter somewhere else in hidden word?
                    elif letter in hidden_word:
                        print(letter + "  +")
                    #  thus, the guess word does not have any common letters found in the hidden word
                    else:
                        print(letter + "  x")
                print()

            if attempts == 0:    # if player is out of attempts, game over
                print("Sorry, you're out of attempts!  Game over!")
                print(f"The hidden word was '{hidden_word}'!", "\n")
                break

check_word()    # play the game; call the function 'check_word'


# TO-DO list (mark each DONE when completed):
''' DONE:
        force player-inputted guess word is exactly 5 characters long
        force player-inputted guess word is exactly 5 letters long (either case)
        print all guessed letters so player knows what remains unguessed 
        print the already-guessed letters in one line, separated by ", ", with newspace at-end
        open text file (read-only) of words list; put words into list; randomly choose 1 word; use that word for game
        compare guess word against word_list from text.file; ensure guess word is a valid 5-letter word from file'''
# write to new file; indicate a word is used (False) or available (True) [create DICT from words:boolean pairs]
# create version of this program that uses MATCH instead of IF (as much as possible)
# refine feedback correct/incorrect letters: only 1st correct letter/wrong spot is shown
# put onto web site (gotta get web site) for play
# instead of using "random" module, try "secrets module" (see: https://docs.python.org/3/library/secrets.html#module-secrets)
# add menu; allow player option to play again or quit
# clean up function check_word() ... What can I take out of it?  Clean up the code ......
