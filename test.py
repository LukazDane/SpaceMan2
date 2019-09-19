import unittest
from spaceman import is_valid, is_guess_in_word, is_word_guessed, get_guessed_word


def test_is_guess_in_word():
    assert is_guess_in_word(
        't', 'test') == True, 'is_guess_in_word() Error: new input in letters_guessed matches secret_word'


def test_is_word_guessed():
    assert is_word_guessed(
        'test', 'test') == True, 'is_word_guessed() Error: word == word'


def test_get_guessed_word():
    assert get_guessed_word(
        'test', 'tést') == 't_st', 'get_guessed_word() Error: words do not match'


if '__name__' == '__main__':
    test_is_guess_in_word()
