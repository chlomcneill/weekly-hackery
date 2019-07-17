from random import randint

ratings = {
    'Norway': 1915,
    'Australia': 2003,
    'England': 2049,
    'Cameroon': 1499,
    'France': 2043,
    'Brazil': 1944,
    'Spain': 1913,
    'USA': 2101,
    'Italy': 1868,
    'China': 1866,
    'Netherlands': 1967,
    'Japan': 1991,
    'Germany': 2072,
    'Nigeria': 1599,
    'Sweden': 1962,
    'Canada': 2006
}


def match_probability(team1rating, team2rating):
    return float(1 / (1 + 10 ** ((team2rating - team1rating) / 400)))


# print(match_formula(1711, 1785))

def rating_change(rating, result, expected):
    return round(float(rating + 60 * (result - expected)), 0)


# print(rating_change(ratings['USA'], 1, match_formula(ratings['Ghana'], ratings['USA'])))


def play_match(team1, team2):
    probability = match_probability(ratings[team1], ratings[team2])
    rand = randint(0, 100) / 100
    if rand < probability:
        winner = team1
        team1newrating = rating_change(ratings[team1], 1, probability)
        return winner, team1newrating
    else:
        winner = team2
        team2newrating = rating_change(ratings[team2], 1, (1-probability))
        return winner, team2newrating


def update_rating(team, newrating):
    ratings[team] = newrating


def round1():
    game1winner, winner1newrating = play_match('Norway', 'Australia')
    game2winner, winner2newrating = play_match('England', 'Cameroon')
    game3winner, winner3newrating = play_match('France', 'Brazil')
    game4winner, winner4newrating = play_match('Spain', 'USA')
    game5winner, winner5newrating = play_match('Italy', 'China')
    game6winner, winner6newrating = play_match('Netherlands', 'Japan')
    game7winner, winner7newrating = play_match('Germany', 'Nigeria')
    game8winner, winner8newrating = play_match('Sweden', 'Canada')
    round1winners = {game1winner: winner1newrating, game2winner: winner2newrating, game3winner: winner3newrating, game4winner: winner4newrating,
                     game5winner: winner5newrating, game6winner: winner6newrating, game7winner: winner7newrating, game8winner: winner8newrating}
    for winner in round1winners:
        update_rating(winner, round1winners[winner])
    return game1winner, game2winner, game3winner, game4winner, game5winner, game6winner, game7winner, game8winner


def quarter_finals():
    g1, g2, g3, g4, g5, g6, g7, g8 = round1()
    game9winner, winner9newrating = play_match(g1, g2)
    game10winner, winner10newrating = play_match(g3, g4)
    game11winner, winner11newrating = play_match(g5, g6)
    game12winner, winner12newrating = play_match(g7, g8)
    quarterfinalwinners = {game9winner: winner9newrating, game10winner: winner10newrating, game11winner: winner11newrating, game12winner: winner12newrating}
    for winner in quarterfinalwinners:
        update_rating(winner, quarterfinalwinners[winner])
    return game9winner, game10winner, game11winner, game12winner


def semi_finals():
    g9, g10, g11, g12 = quarter_finals()
    game13winner, winner13newrating = play_match(g9, g10)
    game14winner, winner14newrating = play_match(g11, g12)
    semifinalwinners = {game13winner: winner13newrating, game14winner: winner14newrating}
    for winner in semifinalwinners:
        update_rating(winner, semifinalwinners[winner])
    return game13winner, game14winner


def final():
    g13, g14 = semi_finals()
    game15winner, winner15newrating = play_match(g13, g14)
    return game15winner


# print(final())


def main():
    results = {}
    count = 0
    for i in range(101):
        winner = final()
        if winner not in results:
            results[winner] = 1
            count += 1
        else:
            results[winner] += 1
            count += 1
    for result in results:
        print(result + ': ' + str(round(results[result]/count, 2)*100) + '%')


main()


