from abc import ABC, abstractmethod


class Extract(ABC):

    @staticmethod
    @abstractmethod
    def extract():
        pass
