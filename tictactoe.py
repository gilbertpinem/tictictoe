def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_player_move(board, player):
    while True:
        move = input(f"{player}, enter a number (1-9) to make your move: ")
        if move.isdigit() and int(move) in range(1, 10):
            index = int(move) - 1
            if board[index] == ' ':
                return index
        print("Invalid move, please try again.")

def check_for_winner(board):
    for i in range(0,3,9):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

def play_game():
    board = [' '] * 9
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        move = get_player_move(board, players[current_player])
        board[move] = players[current_player]
        if check_for_winner(board):
            print_board(board)
            print(f"{players[current_player]} wins!")
            break
        if ' ' not in board:
            print_board(board)
            print("Tie game!")
            break
        current_player = (current_player + 1) % 2

play_game()
