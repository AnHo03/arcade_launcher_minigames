# script module

import sys
import random
import time

def guess_number(name):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    win_percentage = 100

    def play_guess():
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal win_percentage
    

        playerchoice = input(f'Choose a number between 1 and 5 {name}\n\n')
        if playerchoice not in ['1', '2', '3', '4', '5']:
            print(f'Please choose a number between 1 and 5 {name}')
            return play_guess()

        player = int(playerchoice)

        computerchoice = random.choice('12345')

        computer = int(computerchoice)

        print(f'You choose {player}, I choose {computer}')
        
        def decide_winner(player, computer):
            nonlocal game_count
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal win_percentage

            if player == computer:
                player_wins += 1
                return f'{name}, You win!😀'

            else:
                computer_wins += 1
                return f'{name}, you loose 😭\n'
        
        gameresult = decide_winner(player, computer)
        print(gameresult)

        game_count += 1

        win_percentage = round(player_wins/game_count*100,2)

        print(f'game count:{game_count}, Wins:{player_wins}, losses:{computer_wins}, Win percentage {win_percentage}%\n')

        print(f'play again {name}? choose y for yes or n for no')
        
        while True:
            playagain = input().lower()
            if playagain.lower() not in ['y','n']:
                print('choose y for yes or n for no')
                continue
            else:
                break

        if playagain.lower() == "y":
                return play_guess()
        else:
            print('goodbye')
            if __name__ == '__main__':
                time.sleep(3)
                sys.exit
            else:
                time.sleep(3)
                return

        return guess_number()

    play_guess()

def set_up_game():
    print('Welcome to Guess my number')

    name = input('please choose your name:')
    if not name:
        name = 'Player01'
    return name

if __name__ == "__main__":
    name = set_up_game()
    guess_number()

