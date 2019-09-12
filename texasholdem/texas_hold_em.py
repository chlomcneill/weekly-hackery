from texasholdem.data_model import Deck, Player
from texasholdem.scoring import get_hand_ranks


ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def flop(deck):
    deck.discard_card()
    table = [deck.deal_card(), deck.deal_card(), deck.deal_card()]
    return table


def turn(table, deck):
    deck.discard_card()
    table.append(deck.deal_card())
    return table


def river(table, deck):
    deck.discard_card()
    table.append(deck.deal_card())
    return table


def high_card(hand):
    hand_ranks = get_hand_ranks(hand)
    hand_ranks.sort(key=lambda x: ranks.index(x))
    return hand_ranks[-1]


def winning_hand(table, players):
    player_scores = get_player_scores(table, players)
    if player_scores[-1][1] != player_scores[-2][1]:
        winning_hand = player_scores[-1]
    else:
        highest_ranks = [score[2] == player_scores[-1][2] for score in player_scores]
        highest_ranks.sort(key=lambda x: high_card(x[1])) #TODO: tie break
        winning_hand = highest_ranks[-1]
        # winning_hand = tie_break(drawing_player_scores)
    return winning_hand


def get_player_scores(table, players):
    scores = []
    for player in players:
        best_hand, score = player.best_hand(table)
        scores.append([player.name, best_hand, score])
    scores.sort(key=lambda x: x[2])
    return scores  # [player_number, best_hand, score_of_best_hand]


def play():
    deck = Deck()
    deck.shuffle()
    player1 = Player('1')
    player2 = Player('2')
    player3 = Player('3')
    players = [player1, player2, player3]
    for player in players:
        player.draw(deck)
    table = flop(deck)
    table = turn(table, deck)
    table = river(table, deck)
    winner = winning_hand(table, players)
    print("The winner is Player " + winner[0] + " with the hand " + str(winner[1]))


play()
