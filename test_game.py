import pytest
from game import choose_word, process_guess, display_word, WORD_LIST

def test_choose_word():
    word = choose_word()
    assert word in WORD_LIST

def test_process_guess_correct():
    word = "chinchilla"
    guessed_letters = set()
    result = process_guess(word, guessed_letters, "l")
    assert result is True
    assert "l" in guessed_letters

def test_process_guess_incorrect():
    word = "chinchilla"
    guessed_letters = set()
    result = process_guess(word, guessed_letters, "z")
    assert result is False
    assert "z" not in guessed_letters

def test_display_word():
    word = "chinchilla"
    guessed_letters = {"c", "l"}
    displayed = display_word(word, guessed_letters)
    assert displayed == "c _ _ _ c _ _ l l _"
