class Card():
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    suites = ["Diamonds", "Spades", "Hearts", "Clubs"]

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    # order is based on ranks first and if ranks match it goes off of suites.  they are
    # ordered by their respective position in the array.  
    def order(self):
        return self.ranks.index(self.rank) * 10 + self.suites.index(self.suite)

    def __lt__(self, other):
        return self.order() < other.order()

    def __le__(self, other):
        return self.order() <= other.order()

    def __eq__(self, other):
        return self.order() == other.order()

    def __ne__(self, other):
        return self.order() != other.order()

