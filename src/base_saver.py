from abc import ABC, abstractmethod


class BaseSaver(ABC):

    @abstractmethod
    def add_vacancy(self, file):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
