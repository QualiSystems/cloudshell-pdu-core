from abc import ABCMeta
from abc import abstractmethod

class Outlet:
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass
