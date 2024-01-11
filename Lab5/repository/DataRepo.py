from abc import ABC,abstractmethod

class DataRepo(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def save(self):
       pass


    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_to_file(self, string):
        pass

    @abstractmethod
    def convert_to_string(self):
        pass

    @abstractmethod
    def convert_from_string(self, filename, string):
        pass