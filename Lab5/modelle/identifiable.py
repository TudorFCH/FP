from abc import ABC, abstractmethod
class Identifiable(ABC):

    @abstractmethod
    def __init__(self, id):
        self.id = id