from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def create_table(self):
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
    def get_all(self):
        """Get all objects from the repository."""
        pass
