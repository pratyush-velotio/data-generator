from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, *args, **kwargs):
        pass  

    @abstractmethod
    def write(self, data, output_file):
        pass

    @abstractmethod
    def read(self, input_file):
        pass
