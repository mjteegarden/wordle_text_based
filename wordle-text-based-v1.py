def instructions():
    print("""Wordle is a single player game.
          A player must guess a five letter hidden word.
          You have six (6) attempts to guess the hidden word.
          Your progress is shown by your progress guide.
          "/" indicates the letter at that position was guessed correctly.
          "+" indicates the letter at that position is in the hidden word, but is in a different position.
          "x" indicates that the letter at that position is wrong and is not in the hidden word.""")

instructions()

def check_word():
    hidden_word = "crate"
    attempts = 6

    while attempts > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("You guessed the word correctly!  Congratulations!")
            print()
            break
        else:
            attempts -= 1
            print()
            print(f"You have {attempts} attempt(s) remaining.\n")
            for char, letter in zip(hidden_word, guess):
                if (letter in hidden_word) and (letter in char):
                    print(letter + "  /")
                elif letter in hidden_word:
                    print(letter + "  +")
                else:
                    print(letter + "  x")

        if attempts == 0:
            print("You're out of attempts; game over!")
            print

check_word()
