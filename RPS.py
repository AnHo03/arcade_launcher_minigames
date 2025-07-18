import sys
import random
import time
from enum import Enum

MESSAGES = {
    'en': {
        'intro': "{name}, keep me happy while still staying morally sound. Try and make it to round 20!",
        'options': "Enter...\n1 for Rock,\n2 for Paper,\n3 for Jenah (Scissors lol),\n4 for God (instant win at a cost),\n5 for Prayer (fix your moral standing)",
        'invalid': "{name}, you must enter 1, 2, 3, 4, or 5.",
        'play_again': "Play again?\nY for Yes or Q to Quit",
        'win': "{name}, you win!🥳",
        'cheat': "{name}, you Cheated LOL",
        'saved': "{name}, your soul is saved! ... for now",
        'tie': "tie🪢",
        'wrecked': "{name}, Get Wrecked!😭",
        'love_wins': "Love conquers Evil",
        'halfway': "Halfway there!",
        'final_win': "You WIN it all! 🥳🥳🥳 Try and see how high you can get!",
        'fail_happy': "I cannot continue to watch you fail 😭",
        'fail_moral': "God is typing... I'm very disappointed in you.",
        'goodbye': "Thank you for playing. Goodbye {name}!",
        'choose_valid': "You must choose Y for yes or Q for quit.",
        'mom_chose': "Your mom chose",
        'game_count': "Game count",
        'wins': "Wins",
        'losses': "Losses",
        'ties': "Ties",
        'cheated': "Times Cheated",
        'happiness': "My happiness level",
        'morality': "Moral integrity",
        'original_name': "what's your name?"
    },
    'es': {
        'intro': "{name}, manténme feliz mientras conservas tu integridad moral. ¡Trata de llegar a la ronda 20!",
        'options': "Ingresa...\n1 para Piedra,\n2 para Papel,\n3 para Jenah (Tijeras jaja),\n4 para Dios (victoria instantánea con costo),\n5 para Oración (arregla tu integridad moral)",
        'invalid': "{name}, debes ingresar 1, 2, 3, 4 o 5.",
        'play_again': "¿Jugar otra vez?\nY para Sí o Q para Salir",
        'win': "¡{name}, ganaste!🥳",
        'cheat': "¡{name}, hiciste trampa LOL!",
        'saved': "¡{name}, tu alma fue salvada!... por ahora",
        'tie': "empate🪢",
        'wrecked': "¡{name}, destruido!😭",
        'love_wins': "El amor vence al Mal",
        'halfway': "¡Mitad del camino!",
        'final_win': "¡Ganaste todo! 🥳🥳🥳 ¡Intenta superar tu puntaje!",
        'fail_happy': "No puedo seguir viendo tu fracaso 😭",
        'fail_moral': "Dios está escribiendo... Estoy muy decepcionado de ti.",
        'goodbye': "Gracias por jugar. ¡Adiós {name}!",
        'choose_valid': "Debes elegir Y para sí o Q para salir.",
        'mom_chose': "Tu mamá eligió",
        'game_count': "Conteo de juegos",
        'wins': "Victorias",
        'losses': "Derrotas",
        'ties': "Empates",
        'cheated': "Veces que hiciste trampa",
        'happiness': "Mi nivel de felicidad",
        'morality': "Integridad moral",
        'original_name': "Elige tu idioma"

    }
}

labels = {
    'en': {1: 'Rock', 2: 'Paper', 3: 'Jenah', 4: 'God', 5: 'Prayer', 6: 'Evil'},
    'es': {1: 'Piedra', 2: 'Papel', 3: 'Jenah', 4: 'Dios', 5: 'Oración', 6: 'Mal'}
}

