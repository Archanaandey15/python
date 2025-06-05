board = [" " for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(player):
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for line in win:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

def play():
    turn = "X"
    for i in range(9):
        print_board()
        move = int(input(f"Player {turn}, choose 1-9: ")) - 1
        if board[move] != " ":
            print("That spot is taken!")
            continue
        board[move] = turn
        if check_win(turn):
            print_board()
            print(f"🎉 Player {turn} wins!")
            return
        turn = "O" if turn == "X" else "X"
    print_board()
    print("It's a draw!")

play()