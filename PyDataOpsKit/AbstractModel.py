import json
from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @abstractmethod
    def toDict(self) -> dict:
        """
        Returns a dictionary representation of the object.
        """
        pass

    def toJSON(self):
        """Returns a JSON representation of the object"""
        return json.dumps(self.toDict())

    def __repr__(self):
        return f'<{__class__.__name__}>'
