import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 40), width=2, height=1,
                                command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            self.check_win()
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                self.show_win_message(self.board[i][0])
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                self.show_win_message(self.board[0][i])
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.show_win_message(self.board[0][0])
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.show_win_message(self.board[0][2])
            return
        if all([all(row) for row in self.board]):
            self.show_tie_message()

    def show_win_message(self, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        self.root.destroy()

    def show_tie_message(self):
        messagebox.showinfo("Game Over", "Tie game!")
        self.root.destroy()

    def play(self):
        self.root.mainloop()

game = TicTacToe()
game.play()
