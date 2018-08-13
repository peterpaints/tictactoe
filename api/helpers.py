previous_board = []

def is_space_free(board_list):
    for line in board_list:
        for char in line:
            return char == ' '

def is_game_start(board_list):
    characters = []
    for line in board_list:
        for char in line:
            if char != ' ':
                characters.append(char)
    if len(characters) < 2:
        return characters
    else:
        return False

def players_move(previous_board, board_list):
    for line in board_list:
        for new_line in previous_board:
            if set(line) != set(new_line):
                return list(set(line) - set(new_line))
    return False
