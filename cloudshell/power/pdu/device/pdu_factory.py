from abc import ABCMeta
from abc import abstractmethod


class PDUFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_outlets(self):
        """
        :return: list(Outlet)
        """
        pass

    @abstractmethod
    def get_inventory(self):
        pass