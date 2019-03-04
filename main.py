from flight.models import Flight, Newsletter, User


def example():
    flight = Flight('AD9062', 'Austrian')
    news = Newsletter()

    peter = User(325390, 'Peter Rob')
    johny = User(325391, 'Johny Cash')
    jane = User(325392, 'Jane Richardson')

    flight.subscribe_all([peter, johny, jane])
    news.subscribe(johny)

    flight.change_state(Flight.States.CANCELLED)
    # sends notifications to Peter, Johny & Jane

    news.create_letter('We have 50% sale on trips to LA!')
    # sends notifications to Johny

example()
