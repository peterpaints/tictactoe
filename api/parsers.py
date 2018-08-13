from flask_restful import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('board', required=True,
                                  help="Please provide a valid board")
