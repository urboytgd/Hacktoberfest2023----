def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 13)

def is_valid_location(board, col):
    return board[0][col] == ' '

def drop_piece(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return

def check_win(board, piece):
    # Check horizontal locations
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations
    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check diagonal (positive slope)
    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check diagonal (negative slope)
    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def main():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        display_board(board)

        # Ask for player input
        if turn == 0:
            col = int(input("Player 1's turn (0-6):"))
            piece = 'X'
        else:
            col = int(input("Player 2's turn (0-6):"))
            piece = 'O'

        if is_valid_location(board, col):
            drop_piece(board, col, piece)
            if check_win(board, piece):
                display_board(board)
                print(f"Player {piece} wins!")
                game_over = True
            turn += 1
            turn %= 2

if __name__ == '__main__':
    main()
