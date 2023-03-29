from abc import ABC, abstractmethod


class AbstractEntity(ABC):

    def __repr__(self):
        return f'<{__class__.__name__}>'
