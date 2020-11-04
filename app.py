from flask import Flask
from flask_restful import Api

from Controllers.TaskController import TaskController
from Controllers.BoardController import BoardController

app = Flask(__name__)
api = Api(app)

boards = BoardController(api)
tasks = TaskController(api)

if __name__ == '__main__':
    app.run(debug=True)
