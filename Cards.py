import random

class Card(object):
    """Create a card base on rank and suit"""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["S","C","H","D"]

    def __init__(self, rank:str, suit:str, isFaceUp = True):
        self.rank = rank
        self.suit = suit
        self.card = (rank, suit)
        self.isFaceUp = isFaceUp

    def __str__(self):
        if self.isFaceUp:
            output = self.rank + "-" + self.suit
            return output
        else:
            return "XX"

    def flipCard(self):
        if self.isFaceUp:
            self.isFaceUp = False
        else:
            self.isFaceUp = True


class Hand(object):
    """This creates a hand of cards"""

    def __init__(self):
        """creates an empty hand"""
        self.cards = []

    def __str__(self):
        if len(self.cards) == 0:
            return "<Empty Hand>"
        output = ""
        for card in self.cards:
            output += "[" +card.__str__() + "] "
        return output

    def addCard(self,card:Card):
        """This will add a card to the hand"""
        self.cards.append(card)

    def giveCard(self, card:Card, otherHand):
        """removes card from current hand
        to add to other hand"""
        if card in self.cards:
            otherHand.addCard(card)
            self.cards.remove(card)
        else:
            print("can't give that card")

    def getCard(self, rank, suit):
        """return a card from the hand of a given
        rank and suit: None otherwise"""
        for card in self.cards:
            if card.rank == rank and card.suit == suit:
                return card
        return None

    def clearCards(self):
        """remove all cards from hand"""
        self.cards = []


h = Hand()
otherHand = Hand()
h.addCard(Card("9","D"))
h.addCard(Card("J","D"))
print(h)
h.giveCard(h.getCard("J","C"), otherHand)
print(h)
print(otherHand)
h.clearCards()
print(h)








