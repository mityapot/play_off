import collections
import random

team_list = ['FC Barcelona', 'Real Madrid', 'Liverpool FC', 'Manchester United', 'CSKA Moskva', 'Werder Bremen',
             'Arsenal FC', 'Bayern Munchen',
             'Chelsea FC', 'Spartak Moskva', 'Glasgow Rangers', 'Legia Warszawa', 'Olympique Lyonnais', 'IFK Mariehamn',
             'Riga FC', 'PAOK Thessalonikis']

Game = collections.namedtuple('Game', ['first_team', 'second_team', 'score_ft', 'score_sd', 'round_n'])

one_eights = []
one_fourth = []
one_half = []
final = []
round_list = [one_eights, one_fourth, one_half, final]

round_str = {
    0: '1/8',
    1: '1/4',
    2: '1/2',
    3: 'final',
}


def correct_team():
    offer_enter = 'Enter team from list: '
    team_input = input(offer_enter)
    while team_input not in team_list:
        print('ERROR!!! No such team')
        team_input = input(offer_enter)
    return team_input


def different_random(random_score):
    diff = random.randint(0, 20)
    while diff == random_score:
        diff = random.randint(0, 20)
    return diff


def winners(first_game, second_game):
    if first_game.score_ft > first_game.score_sd:
        winner_1 = first_game.first_team
    else:
        winner_1 = first_game.second_team
    if second_game.score_ft > second_game.score_sd:
        winner_2 = second_game.first_team
    else:
        winner_2 = second_game.second_team
    return winner_1, winner_2


def play_games():
    random.shuffle(team_list)
    for i in range(0, len(team_list), 2):
        rand_score = random.randint(0, 20)
        one_eights.append(Game(team_list[i], team_list[i + 1], rand_score, different_random(rand_score), round_str[0]))
    for i in range(1, len(round_list)):
        round_previous = round_list[i - 1]
        round_current = round_list[i]
        for j in range(0, len(round_list[i - 1]), 2):
            first_game = round_previous[j]
            second_game = round_previous[j + 1]
            winner1, winner2 = winners(first_game, second_game)
            rand_score = random.randint(0, 20)
            round_current.append(Game(winner1, winner2, rand_score, different_random(rand_score), round_str[i]))


def print_team_result(game):
    print('Round', game.round_n, ':', game.first_team, '-', game.second_team, ' ', game.score_ft, ':', game.score_sd)


def search_team_result(team):
    is_in_round = 0
    for round_current in round_list:
        for game in round_current:
            if team in game:
                is_in_round = 1
                print_team_result(game)
                break
        if is_in_round == 0:
            break


if __name__ == '__main__':
    print(team_list)
    play_games()
    question = "Do you want to input team results [y/n]?"
    answer = input(question)
    while answer == 'y':
        team = correct_team()
        search_team_result(team)
        answer = input(question)
