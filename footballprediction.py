## A program that asks user to predict who wins or the correct score of a match

import math
import random

matches = [
    {"Manchester United": 0, "Chelsea": 0}, {'Real madrid': 0, 'Arsenal': 0},
    {'Benfica': 0, 'Barcelona': 0}
]

straight_win = []
correct_score = []
win = []
correct_score_prediction = {}

def predict():
    game = False;
    user_choice = input('Prediction option: press 12 for [straight win] and press "cs" for [correct score]: ')
    if user_choice == '12':
        play_straight_win()
    elif user_choice.lower() == 'cs':
        play_correct_score()

def play_straight_win():
    play_match()
    straight_win_prediction()
    game = check_straight_win_game()
    display_result()
    if game:
        print('Congratulations, You won')
    else:
        print('You lost!!!')

def play_correct_score():
    play_match()
    correct_score()
    display_correct_score_result()
    if(check_correct_win_game()):
        print('Congratulation, You won')
    else:
        print('You lost!!!')

def straight_win_prediction():
    print('\nPREDICT WINNER BY SELECTING 1[HOME] or 2[AWAY]: ')
    for match in matches:
        card = []
        for team in match:
            if len(card) % 2 == 1:
                card.append(' vs ')
            card.append(team)
        user_prediction = int(input(' '.join(card) + ': '))
        card.remove(' vs ')
        winner = user_prediction - 1 ## index of 0
        straight_win.append(winner)

## I would have to create an alternate dictionary of the existing teams with the predicted score
def correct_score():
    i = 0
    print('PRESS - TO IGNORE A TEAM: ')
    for match in matches:
        for team in match:
            score = input('Enter correct score for {}: '.format(team))
            if score == '-':
                continue
            else:
                correct_score_prediction[team] = int(score)


def play_match():
    for match in matches:
        for team in match:
            match[team] = random.randint(0, 15)

def display_result():
    result = []
    count = 0
    print('\n')
    for match in matches:
        for team in match:
            if len(result) % 2 == 1:
                result.append(' : ')
            result.append('{} ({})'.format(team, match[team]))
        result.append('\t\t[{}]\n'.format(win[count]))
        count += 1
    print(' '.join(result))


def display_correct_score_result():
    result = []
    count = 0
    print('\n')

    for match in matches:
        for team in match:
            result.append('{} {} ({})'.format(team, ':', match[team]))
            if team in correct_score_prediction:
                result.append('\t\t{} ({}) \t[{}]\n\n'.format(team, correct_score_prediction[team], win[count]))
            else:
                result.append('\n\n')
        count += 1
    print(' '.join(result))

def check_straight_win_game():
    i = 0
    index = 0

    for match in matches:
        game = []   ## store scores between teams
        for team in match:
            game.append(int(match[team]))

        index = straight_win[i]
        score = game[index]

        if game[0] == game[1]: ## check for draw
            win.append('draw')
        elif(score == max(game)):
            win.append('win')
        else:
            win.append('lost')
        i += 1
    
    for game_result in win:
        if game_result == 'lost':
            return False
    
    return True

def check_correct_win_game():
    i = 0
    team_predicted_score = []

    for match in matches:
        for team in match:
            if team in correct_score_prediction:
                if match[team] == correct_score_prediction[team]:
                    win.append('win')
                else:
                    win.append('lost')
    
    for game_result in win:
        if game_result == 'lost':
            return False
    return True

predict()