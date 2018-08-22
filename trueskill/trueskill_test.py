from trueskill import TrueSkill
ENV = TrueSkill(mu=25.0, sigma=25.0/3)

def make_ratings(amount):
    return [(ENV.create_rating(),) for _ in range(amount)]

def update_elo(ratings):
    ranks = [x for x in range(len(ratings))]
    new_ratings = ENV.rate(ratings, ranks)
    print(new_ratings)
    return new_ratings

def print_ratings(ratings):
    for x in ratings:
        print(x)

    print("\n\n")

iterations = 1
player_count = 13
ratings = make_ratings(player_count)
for _ in range(iterations):
    ratings = update_elo(ratings)

# print(sum(map(lambda r: r[0].mu, ratings))/player_count)
print_ratings(ratings)
