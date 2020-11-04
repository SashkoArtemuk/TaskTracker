from flask import request
from flask_restful import Resource
import json

from DAO.BoardDAO import BoardDAO
from Models.Board import Board




class BoardController:

    """
    Board Controller class.

    Defines api for boards.
    """

    def __init__(self, api):
        """
        Board Controller initializer.

        :param api: Flask api.

        :return: An instance of Board Controller class initialized with api and routing.
        """

        self.api = api
        self.api.add_resource(self.AddBoard, '/board/add')
        self.api.add_resource(self.GetBoards, '/board/get_all')
        self.api.add_resource(self.GetBoard, '/board/get/<int:id>')
        self.api.add_resource(self.EditBoardName, '/board/edit/<int:id>')
        self.api.add_resource(self.DeleteBoard, '/board/delete/<int:id>')

    class AddBoard(Resource):
        def put(self):
            """Adds new board

            Handles 'put' requests on route /board/add with parameter 'name' in data\n
            Example:
             - put('http://localhost:5000/board/add', data={'name': 'Brand new board'})

            :return: Id of created board.
            """
            board = Board(request.form['name'])
            board_dao = BoardDAO
            id = board_dao.AddBoard(board)
            return {'id': id}

    class GetBoards(Resource):
        def get(self):
            """Get all boards

            Handles 'get' requests on route board/get_all\n
            Example:
             - get('http://localhost:5000/board/get_all')

            :return: Json response with all boards(id: board)
            """
            board_dao = BoardDAO
            boards = board_dao.GetBoards()
            dataset = {}
            for el in boards:
                board = Board(el[1], el[2], el[3])
                dataset[el[0]] = json.loads(board.json())

            return dataset

    class GetBoard(Resource):
        def get(self, id):
            """Get specific board(by id)

            Handles 'get' requests on board /board/get/<id>\n
            Example:
             - get('http://localhost:5000/board/get/5')

            :param id: Board id.

            :return: Json response with board (id: board) or error response if id is wrong
            """
            board_dao = BoardDAO()
            sql_board = board_dao.GetBoard(int(id))
            if sql_board:
                board = Board(sql_board[1], sql_board[2], sql_board[3])
                return {id: json.loads(board.json())}
            else:
                return "Error(incorrect id)"

    class EditBoardName(Resource):
        def put(self, id):
            """Change specific board's name(by id)

            Handles 'put' requests on route /board/edit/<id> with parameter 'name' in data\n
            Example:
             - put('http://localhost:5000/board/edit/1', data={'name': 'New name'})

            :param id: Board id.

            :return: Success(even if board doesn't exist).
            """
            board_dao = BoardDAO()
            board_dao.EditBoardName(id, request.form['name'])
            return "Success"

    class DeleteBoard(Resource):
        def put(self, id):
            """Deletes board(by id)

            Handles 'put' requests on route board/delete/ with parameter 'name' in data\n
            Example:
             - put('http://localhost:5000/board/delete/1')

            :param id: Board id.

            :return: Success(even if board doesn't exist)
            """
            board_dao = BoardDAO()
            board_dao.DeleteBoard(id)
            return "Success"
