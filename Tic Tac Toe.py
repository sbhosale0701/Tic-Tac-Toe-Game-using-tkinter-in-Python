import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.buttons = []
        self.board = [" " for _ in range(9)]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Create buttons
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", width=10, height=5,
                                   command=lambda x=i, y=j: self.click_button(x, y))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # Create restart button
        restart_button = tk.Button(self.window, text="Restart", width=20, height=2, command=self.restart)
        restart_button.grid(row=3, column=1, columnspan=2)

    def start(self):
        self.window.mainloop()

    def click_button(self, x, y):
        if self.board[x*3 + y] == " ":
            self.buttons[x][y].config(text=self.current_player)
            self.board[x*3 + y] = self.current_player
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                self.restart()
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "Tie game!")
                self.restart()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check rows
        for i in range(3):
            if self.board[i*3:i*3+3] == [self.current_player]*3:
                return True
        # Check columns
        for i in range(3):
            if self.board[i::3] == [self.current_player]*3:
                return True
        # Check diagonals
        if self.board[0::4] == [self.current_player]*3 or self.board[2:8:2] == [self.current_player]*3:
            return True
        return False

    def check_tie(self):
        return " " not in self.board

    def restart(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    game = TicTacToe()
    game.start()
