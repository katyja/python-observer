from enum import Enum
from observer.publisher import Publishable
from observer.subscriber import Subscriber
from utils.states import Stateable


class Flight(Publishable, Stateable):

    class States(Enum):
        ON_TIME = 'on_time'
        CANCELLED = 'cancelled'
        DELAYED = 'delayed'

    _subscriber = {}
    state = States.ON_TIME
    states = States

    def __init__(self, number: str, airline: str, **kwargs):
        self.number = number
        self.airline = airline
        super().__init__()

    def __repr__(self):
        return 'Flight %s manipulated by airline %s is %s' % (self.number, self.airline, self.state.value)

    def change_state(self, state: States):
        # todo change state maybe to property
        self.state = state
        self._notify()

    # todo decorator
    def _notify(self):
        for subscriber in self._subscribers.values():
            subscriber.update(self)


class Newsletter(Publishable):
    """
    Newsletter domain model
    """

    _subscriber = {}

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
        self._notify()

    def _notify(self):
        """
        Notify all subscribers
        :return: None
        """
        for subscriber in self._subscribers.values():
            subscriber.update(self)


class User(Subscriber):
    """
    User of airline
    """
    # todo review default for newsletter
    default_subscription = [Newsletter]

    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.name = name
        # self._init_subscription()

    # def _init_subscription(self):
    #     for subscription in self.default_subscription:
    #         subscription.subscribe(self)

    # todo: update - send email? no callback
    def update(self, publisher):
        # email to
        print('Email for {}: {}'.format(self.name, publisher))
