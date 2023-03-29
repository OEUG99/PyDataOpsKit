from PyDataOpsKit import AbstractDatabaseStrategy

class DatabaseManager:

    def __init__(self, strategy: AbstractDatabaseStrategy):
        self.strategy = strategy

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
