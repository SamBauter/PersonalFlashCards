class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
        self.learned = False
        self.seen = False

    def front(self):
        return self.term

    def back(self):
        return self.definition

    def set_learned(self):
        self.learned = True

    def set_seen(self):
        self.seen = True

