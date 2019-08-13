import random
import itertools


def deck():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    cards = list(itertools.product(ranks, suits))
    return cards


def deal_a_card(deck):
    card = deck.pop(random.randint(0, len(deck)))
    return card, deck


def discard_a_card(deck):
    deck.pop(random.randint(0, len(deck)))
    return deck


def deal_to_players(num_of_players):
    cards = deck()
    hands = []
    for i in range(1, num_of_players + 1):
        first_card, cards = deal_a_card(cards)
        second_card, cards = deal_a_card(cards)
        hands.append([i, first_card, second_card])
    return hands, cards


def deal_to_table(cards):
    table = []
    cards = discard_a_card(cards)
    for i in range(3):
        card, cards = deal_a_card(cards)
        table.append(card)
    cards = discard_a_card(cards)
    card, cards = deal_a_card(cards)
    table.append(card)
    cards = discard_a_card(cards)
    card, cards = deal_a_card(cards)
    table.append(card)
    return table, cards


def play(num_of_players):
    hands, cards = deal_to_players(num_of_players)
    table, cards = deal_to_table(cards)
    return hands, table, len(cards)


print(play(3))

