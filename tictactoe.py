def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'.\n")
    print_board(board)

    current_player = "X"

    while True:
        try:
            print(f"Player {current_player}'s turn.")
            row = int(input("Enter the row (1, 2, or 3): ")) - 1
            col = int(input("Enter the column (1, 2, or 3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid input! Please choose a row and column between 1 and 3.")
                continue
            if board[row][col] != " ":
                print("This spot is already taken. Choose a different one.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Congratulations! Player {current_player} wins!")
                break
            if is_draw(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()
