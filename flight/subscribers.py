from observer.subscriber import Subscriber


class FlightSubscriber(Subscriber):
    """
    Subscriber - update on flight status
    """

    def __init__(self, uid):
        self.uid = uid

    def update(self, publisher):
        print(publisher)


class NewsletterSubscriber(Subscriber):
    """
    Subscriber - update about news
    """

    def __init__(self, uid):
        self.uid = uid

    def update(self, publisher):
        print(publisher)
