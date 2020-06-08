#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

        # starting location is the key and
        # the destination is the value

    def __repr__(self):
        return f'source: {self.source}, destination: {self.destination}'


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    trip = {}
    route = []

    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    next = trip['NONE']

    while next != 'NONE':
        route.append(next)
        next = trip[next]

    route.append('NONE')

    return route

# output an array of strings with the entire route of
# your trip.

#  `source` string represents the starting airport and the
# `destination` string represents the next airport along our trip
# The ticket for your first flight has a destination with a `source` of
# `NONE`
# ticket for your final flight has a `source` with a
# `destination` of `NONE`. 


