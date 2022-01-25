import random
import Card


class Deck:
    def __init__(self, cards):
        self.cards = []
        for card in cards:
            self.cards.append(card)
        self.seen_cards = []
        self.learned_card = []

    def draw(self):
        return self.cards[0]

    def learn(self, front=True):
        while self.cards:
            card = self.draw()
            side = card.front() if front else card.back()
            print(side)
            ready_check = 'N'
            while ready_check != 'Y':
                ready_check = input("Are you ready to flip the card?")
            other_side = card.back() if front else card.front()
            card.set_seen()
            self.cards.remove(card)
            self.seen_cards.append(card)
            print(other_side)
            learn_check = input("See this card again?")
            if learn_check == 'N':
                card.set_learned()
                self.learned_card.append(card)
            else:
                self.cards.append(card)
        print("There are no more cards")

    def shuffle(self):
        random.shuffle(self.cards)

    def add(self, card):
        self.cards.append(card)

    def delete(self, card):
        self.cards.remove(card)


test_deck = Deck([Card.Card("mammal", "furry animal"),
                  Card.Card("fish", "scaly swimmer"),
                  Card.Card("reptile", "scaly dino like"),
                  Card.Card("amphibian", "slimy froglike")
                  ])