def RPS(name='PlayerOne', lang='en'):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie = 0
    cheater_lol = 0
    moral_integrity = 100
    happiness = 100

    def play_RPS():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie
        nonlocal cheater_lol
        nonlocal moral_integrity
        nonlocal happiness

        class RPS(Enum):
            Rock = 1
            Paper = 2
            Jenah = 3
            God = 4
            Evil = 6
            prayer = 5

        playerchoice = input(f"{MESSAGES[lang]['intro'].format(name=name)}\n{MESSAGES[lang]['options']}\n\n")

        if playerchoice not in ['1','2','3', '4', '5']:
            print(MESSAGES['invalid'].format(name=name))
            return play_RPS()

        player = int(playerchoice)

        computerchoice = random.choice('1236')

        computer = int(computerchoice)

        print(f"\n{name}, you chose {labels[lang][player]}.")
        print(f"{MESSAGES[lang]['mom_chose']} {labels[lang][computer]}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie
            nonlocal cheater_lol
            nonlocal moral_integrity
            nonlocal happiness

            if player == 1 and computer == 3:
                player_wins += 1
                happiness += 5
                moral_integrity += 5
                return MESSAGES[lang]['win'].format(name=name)

            elif player == 2 and computer == 1:
                player_wins += 1
                happiness += 5
                moral_integrity += 5
                return MESSAGES[lang]['win'].format(name=name)

            elif player == 3 and computer == 2:
                player_wins += 1
                happiness += 5
                moral_integrity += 5
                return MESSAGES[lang]['win'].format(name=name)
            
            elif player == 4 and computer in [1, 2, 3, 6]:
                cheater_lol += 1
                happiness += 20
                moral_integrity -= 25
                return MESSAGES[lang]['cheat'].format(name=name)
            
            elif player in [1,2] and computer == 6:
                computer_wins += 1
                happiness -= 25
                moral_integrity += 5
                return MESSAGES[lang]['wrecked'].format(name=name)
            
            elif player == 3 and computer == 6:
                player_wins += 1
                happiness += 25
                moral_integrity += 5
                return MESSAGES[lang]['love_wins'].format(name=name)
    
            elif player == computer:
                tie += 1
                moral_integrity += 5
                return MESSAGES[lang]['tie'].format(name=name)
            
            if player == 5:
                computer_wins +=1
                happiness -= 20
                moral_integrity += 25
                return MESSAGES[lang]['saved'].format(name=name)
            
            else:
                computer_wins += 1
                happiness -= 25
                moral_integrity += 5
                return MESSAGES[lang]['wrecked'].format(name=name)
        
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        if game_count - tie == 10:
            print(MESSAGES[lang]['halfway'])
        
        if game_count - tie == 20:
            print(MESSAGES[lang]['final_win'])
            time.sleep(3)
            

        happiness = min(happiness, 100)
        moral_integrity = min(moral_integrity, 100)

        print(f"\n{MESSAGES[lang]['game_count']}: {game_count}")
        print(f"{MESSAGES[lang]['wins']}: {player_wins}, {MESSAGES[lang]['losses']}: {computer_wins}, {MESSAGES[lang]['ties']}: {tie}, {MESSAGES[lang]['cheated']}: {cheater_lol}")
        print(f"{MESSAGES[lang]['happiness']}: {happiness}%")
        print(f"{MESSAGES[lang]['morality']}: {moral_integrity}%")


        if happiness < 50:
            print(MESSAGES[lang]['wrecked'])
        
        if happiness == 0:
            print(MESSAGES[lang]['fail_happy'])
            time.sleep(5)
            if __name__ == '__main__':
                time.sleep(3)
                sys.exit
            else:
                return
        
        if moral_integrity == 0:
            print(MESSAGES[lang]['fail_moral'])
            time.sleep(5)
            if __name__ == '__main__':
                time.sleep(3)
                sys.exit
            else:
                return

        print(f'\n{MESSAGES[lang]['play_again']}\n')
            
        while True:
            playagain = input().lower()
            if playagain.lower() not in ['y','q']:
                print(MESSAGES[lang]['choose_valid'])
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_RPS()
        else:
            print(MESSAGES[lang]['goodbye'].format(name=name))
            time.sleep(5)
            if __name__ == '__main__':
                time.sleep(3)
                sys.exit
            else:
                time.sleep(3)
                return

    return play_RPS

def setup_game():
    print(' Welcome to Rock-Paper-Jenah!\n')

    lang = input("Choose your language/Elige tu idioma: 'en' for English, 'es' for Español\n: ").lower().strip()
    if lang not in ['en', 'es']:
        print("Invalid choice. Defaulting to English.\n")
        lang = 'en'

    name = input(f"{MESSAGES[lang]['original_name']}\n: ").strip()
    if not name:
        name = "PlayerOne" 

    return lang, name

if __name__ == '__main__':
    lang, name = setup_game()
    Rock_Paper_Jenah = RPS(name=name, lang=lang)
    Rock_Paper_Jenah()

