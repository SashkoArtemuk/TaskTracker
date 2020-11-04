from DAO.BaseDAO import BaseDAO
from datetime import datetime


class BoardDAO:
    """
    Board Data Access Object class.

    Creates interface for db actions with boards
    """

    @staticmethod
    def AddBoard(board):
        """Adds board to DB

        :param board: Board object

        :return: Id of created board.
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """INSERT INTO boards(name,date_creation,date_edition) VALUES(%s, %s, %s) RETURNING id;"""
        cursor.execute(sql, board.db())
        result = cursor.fetchone()[0]
        dao.close()
        return result

    @staticmethod
    def GetBoards():
        """Gets all boards from DB

        :return: List with sql response with boards ordered by id ascending
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """SELECT * FROM boards ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        dao.close()
        return result

    @staticmethod
    def GetBoard(id=1):
        """Gets specific board from DB

        :param id: Id of board to be got.

        :return: Sql resonse with board
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """SELECT * FROM boards WHERE id="""+str(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        dao.close()
        return result

    @staticmethod
    def EditBoardName(id=1, name="Name"):
        """Change name of specific board(by id) in DB

        :param id: Id of board to be changed.
        :param name: New name of board
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """UPDATE boards SET name = %s, date_edition = %s WHERE id=%s"""
        cursor.execute(sql,(name,datetime.now(),str(id)))
        dao.close()

    @staticmethod
    def DeleteBoard(id=1):
        """Deletes specific board from DB

        :param id: Id of board to be deleted.
        """
        dao = BaseDAO()
        cursor = dao.open()
        sql = """DELETE FROM boards WHERE id=%s"""
        cursor.execute(sql, [str(id)])
        dao.close()
