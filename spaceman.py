import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    # comment this line out if you use a words.txt file with each word on a new line
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_"
    return result


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    # TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    # TODO: show the player information about the game according to the project spec

    # TODO: Ask the player to guess one letter per round and check that it is only one letter

    # TODO: Check if the guessed letter is in the secret or not and give the player feedback

    # TODO: show the guessed word so far

    # TODO: check if the game has been won or lost

    letters_guessed = []
    guess_limit = len(secret_word)
    guess_number = 0

    print("Welcome to the world of Spaceman!")
    print("Take a chance, guess a letter, let's play a game...\n")

    print("Guesses: " + str(guess_limit - guess_number))
    print("_"*len(secret_word))

    while True:
        guess = input("Guess: ")
        if is_valid(guess, letters_guessed):
            letters_guessed.extend(guess)
            guess_number += 1
            if is_guess_in_word(guess, secret_word):
                print("You got it! :)")
            else:
                print("X_X incorrect :(")
        else:
            print("Please try a valid input")

        print("Guesses left: " + str(guess_limit - guess_number))
        print(get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print("You git it! The word was " + secret_word)
            break
        if guess_number >= guess_limit:
            print(
                "Looks like you need to go back to the trainer school... \nThe word was " + secret_word)
            break


def is_valid(guess, letters_guessed):
    if guess.isalpha():
        if len(guess) == 1:
            if guess not in letters_guessed:
                return True
    return False


# These function calls that will start the game
# secret_word = load_word()
# spaceman(secret_word)
    # while True:
    #     play_again = input("Would you like to play again? (yes, y): ")
    #     play_again = play_again.lower()
    #     if play_again == 'y' or play_again == 'yes':
    #         secret_word = load_word()
    #         spaceman(secret_word)
    #     else:
    #         break

if '__name__' == '__main__':
    running = True
    while running:
        secret_word = load_word()
        spaceman(secret_word)
