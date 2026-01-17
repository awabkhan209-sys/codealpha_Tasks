import random

class HangmanGame:
    def __init__(self):
        self.words = ["python", "apple", "chair", "house", "train"]
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts_left = 6

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return "already"

        self.guessed_letters.append(letter)

        if letter not in self.secret_word:
            self.attempts_left -= 1
            return "wrong"
        else:
            return "correct"

    def get_display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def is_lost(self):
        return self.attempts_left == 0
