import abc


class Publishable(abc.ABC):
    """
    Abstract class (interface) to implement subjects/publishers for observing

    Note:
        The subscribers are implemented as dictionary. The uid should be unique
    """

    def __init__(self):
        self._subscribers = {}

    @property
    @abc.abstractmethod
    def _subscriber(self):
        return self._subscriber

    def subscribe_all(self, subscribers: list):
        """
        Add all subscribers based on uid

        :param subscribers:
        :return:
        """
        for subscriber in subscribers:
            self._subscribers[subscriber.uid] = subscriber

    def unsubscribe_all(self, subscribers: list):
        """
        Remove all subscribers based on uid

        :param subscribers:
        :return:
        """
        for subscriber in subscribers:
            self._subscribers.pop(subscriber.uid)

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
    def _notify(self):
        """
        Notify all subscribers
        :return:
        """
        pass
