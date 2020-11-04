from datetime import datetime
import json


class Task:
    """
    Task Object class.

    Creates task model.
    """
    def __init__(self, name="Task", description="Task description",
                 completed=False, date_creation=datetime.now(), date_edition=None):
        """Task initializer.

        :param name: Task name.
        :param description: Task description.
        :param completed: Task completion.
        :param date_creation: Date of object creation(default - now).
        :param date_edition:

        :return: Task.
        """
        self.__name = name
        self.__description = description
        self.__date_creation = date_creation
        self.__date_edition = date_edition
        self.__completed = completed

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
    def description(self):
        """
        Description getter.
        """
        return self.__description

    @description.setter
    def description(self, value):
        """
        Description setter.
        :param value: Description to be set.
        """
        if value:
            self.__description = value
            self.__date_edition = datetime.now()
        else:
            raise Exception("Wrong value")

    @property
    def completed(self):
        """
        Completion getter.
        """
        return self.__completed

    @completed.setter
    def completed(self, value):
        """
        Completion setter.
        :param value: Completion to be set.
        """
        if value:
            self.__completed = bool(value)
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
        :return: Task info in json format
        """
        data = {
            "name": self.__name,
            "description": self.__description,
            "completed": self.__completed,
            "date_creation": str(self.__date_creation),
            "date_edition": str(self.__date_edition)
        }
        return json.dumps(data)

    def db(self):
        """
        Makes db arguments from object
        :return: List with task info
        """
        data=[self.__name,self.__description,self.__completed,self.__date_creation,self.__date_edition]
        return data