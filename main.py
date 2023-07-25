import random

def print_board(board):
    print("   1   2   3")
    print("A  " + " | ".join(board[0]))
    print("  ---+---+---")
    print("B  " + " | ".join(board[1]))
    print("  ---+---+---")
    print("C  " + " | ".join(board[2]))

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def bot_move(board):
    # This bot makes a random move by choosing an empty cell on the board.
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    against_bot = input("Do you want to play against a bot? (yes/no): ").lower() == "yes"
    
    for turn in range(9):
        player_symbol = players[current_player]
        print(f"Player {player_symbol}'s turn.")
        
        if current_player == 1 and against_bot:
            row, col = bot_move(board)
        else:
            while True:
                move = input("Enter your move (e.g., A1, B2, C3): ").upper()

                if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
                    print("Invalid move. Try again.")
                else:
                    row = ord(move[0]) - ord("A")
                    col = int(move[1]) - 1

                    if board[row][col] == " ":
                        break
                    else:
                        print("That cell is already taken. Try again.")

        board[row][col] = player_symbol
        print_board(board)

        if check_winner(board, player_symbol):
            print(f"Player {player_symbol} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()
