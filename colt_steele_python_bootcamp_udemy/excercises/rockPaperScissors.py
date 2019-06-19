import os
import time
import random

player1 = None
player2 = None
choices = ['rock', 'paper', 'scissors']


def cls():
    return os.system('cls') if os.name == 'nt' else os.system('clear')


def init_player_choice(player):
    while True:
        cls()
        globals()[player] = input(f'rock / paper / scissors, choose {player} >  ')
        if globals()[player] in choices:
            print('okay, good luck')
            time.sleep(1)
            break
        print('enter exact rock / paper / scissors please.')
        time.sleep(1)


def init_ai():
    ai = input(f'''
    Do you want to play vs AI?
    type yes if you want
    ''')
    if ai.lower() == 'yes':
        global player2
        player2 = choices[random.randint(0, 3)]
        return True


def return_winner():
    game_key = {('paper', 'rock'): True,
                ('paper', 'scissors'): False,
                ('rock', 'paper'): False,
                ('rock', 'scissors'): True,
                ('scissors', 'paper'): True,
                ('scissors', 'rock'): False}
    # true if player 1 wins, false otherwise
    try:
        return game_key[(player1, player2)]
    except KeyError:
        return 'draw'


init_player_choice('player1')
if not init_ai():
    init_player_choice('player2')

winner = return_winner()
if winner == 'draw':
    print('A draw, try again lad')
else:
    print(f"The winner is {'player1' if winner else 'player2'}")
