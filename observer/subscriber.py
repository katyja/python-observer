import abc


class Subscriber(abc.ABC):
    """
    Base subscriber
    """

    @abc.abstractmethod
    def update(self, publisher):
        """
        update subscriber
        :param publisher:
        :return:
        """
        pass
