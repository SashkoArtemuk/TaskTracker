from DAO.BaseDAO import BaseDAO
from datetime import datetime


class TaskDAO:
    """
    Task Data Access Object class.

    Creates interface for db actions with tasks
    """

    @staticmethod
    def AddTask(task, board_id=1):
        """Adds task to DB

        :param board_id: Board id to which the task belongs

        :return: Id of created task.
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """INSERT INTO tasks(name,description,completed,date_creation,date_edition,board_id) 
        VALUES(%s, %s, %s, %s, %s, %s) RETURNING id;"""
        task_db = task.db()
        task_db.append(board_id)
        cursor.execute(sql, task_db)
        result = cursor.fetchone()[0]
        dao.close()
        return result

    @staticmethod
    def GetTasks(board_id=1):
        """Get tasks from DB by board id

        :param board_id: Board id to which the tasks belongs

        :return: List with sql responses with tasks.
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """SELECT * FROM tasks WHERE board_id=%s ORDER BY id ASC"""
        cursor.execute(sql, [board_id])
        result = cursor.fetchall()
        dao.close()
        return result

    @staticmethod
    def GetTask(id=1):
        """Get specific task from DB by id

        :param id: Task id

        :return: Sql response with task
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """SELECT * FROM tasks WHERE id=%s"""
        cursor.execute(sql, [id])
        result = cursor.fetchone()
        dao.close()
        return result

    @staticmethod
    def EditTask(task, id=1):
        """Change specific task from DB by id

        :param task: Task object
        :param id: Task id
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """UPDATE tasks SET name = %s, description = %s, completed = %s, date_edition = %s WHERE id=%s"""
        cursor.execute(sql, (task.name, task.description, task.completed, datetime.now(), str(id)))
        dao.close()

    @staticmethod
    def DeleteTask(id=1):
        """Deletes task from DB by id

        :param id: Task id
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """DELETE FROM tasks WHERE id=%s"""
        cursor.execute(sql, [str(id)])
        dao.close()