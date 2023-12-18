import tkinter as tk

# Create the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth+1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth+1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    max_eval = float("-inf")
    best_move_index = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > max_eval:
                max_eval = eval
                best_move_index = i
    return best_move_index

# Function to make the AI move
def make_ai_move(board):
    move = best_move(board)
    if move is not None:
        board[move] = "O"

# Function to handle player's move
def player_move(index):
    if board[index] == " ":
        board[index] = "X"
        update_gui()

        if check_win(board, "X"):
            result_label.config(text="You win! Congrats!")
            disable_buttons()
        elif " " not in board:
            result_label.config(text="It's a tie!")
            disable_buttons()
        else:
            make_ai_move(board)
            update_gui()

            if check_win(board, "O"):
                result_label.config(text="AI wins! Better luck next time.")
                disable_buttons()
            elif " " not in board:
                result_label.config(text="It's a tie!")
                disable_buttons()

# Function to disable buttons after game ends
def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Function to update the GUI board
def update_gui():
    for i in range(9):
        buttons[i]["text"] = board[i]

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                       command=lambda i=i: player_move(i))
    buttons.append(button)
    buttons[i].grid(row=i // 3, column=i % 3)

# Create a label for game results
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=3, columnspan=3)

# Run the Tkinter event loop
root.mainloop()
