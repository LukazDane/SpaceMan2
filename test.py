import unittest
from spaceman import is_valid, is_guess_in_word, is_word_guessed, get_guessed_word


def test_is_guess_in_word():

    assert is_guess_in_word(
        't', 'test') == True, 'is_guess_in_word() Error: new input in letters_guessed matches secret_word'


if '__name__' == '__main__':
    test_is_guess_in_word()
