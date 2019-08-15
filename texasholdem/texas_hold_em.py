import random
import itertools
from texasholdem.scoring import score_hand


ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


def deal_a_card(deck):
    card = deck.pop(random.randint(0, len(deck)-1))
    return card, deck


def discard_a_card(deck):
    deck.pop(random.randint(0, len(deck)-1))
    return deck


def deal_to_players(num_of_players):
    deck = list(itertools.product(ranks, suits))
    hands = []
    for i in range(1, num_of_players + 1):
        first_card, deck = deal_a_card(deck)
        second_card, deck = deal_a_card(deck)
        hands.append([i, first_card, second_card])
    return hands, deck


def flop(deck):
    table = []
    deck = discard_a_card(deck)
    for i in range(3):
        card, deck = deal_a_card(deck)
        table.append(card)
    return table, deck


def turn(table, deck):
    deck = discard_a_card(deck)
    card, deck = deal_a_card(deck)
    table.append(card)
    return table, deck


def river(table, deck):
    deck = discard_a_card(deck)
    card, deck = deal_a_card(deck)
    table.append(card)
    return table, deck


def get_possible_hands(table, player_hand):
    cards = [player_hand[1], player_hand[2]]
    hands = []
    combinations = list(itertools.combinations(table, 3))
    # print(combinations)
    for combo in combinations:
        hands.append(cards + list(combo))
    return hands


def best_player_hand(table, player_hand):
    possible_hands = get_possible_hands(table, player_hand)
    # print(possible_hands)
    scores = []
    for hand in possible_hands:
        scores.append([hand, score_hand(hand)[0], score_hand(hand)[1]])
    # print(scores)
    scores.sort(key=lambda x: x[1])
    if len(scores) == 1:
        best_hand = scores[0]
    else:
        if scores[-1][1] != scores[-2][1]:
            best_hand = scores[-1]
        else:
            highest_ranks = [score[1] == scores[-1][1] for score in scores]
            highest_ranks.sort(key=lambda x: ranks.index(x))
            if highest_ranks[0][2] == 'Ace':
                best_hand = highest_ranks[0]
            else:
                best_hand = highest_ranks[-1]
    return best_hand[0], best_hand[1]


def get_player_scores(table, player_hands):
    scores = {}
    for player_hand in player_hands:
        best_hand, score = best_player_hand(table, player_hand)
        scores[player_hand[0]] = [best_hand, score]
    return scores  # {player_number: best_hand, score_of_best_hand}


def play(num_of_players):
    hands, cards = deal_to_players(num_of_players)
    table, cards = flop(cards)
    scores = get_player_scores(table, hands)
    table, cards = turn(table, cards)
    table, cards = river(table, cards)
    return hands, table, scores


print(play(3))
# print(get_possible_hands([('10', 'Clubs'), ('8', 'Clubs'), ('7', 'Hearts'), ('Jack', 'Spades')], [1, ('King', 'Hearts'), ('5', 'Spades')]))
# print(best_player_hand([('10', 'Clubs'), ('8', 'Clubs'), ('7', 'Hearts'), ('Jack', 'Spades')], [1, ('King', 'Hearts'), ('5', 'Spades')]))
# print(best_player_hand([('10', 'Clubs'), ('8', 'Clubs'), ('Queen', 'Hearts'), ('Jack', 'Spades')], [1, ('King', 'Hearts'), ('9', 'Spades')]))
