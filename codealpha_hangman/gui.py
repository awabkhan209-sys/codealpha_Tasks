import tkinter as tk
from game_logic import HangmanGame

class HangmanGUI:
    def __init__(self, root):
        self.game = HangmanGame()
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x350")
        self.root.config(bg="#f2f2f2")

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        tk.Label(self.root, text="Hangman Game",
                 font=("Arial", 18, "bold"),
                 bg="#f2f2f2").pack(pady=10)

        self.word_label = tk.Label(self.root, font=("Courier", 20), bg="#f2f2f2")
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(self.root, font=("Arial", 12), bg="#f2f2f2")
        self.attempts_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        tk.Button(self.root, text="Guess Letter",
                  command=self.make_guess,
                  bg="#4CAF50", fg="white",
                  font=("Arial", 12)).pack()

        self.message_label = tk.Label(self.root, text="", font=("Arial", 12),
                                      fg="red", bg="#f2f2f2")
        self.message_label.pack(pady=10)

    def update_display(self):
        self.word_label.config(text=self.game.get_display_word())
        self.attempts_label.config(text=f"Attempts Left: {self.game.attempts_left}")

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Enter only ONE letter")
            return

        result = self.game.guess_letter(guess)

        if result == "already":
            self.message_label.config(text="Already guessed!")
        elif result == "wrong":
            self.message_label.config(text="Wrong guess!")
        else:
            self.message_label.config(text="Good guess!")

        self.update_display()
        self.check_status()

    def check_status(self):
        if self.game.is_won():
            self.message_label.config(text="🎉 YOU WON!")
        elif self.game.is_lost():
            self.message_label.config(
                text=f"❌ YOU LOST! Word was: {self.game.secret_word}"
            )
