import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.current_player = ''
        self.player1_name = ''
        self.player2_name = ''
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_main_menu()

    def create_main_menu(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)

        tk.Label(main_frame, text="Tic Tac Toe", font=('Arial', 24)).grid(row=0, columnspan=2, pady=10)
        tk.Button(main_frame, text="Single Player", font=('Arial', 16), command=self.setup_single_player_game).grid(row=1, column=0, padx=10)
        tk.Button(main_frame, text="Two Players", font=('Arial', 16), command=self.setup_two_players_game).grid(row=1, column=1, padx=10)

    def setup_single_player_game(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe - Single Player")

        setup_frame = tk.Frame(self.root)
        setup_frame.pack(pady=20)

        tk.Label(setup_frame, text="Enter your name: ", font=('Arial', 16)).grid(row=0, column=0)
        self.player1_name_entry = tk.Entry(setup_frame, font=('Arial', 16))
        self.player1_name_entry.grid(row=0, column=1, padx=10)

        tk.Label(setup_frame, text="Choose your symbol: ", font=('Arial', 16)).grid(row=1, column=0)
        self.symbol_var = tk.StringVar()
        self.symbol_var.set('X')
        tk.Radiobutton(setup_frame, text='X', font=('Arial', 16), variable=self.symbol_var, value='X').grid(row=1, column=1)
        tk.Radiobutton(setup_frame, text='O', font=('Arial', 16), variable=self.symbol_var, value='O').grid(row=1, column=2)

        tk.Button(setup_frame, text="Start Game", font=('Arial', 16), command=self.start_single_player_game).grid(row=2, columnspan=3, pady=10)

    def setup_two_players_game(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe - Two Players")

        setup_frame = tk.Frame(self.root)
        setup_frame.pack(pady=20)

        tk.Label(setup_frame, text="Enter Player 1's name: ", font=('Arial', 16)).grid(row=0, column=0)
        self.player1_name_entry = tk.Entry(setup_frame, font=('Arial', 16))
        self.player1_name_entry.grid(row=0, column=1, padx=10)

        tk.Label(setup_frame, text="Enter Player 2's name: ", font=('Arial', 16)).grid(row=1, column=0)
        self.player2_name_entry = tk.Entry(setup_frame, font=('Arial', 16))
        self.player2_name_entry.grid(row=1, column=1, padx=10)

        tk.Button(setup_frame, text="Start Game", font=('Arial', 16), command=self.start_two_players_game).grid(row=2, columnspan=2, pady=10)

    def start_single_player_game(self):
        self.player1_name = self.player1_name_entry.get() or "Player"
        self.player2_name = "Computer"

        self.current_player = self.symbol_var.get()
        self.root.destroy()
        self.create_game_board()

    def start_two_players_game(self):
        self.player1_name = self.player1_name_entry.get() or "Player 1"
        self.player2_name = self.player2_name_entry.get() or "Player 2"

        self.current_player = 'X'
        self.root.destroy()
        self.create_game_board()

    def create_game_board(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.status_var = tk.StringVar()
        self.status_var.set(f"Current Turn: {self.player1_name}")

        status_label = tk.Label(self.root, textvariable=self.status_var, font=('Arial', 16))
        status_label.pack(pady=10)

        game_frame = tk.Frame(self.root)
        game_frame.pack()

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(game_frame, text='', font=('Arial', 20), width=6, height=3,
                                               command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                winner = self.player1_name if self.current_player == 'X' else self.player2_name
                messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
                self.ask_play_again()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.ask_play_again()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.update_status()

                if self.player2_name == "Computer" and self.current_player == 'O':
                    self.computer_move()

    def update_status(self):
        if self.current_player == 'X':
            self.status_var.set(f"Current Turn: {self.player1_name}")
        else:
            self.status_var.set(f"Current Turn: {self.player2_name}")

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        row, col = random.choice(empty_cells)
        self.click(row, col)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def ask_play_again(self):
        if messagebox.askyesno("Tic Tac Toe", "Do you want to play again?"):
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'
        self.update_status()

        if self.player2_name == "Computer" and self.current_player == 'O':
            self.computer_move()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
