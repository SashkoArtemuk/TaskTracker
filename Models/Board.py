from datetime import datetime
import json


class Board:
    """
    Board Object class.

    Creates board model.
    """

    def __init__(self, name="Board", date_creation=datetime.now(), date_edition=None):
        """Board initializer.

        :param name: Board name.
        :param date_creation: Date of object creation(default - now).
        :param date_edition:

        :return: Board.
        """
        self.__name = name
        self.__date_creation = date_creation
        self.__date_edition = date_edition

    @property
    def name(self):
        """
        Name getter.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Name setter.
        :param value: Name to be set.
        """
        if value:
            self.__name = value
            self.__date_edition = datetime.now()
        else:
            raise Exception("Wrong value")

    @property
    def date_creation(self):
        """
        Date creation getter.
        """
        return self.__date_creation

    @property
    def date_edition(self):
        """
        Date edition getter.
        """
        return self.__date_edition

    def json(self):
        """
        Makes json from object
        :return: Board info in json format
        """
        data = {
            "name": self.__name,
            "date_creation": str(self.__date_creation),
            "date_edition": str(self.__date_edition)
        }
        return json.dumps(data)

    def db(self):
        """
        Makes db arguments from object
        :return: List with board info
        """
        data=[self.__name,self.__date_creation,self.date_edition]
        return data
