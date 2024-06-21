import numpy as np

def check_win(board, user_value):
    for i in range(3):
        if np.all(board[i] == user_value) or np.all(board[:, i] == user_value):
            return True
    if np.all(np.diag(board) == user_value) or np.all(np.diag(np.fliplr(board)) == user_value):
        return True
    return False

def is_draw(board):
    return np.all(board != " ")

def print_board(board):

    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def game_starts():
    board = np.full((3, 3), " ")
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")
    current_player = player1
    current_value = 'x'
    
    while True:
        print(f"\n{current_player}'s turn:")
        print_board(board)
        
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == " ":
                        board[row][col] = current_value
                        break
                    else:
                        print("That spot is already occupied. Try again.")
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter valid integers for row and column.")

        if check_win(board, current_value):
            print_board(board)
            print(f"\n{current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        if current_player == player1:
            current_player = player2
            current_value = 'o'
        else:
            current_player = player1
            current_value = 'x'

if __name__ == "__main__":
    print("WELCOME TO TIC-TAC-TOE")
    play1 = input("Are you ready to play (yes/no): ").lower()
    if play1 == "yes":
        game_starts()
    else:
        print("You chose not to play")
