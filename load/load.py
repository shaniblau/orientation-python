from abc import ABC, abstractmethod


class Load(ABC):

    @staticmethod
    @abstractmethod
    def load(data):
        pass
