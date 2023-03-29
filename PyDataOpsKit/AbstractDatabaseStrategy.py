from abc import ABC, abstractmethod


class AbstractDatabaseStrategy(ABC):

    """
    This is the abstract class for the database connection strategy.
    It defines the interface for the concrete strategies.
    It allows for hot swap-ability of databases at runtime!
    For example, you can have a MySQLConnectionStrategy and a PostgreSQLConnectionStrategy.
    or you can have a DB for prod and a DB for dev.
    """

    @abstractmethod
    def connect(self):
        """
        This method should return a connection object for the given database.
        """
        pass

    @abstractmethod
    def close(self):
        """
        This method should close the connection object for the given database.
        """
        pass

    @abstractmethod
    def query(self, query, params=None):
        """
        This method should execute a query on the given database.
        """
        pass
