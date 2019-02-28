from enum import Enum
from observer.publisher import Publishable
from flight.subscribers import FlightSubscriber, NewsletterSubscriber
from utils.states import Stateable

DEFAULT_SUBSCRIPTION = [FlightSubscriber, NewsletterSubscriber]


class User:
    """
    User of airline
    """

    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.name = name
        self.subscriptions = self._init_subscription()

    def _init_subscription(self):
        for subscription in DEFAULT_SUBSCRIPTION:
            yield subscription(self.uid)

    def update(self):
        for subscription in self.subscriptions:
            subscription.update()


class Flight(Publishable, Stateable):

    class States(Enum):
        ON_TIME = 'on_time'
        CANCELLED = 'cancelled'
        DELAYED = 'delayed'

    state = States.ON_TIME
    states = States

    def __init__(self, number: str, airline: str, **kwargs):
        self.number = number
        self.airline = airline
        super().__init__()

    def __repr__(self):
        return 'Flight %s manipulated by airline %s is %s' % self.number, self.airline, self.state

    def _change_state(self, state: States.member_type):
        # todo change state maybe property?
        self.state = state
        self.notify()

    def notify(self):
        for subscriber in self._subscribers.values():
            subscriber.update(self)


class Newsletter(Publishable):
    """
    Newsletter domain model
    """

    def __init__(self, letter: str=None, **kwargs):
        self.letter = letter
        super().__init__()

    def __repr__(self):
        return '%s' % self.letter

    def create_letter(self, message: str):
        """
        Notify always when new letter is created
        :param message: message in the letter
        :return:
        """
        self.letter = message
        self.notify()

    def notify(self):
        """
        Notify all subscribers
        :return: None
        """
        for subscriber in self._subscribers.values():
            subscriber.update(self)
