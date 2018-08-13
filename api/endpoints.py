from flask import g, request, abort
from flask_restful import Resource
from api.parsers import pagination_arguments
from api.helpers import previous_board, is_space_free, is_game_start, players_move


class TicTacToe(Resource):

    @classmethod
    def get(cls):
        args = pagination_arguments.parse_args(request)
        board = args.get('board')
        if not board:
            abort(404, "Please provide a valid board")
        board_lines_list = board.strip().splitlines()
        board_list = map(lambda x: list(x.strip()), board_lines_list)
        possible_moves = []
        char_to_play = ""

        is_start = is_game_start(board_list)
        if is_start:
            if is_start[0] == 'x':
                char_to_play += 'y'
            else:
                char_to_play += 'x'

        else:
            still_in_play = is_space_free(board_list)
            if still_in_play and previous_board:
                if players_move(previous_board, board_list)[0] == 'x':
                    char_to_play += 'y'
                else:
                    char_to_play += 'x'
