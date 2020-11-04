import psycopg2

class BaseDAO:
    """
    Basic Data Object class.

    Does database connection and disconnection.
    """

    def open(self):
        """Connecnts to database

        :return: Database cursor
        """
        self.conn = psycopg2.connect(dbname='tasktrackerdb', user='admin1',
                                password='admin', host='localhost')
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        return self.cursor

    def close(self):
        """Closes connection to database
        """
        self.cursor.close()
        self.conn.close()




