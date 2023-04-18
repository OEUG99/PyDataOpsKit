import os
from typing import TypeVar

from . import AbstractDatabaseStrategy
from .MySQLStrategy import MySQLStrategy


T = TypeVar('T', bound=AbstractDatabaseStrategy)

class DatabaseManager:
    def __init__(self, strategy: T = None):
        if strategy is not None:
            self.strategy = strategy

        if os.environ.get("ENVIRONMENT") == "PRODUCTION":
            pass
        elif os.environ.get("ENVIRONMENT") == "DEVELOPMENT":
            pass
        elif os.environ.get("ENVIRONMENT") == "TESTING":
            pass
        else:
            self.strategy = MySQLStrategy(os.getenv("MYSQL_IP"),
                                          3306,
                                          "root",
                                          os.getenv("MYSQL_ROOT_PASSWORD"),
                                          os.getenv("MYSQL_DATABASE"))




    def setStrategy(self, strategy: AbstractDatabaseStrategy):
        """
        Set a new strategy for the database connection. Allowing for hot swap-ability of databases at runtime!
        :param strategy:
        :type strategy:
        :return:
        :rtype:
        """
        self.strategy = strategy

    def connect(self):
        self.strategy.connect()

    def close(self):
        self.strategy.close()

    def query(self, query, params=None):
        self.strategy.query(query, params)
