from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def operation(self):
        pass