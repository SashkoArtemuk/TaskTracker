from flask import request
from flask_restful import Resource
import json

from Models.Task import Task
from DAO.TaskDAO import TaskDAO


class TaskController:
    """
    Task Controller class.

    Defines api for tasks.
    """

    def __init__(self, api):
        """
        Task Controller initializer.

        :param api: Flask api.

        :return: An instance of Task Controller class initialized with api and routing.
        """
        self.api = api
        self.api.add_resource(self.AddTask, '/task/add/<int:board_id>')
        self.api.add_resource(self.GetTasks, '/task/get_all/<int:board_id>')
        self.api.add_resource(self.GetTask, '/task/get/<int:id>')
        self.api.add_resource(self.EditTask, '/task/edit/<int:id>')
        self.api.add_resource(self.DeleteTask, '/task/delete/<int:id>')

    class AddTask(Resource):
        def put(self, board_id):
            """Adds new task to specific board(by board id)

            Handles 'put' requests on route /task/add/<board_id> with parameters:
             - 'name'
             - 'description'
             - 'completed'

            in request data\n
            Example:
             - put('http://localhost:5000/task/add/5', data={'name': 'Task 1',
                'description': "Create TaskTracker api",'completed': False})

            :param board_id: Id of board for task to be added.

            :return: Id of created task.
            """
            task = Task(request.form['name'], request.form['description'], request.form['completed'])
            task_dao = TaskDAO()
            id = task_dao.AddTask(task, board_id)
            return {'id': id}

    class GetTasks(Resource):
        def get(self, board_id):
            """Gets all tasks from specific board(by board id)

            Handles 'get' requests on route /task/get_all/<board_id>\n
            Example:
             - get('http://localhost:5000/task/get_all/1')

            :param board_id: Id of board for tasks to be got.

            :return: Json response with tasks(id: task).
            """
            task_dao = TaskDAO()
            tasks = task_dao.GetTasks(board_id)
            dataset = {}
            for el in tasks:
                task = Task(el[1], el[2], el[3], el[4], el[5])
                dataset[el[0]] = json.loads(task.json())
            return dataset

    class GetTask(Resource):
        def get(self, id):
            """Gets task(by task id)

            Handles 'get' requests on route /task/get/<id>\n
            Example:
             - get('http://localhost:5000/task/get/2')

            :param id: Id of task to be got.

            :return: Json response with task(id: task) or error response if id is wrong.
            """
            task_dao = TaskDAO()
            sql_task = task_dao.GetTask(id)
            if sql_task:
                task = Task(sql_task[1], sql_task[2], sql_task[3], sql_task[4], sql_task[5])
                return {id: json.loads(task.json())}
            else:
                return "Error(incorrect id)"

    class EditTask(Resource):
        def put(self, id):
            """Edits task(by task id)

            Handles 'put' requests on route /task/edit/<id> with OPTIONAL parameters:
             - 'name'
             - 'description'
             - 'completed'

            in request data\n
            Example:
             - put('http://localhost:5000/task/edit/2',
                data={'name': 'Edited name', 'completed': True})

            :param board_id: Id of board for task to be edited.

            :return: Success or error if id is wrong
            """
            task_dao = TaskDAO()
            sql_task = task_dao.GetTask(id)
            if sql_task:
                task = Task(sql_task[1], sql_task[2], sql_task[3], sql_task[4], sql_task[5])
                if "name" in request.form:
                    task.name = request.form['name']
                if "description" in request.form:
                    task.description = request.form['description']
                if "completed" in request.form:
                    task.completed = request.form['completed']
                task_dao.EditTask(task, id)
                return "Success"
            else:
                return "Error(incorrect id)"

    class DeleteTask(Resource):
        def put(self, id):
            """Deletes task(by task id)

            Handles 'put' requests on route /task/delete/<id>\n
            Example:
             - put('http://localhost:5000/task/delete/2')

            :param id: Id of task to be deleted.

            :return: Success(even if task doesn't exist)
            """
            task_dao = TaskDAO()
            task_dao.DeleteTask(id)
            return "Success"