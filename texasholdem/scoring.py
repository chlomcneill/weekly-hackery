ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


def get_hand_ranks(hand):
    hand_ranks = []
    for card in hand:
        hand_ranks.append(card.rank)
    return hand_ranks


def get_hand_suits(hand):
    hand_suits = []
    for card in hand:
        hand_suits.append(card.suit)
    return hand_suits


def is_straight(hand):
    hand_ranks = get_hand_ranks(hand)
    hand_ranks.sort(key=lambda x: ranks.index(x))
    if ranks.index(hand_ranks[1]) == ranks.index(hand_ranks[0])+1 and ranks.index(hand_ranks[2]) == ranks.index(hand_ranks[1])+1 and ranks.index(hand_ranks[3]) == ranks.index(hand_ranks[2])+1 and ranks.index(hand_ranks[4]) == ranks.index(hand_ranks[3])+1:
        return True
    elif hand_ranks == ['2', 'Jack', 'Queen', 'King', 'Ace']:
        return True
    elif hand_ranks == ['2', '3', 'Queen', 'King', 'Ace']:
        return True
    elif hand_ranks == ['2', '3', '4', 'King', 'Ace']:
        return True
    elif hand_ranks == ['2', '3', '4', '5', 'Ace']:
        return True
    else:
        return False


def is_flush(hand):
    hand_suits = get_hand_suits(hand)
    if all(x == hand_suits[0] for x in hand_suits):
        return True
    else:
        return False


def contains_only_one_pair(hand):
    hand_ranks = get_hand_ranks(hand)
    count = [hand_ranks.count(rank) for rank in list(dict.fromkeys(hand_ranks))]
    count.sort()
    if count == [1, 1, 1, 2]:
        return True
    else:
        return False


def contains_three_of_a_kind(hand):
    hand_ranks = get_hand_ranks(hand)
    count = [hand_ranks.count(rank) for rank in list(dict.fromkeys(hand_ranks))]
    count.sort()
    if count == [1, 1, 3]:
        return True
    else:
        return False


def contains_two_pairs(hand):
    hand_ranks = get_hand_ranks(hand)
    count = [hand_ranks.count(rank) for rank in list(dict.fromkeys(hand_ranks))]
    count.sort()
    if count == [1, 2, 2]:
        return True
    else:
        return False


def is_full_house(hand):
    hand_ranks = get_hand_ranks(hand)
    count = [hand_ranks.count(rank) for rank in list(dict.fromkeys(hand_ranks))]
    count.sort()
    if count == [2, 3]:
        return True
    else:
        return False


def contains_four_of_a_kind(hand):
    hand_ranks = get_hand_ranks(hand)
    count = [hand_ranks.count(rank) for rank in list(dict.fromkeys(hand_ranks))]
    count.sort()
    if count == [1, 4]:
        return True
    else:
        return False


def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False


def is_royal_flush(hand):
    hand_ranks = get_hand_ranks(hand)
    royal_flush = ['Ace', 'King', 'Queen', 'Jack', '10']
    if set(hand_ranks) == set(royal_flush) and is_flush(hand):
        return True
    else:
        return False


def high_card(hand):
    hand_ranks = get_hand_ranks(hand)
    hand_ranks.sort(key=lambda x: ranks.index(x))
    return hand_ranks[-1]


def score_hand(hand):
    if is_royal_flush(hand):
        return 10, None
    elif is_straight_flush(hand):
        return 9, high_card(hand)
    elif contains_four_of_a_kind(hand):
        return 8, high_card(hand)
    elif is_full_house(hand):
        return 7, high_card(hand)
    elif is_flush(hand):
        return 6, high_card(hand)
    elif is_straight(hand):
        return 5, high_card(hand)
    elif contains_three_of_a_kind(hand):
        return 4, high_card(hand)
    elif contains_two_pairs(hand):
        return 3, high_card(hand)
    elif contains_only_one_pair(hand):
        return 2, high_card(hand)
    else:
        return 1, high_card(hand)