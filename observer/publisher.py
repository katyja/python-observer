import abc


class Publishable(abc.ABC):
    """
    Abstract class (interface) to implement subjects/publishers for observing

    Note:
        The subscribers are implemented as dictionary. The uid should be unique
    """

    def __init__(self):
        self._subscribers = {}

    def subscribe(self, subscriber):
        """
        Add subscriber based on uid

        :param subscriber:
        :return:
        """
        self._subscribers[subscriber.uid] = subscriber

    def unsubscribe(self, subscriber):
        """
        Remove subscriber
        :param subscriber:
        :return:
        """
        self._subscribers.pop(subscriber.uid)

    @abc.abstractmethod
    def notify(self):
        """
        Notify all subscribers
        :return:
        """
        pass
