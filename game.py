game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_flag = True

def display_board(sells):
    result = create_row(sells[0:3]) + "\n-----------\n" + create_row(sells[3:6]) + "\n-----------\n" + create_row(sells[6:9])
    return result

def create_row(sells_in_row):
    return f"   |   |   \n {sells_in_row[0]} | {sells_in_row[1]} | {sells_in_row[2]} \n   |   |   "

def change_sell_value(board, sell, symbol):
    board[sell - 1] = symbol
    return board

def check_for_legal_turn(board, sell):
    return board[sell - 1] == ' '

def select_symbol():
    if player_flag:
        return 'X'
    else:
        return 'O'

def create_turn():
    global player_flag
    print(display_board(game_board))
    print(f"Player {select_symbol()} turn!")
    sell = int(input("select sell for your turn"))
    if check_for_legal_turn(game_board, sell):
        symbol = select_symbol()
        change_sell_value(game_board, sell, symbol)
        player_flag = not player_flag

def check_for_rows():
    return game_board[0] == game_board[1] == game_board[2] and game_board[0] != ' ' \
    or game_board[3] == game_board[4] == game_board[5] and game_board[3] != ' ' \
    or game_board[6] == game_board[7] == game_board[8] and game_board[6] != ' '

def check_for_columns():
    return game_board[0] == game_board[3] == game_board[6] and game_board[0] != ' ' \
           or game_board[1] == game_board[4] == game_board[7] and game_board[1] != ' ' \
           or game_board[2] == game_board[5] == game_board[8] and game_board[2] != ' '

def check_for_diagonals():
    return game_board[0] == game_board[4] == game_board[8] and game_board[4] != ' ' \
           or  game_board[2] == game_board[4] == game_board[6] and game_board[4] != ' '

def check_for_win():
    return check_for_columns() or check_for_rows() or check_for_diagonals()

def lets_the_game_begin():
    global player_flag
    print("Begin Game!")
    while not check_for_win():
        create_turn()
    player_flag = not player_flag
    print(f"player {select_symbol()} win!")

lets_the_game_begin()