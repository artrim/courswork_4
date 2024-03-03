from abc import ABC, abstractmethod


class GetApi(ABC):

    @abstractmethod
    def get_api(self, keyword):
        pass
