import tkinter as tk
from tkinter import messagebox
import random

# Initialize
root = tk.Tk()
root.geometry("300x500")

# Ask the question
play_with_computer = messagebox.askyesno("Game Mode", "Do you want to play against the computer?")

if play_with_computer:
    print("User chose to play against computer.")
    root.title("Tic Tac Toe - User vs Computer")
else:
    print("User chose 2-player mode.")
    root.title("Tic Tac Toe - 2-Player Mode")

# Create a variable to store and update the game status text
status_text = tk.StringVar()
status_text.set("Player X's turn")

# Create status_label to display whose turn it is
status_label = tk.Label(root, textvariable=status_text, font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3, pady=10)

# Initialize the button grid and game state matrix
buttons = [[None for i in range(3)] for i in range(3)]  # Stores button objects
status = [["" for i in range(3)] for i in range(3)]  # Stores game state ("X", "O", or "")

print(buttons)

# Use a list for current_player to make it mutable in functions
current_player = ["X"]


def win_or_lose(status):
    """
    Check if any player has won the game
    Returns: "X" or "O" if a player has won, None otherwise
    """
    for i in range(3):
        # Check rows
        if status[i][0] == status[i][1] == status[i][2] != "":
            return status[i][0]
        # Check columns
        if status[0][i] == status[1][i] == status[2][i] != "":
            return status[0][i]
    # Check diagonals
    if status[0][0] == status[1][1] == status[2][2] != "":
        return status[0][0]
    if status[0][2] == status[1][1] == status[2][0] != "":
        return status[0][2]
    return None

def end_game():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def check_game_end():
    result = win_or_lose(status)
    # Check for win condition
    result = win_or_lose(status)
    if result is not None:
        messagebox.showinfo(title='Congratulations', message=f'Player {result} win this game')
        end_game()
        return True
    # Check for tie condition (all cells filled)
    if all(cell != "" for row in status for cell in row):
        messagebox.showinfo(title='Game Over', message='It is a tie')
        end_game()
        return True
    return False


def on_button_click(r, c):
    """
    Handle button click events
    Parameters:
        r (int): Row index of the clicked button
        c (int): Column index of the clicked button
    """
    button = buttons[r][c]
    # Only process click if the cell is empty
    if button["text"] == "":
        # Update button text with current_player's symbol
        button["text"] = current_player[0]
        # Update game state and switch player
        if current_player[0] == "X":
            status[r][c] = "X"
            current_player[0] = "O"
            if check_game_end():
                return
            if position == 1:
                computer_move()
        else:
            status[r][c] = "O"
            current_player[0] = "X"
            if check_game_end():
                return
            if position == 0:
                computer_move()
        # Update status display for next player
        status_text.set(f"Player {current_player[0]}'s turn")
        print(status)

    else:
        # Display warning if cell is already occupied
        messagebox.showwarning("Not available", "This box have been occupied")

def computer_move():
    available_buttons = [btn for row in buttons for btn in row if btn["text"] == ""]
    if available_buttons:
        random.choice(available_buttons).invoke()

# Create the game board with 3x3 grid of buttons
for row in range(3):
    # Configure row weights for grid layout
    root.grid_rowconfigure(row, weight=1)
    for col in range(3):
        # Configure column weights for grid layout
        root.grid_columnconfigure(col, weight=1)
        # Create button with command that captures current row and column values
        button = tk.Button(root, text="",
                           width=7, height=7,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        # Store button reference in the buttons matrix
        buttons[row][col] = button

if play_with_computer:
    # Judge the computer is first or second
    position = random.randint(0, 1)
    if position == 0:
        computer_move()

# Start the main event loop
root.mainloop()