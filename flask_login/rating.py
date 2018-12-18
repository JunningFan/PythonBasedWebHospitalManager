class Rating():
    def __init__(self):
        self._ratings = []
        self._customers = []
    def makeRating(self, customer, score):
        if not score:
            raise ValueError
        try:
            self._ratings[self._customers.index(customer.get_id())] = score
        except ValueError:
            self._customers.append(customer.get_id())
            self._ratings.append(score)

    def get_average(self):
        if self._ratings:
            print(self._ratings)
            return sum(self._ratings)/len(self._ratings)
        return 'No ratings'

    def get_previous_rating(self, customer):
        try:
            return self._ratings[self._customers.index(customer.get_id())]
        except ValueError:
            return None
