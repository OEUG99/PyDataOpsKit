from abc import ABC, abstractmethod

from PyDataOpsKit.DatabaseManager import DatabaseManager


class AbstractRepository(ABC):

    def __init__(self):
        self.db = DatabaseManager()
        self.createTable()

    @abstractmethod
    def createTable(self):
        """Create the table for the repository."""
        pass

    @abstractmethod
    def add(self, obj):
        """Create a new object in the repository."""
        pass

    @abstractmethod
    def update(self, obj):
        """Update an existing object in the repository."""
        pass

    @abstractmethod
    def delete(self, obj):
        """Delete an object from the repository."""
        pass

    @abstractmethod
    def get(self, id):
        """Get an object from the repository by its ID."""
        pass

    @abstractmethod
    def getAll(self):
        """Get all objects from the repository."""
        pass

    @abstractmethod
    def getList(self, limit, offset=None):
        """Get all objects from the repository."""
        pass

    @abstractmethod
    def getCount(self):
        """Get the number of objects in the database."""
        pass

    @abstractmethod
    def getByAttribute(self, attribute):
        """Get an object from the repository by an attribute."""
        pass
