import random
from texasholdem.scoring import score_hand
import itertools


ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Card:
    """A standard playing card."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return self.rank + ' of ' + self.suit

    def __cmp__(self, other):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        if ranks.index(self.rank) < ranks.index(other.rank):
            return -1
        elif ranks.index(self.rank) == ranks.index(other.rank):
            return 0
        return 1

    def show(self):
        print(self.__repr__())


class Deck:
    """Represents a standard deck of playing cards, without Jokers."""

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def show(self):
        for card in self.cards:
            card.show()

    def count(self):
        print(len(self.cards))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def discard_card(self):
        self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __repr__(self):
        return {'name': self.name, 'hand': self.cards}

    def draw(self, deck):
        for i in range(2):
            self.cards.append(deck.deal_card())

    def show(self):
        for card in self.cards:
            card.show()

    def best_hand(self, table):

        def get_possible_hands(cards, table):
            hands = []
            combinations = list(itertools.combinations(table, 3))
            for combo in combinations:
                hands.append(cards + list(combo))
            return hands

        possible_hands = get_possible_hands(self.cards, table)
        scores = []
        for hand in possible_hands:
            scores.append([hand, score_hand(hand)[0], score_hand(hand)[1]])
        scores.sort(key=lambda x: x[1])
        if len(scores) == 1:
            best_hand = scores[0]
        else:
            if scores[-1][1] != scores[-2][1]:
                best_hand = scores[-1]
            else:
                highest_ranks = []
                for score in scores:
                    if score[1] == scores[-1][1]:
                        highest_ranks.append(score)
                highest_ranks.sort(key=lambda x: ranks.index(x[2])) #TODO: tie break
                best_hand = highest_ranks[-1]
        return best_hand[0], best_hand[1]