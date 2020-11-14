

class FuzzyString(str):

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __repr__(self):
        return repr(self.string)

    def __eq__(self, other):
        return self.string.lower() == other.lower()

    def __ne__(self, other):
        return self.string.lower() != other.lower()

    def __lt__(self, other):
        return self.string.lower() < other

    def __gt__(self, other):
        return self.string.lower() > other

    def __le__(self, other):
        return self.string.lower() <= other

    def __ge__(self, other):
        return self.string.lower() >= other
