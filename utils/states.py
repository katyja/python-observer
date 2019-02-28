import abc
from enum import Enum


class Stateable(abc.ABC):
    """
    Abstract class for states
    """
    class States(Enum):
        pass

    @property
    @abc.abstractproperty
    def states(self):
        return self.States
