# write your code here
import random


def print_board(board_to_print):
    print("---------")
    for print_i in range(3):
        print("|", end=" ")
        for print_j in range(3):
            print(board_to_print[print_i][print_j], end=" ")
        print("|")
    print("---------")


def check_win(player):
    for func_i in range(3):
        if (board[func_i][0] == player and board[func_i][1] == player and board[func_i][2] == player) \
                or (board[0][func_i] == player and board[1][func_i] == player and board[2][func_i] == player) \
                or (board[0][0] == player and board[1][1] == player and board[2][2] == player)\
                or (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return True
    return False


def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def is_input_correct(command_params):
    if command_params[0] != "start" \
            and (command_params[1] != "user" or command_params[1] != "easy") \
            and (command_params[2] != "user" or command_params[2] != "easy"):
        return False
    return True


def create_board():
    play_board = []
    for i in range(3):
        play_board.append([])
        for j in range(3):
            play_board[i].append(' ')
    return play_board


def check_row(sign, *row):
    if row[0] == sign and row[1] == sign and row[2] == ' ':
        return 2
    elif row[0] == sign and row[2] == sign and row[1] == ' ':
        return 1
    elif row[1] == sign and row[2] == sign and row[0] == ' ':
        return 0
    else:
        return -1


def user_move(sign):
    coords_str = input("Enter the coordinates:").split(" ")
    if (not coords_str[0].isdigit()) or (not coords_str[1].isdigit()):
        print("You should enter numbers!")
        return
    coord_x = int(coords_str[0])
    coord_y = int(coords_str[1])
    if coord_x < 1 or coord_x > 3 or coord_y < 1 or coord_y > 3:
        print("Coordinates should be from 1 to 3!")
        return
    coord_x -= 1
    coord_y -= 1
    if board[coord_x][coord_y] != ' ':
        print("This cell is occupied! Choose another one!")
        return
    board[coord_x][coord_y] = sign


def easy_move(sign):
    is_finish = False
    while not is_finish:
        x_coord = random.randint(0, 2)
        y_coord = random.randint(0, 2)
        if board[x_coord][y_coord] == ' ':
            board[x_coord][y_coord] = sign
            is_finish = True
        else:
            continue


def get_enemy_sign(sign):
    if sign == 'X':
        return 'O'
    else:
        return 'X'


def possible_medium_move(sign, is_enemy):
    sign_to_check = sign if (not is_enemy) else get_enemy_sign(sign)
    check_result = check_row(sign_to_check, board[0][0], board[1][1], board[2][2])
    if check_result != -1:
        board[check_result][check_result] = sign
        return True

    check_result = check_row(sign_to_check, board[0][2], board[1][1], board[2][0])
    if check_result != -1:
        board[0 + check_result][2 - check_result] = sign
        return True

    for i in range(3):
        check_result = check_row(sign_to_check, board[i][0], board[i][1], board[i][2])
        if check_result != -1:
            board[i][check_result] = sign
            return True
        check_result = check_row(sign_to_check, board[0][i], board[1][i], board[2][i])
        if check_result != -1:
            board[check_result][i] = sign
            return True

    return False


def medium_move(sign):
    if possible_medium_move(sign, False):
        return
    elif possible_medium_move(sign, True):
        return
    else:
        easy_move(sign)


def avail(minimax_board):
    new_board = []
    for cell in minimax_board:
        if cell != 'X' and cell != 'O':
            new_board.append(cell)
    return new_board


def check_win_minimax(minimax_board, player):
    if ((minimax_board[0] == player and minimax_board[1] == player and minimax_board[2] == player) or
            (minimax_board[3] == player and minimax_board[4] == player and minimax_board[5] == player) or
            (minimax_board[6] == player and minimax_board[7] == player and minimax_board[8] == player) or
            (minimax_board[0] == player and minimax_board[3] == player and minimax_board[6] == player) or
            (minimax_board[1] == player and minimax_board[4] == player and minimax_board[7] == player) or
            (minimax_board[2] == player and minimax_board[5] == player and minimax_board[8] == player) or
            (minimax_board[0] == player and minimax_board[4] == player and minimax_board[8] == player) or
            (minimax_board[2] == player and minimax_board[4] == player and minimax_board[6] == player)
    ):
        return True
    else:
        return False


def minimax(minimax_board, player, ai_player, hu_player):
    new_board = avail(minimax_board)
    if check_win_minimax(minimax_board, hu_player):
        return {"score": -10}
    elif check_win_minimax(minimax_board, ai_player):
        return {"score": 10}
    elif len(new_board) == 0:
        return {"score": 0}
    moves = []
    for i in range(len(new_board)):
        move = {}
        move.update({"index": minimax_board[new_board[i]]})
        minimax_board[new_board[i]] = player
        if player == ai_player:
            g = minimax(minimax_board, hu_player, ai_player, hu_player)
            move.update({"score": g["score"]})
        else:
            g = minimax(minimax_board, ai_player, ai_player, hu_player)
            move.update({"score": g["score"]})
        minimax_board[new_board[i]] = move["index"]
        moves.append(move)

    if player == ai_player:
        best_score = -10000
        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_score = moves[i]["score"]
                best_move = i
    else:
        best_score = 10000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_score = moves[i]["score"]
                best_move = i
    return moves[best_move]


def hard_move(sign):
    minimax_board = []
    index = 0
    ai_player = sign
    hu_player = toggle_sign(sign)
    for row in board:
        for cell in row:
            if cell == ' ':
                minimax_board.append(index)
            else:
                minimax_board.append(cell)
            index += 1
    move_index = minimax(minimax_board, ai_player, ai_player, hu_player)["index"]
    board[int(move_index / 3)][move_index % 3] = sign


def player_move(player, sign):
    if player == "easy":
        print('Making move level "easy"')
        easy_move(sign)
    elif player == "medium":
        print("Making move level 'medium'")
        medium_move(sign)
    elif player == "hard":
        print("Making move level 'hard'")
        hard_move(sign)
    elif player == "user":
        user_move(sign)


def toggle_player(player):
    global first_user, second_user
    if player is first_user:
        return second_user
    if player is second_user:
        return first_user


def toggle_sign(sign):
    if sign == 'X':
        return 'O'
    if sign == 'O':
        return 'X'


while True:
    input_command = input("Input command: ")
    if input_command == "exit":
        break
    command_params = input_command.split(" ")
    if len(command_params) != 3 or not is_input_correct(command_params):
        print("Bad parameters!")
        continue
    board = create_board()
    print_board(board)
    first_user = command_params[1]
    second_user = command_params[2]
    is_end = False
    current_player = first_user
    current_sign = 'X'
    while not is_end:
        player_move(current_player, current_sign)
        print_board(board_to_print=board)
        if check_win(current_sign):
            print(current_sign, "wins")
            is_end = True
        elif check_draw():
            print("Draw")
            is_end = True
        else:
            current_player = toggle_player(current_player)
            current_sign = toggle_sign(current_sign)
    if is_end:
        break
