from RPS import RPS
from guess_number import guess_number
import sys
import time

def arcade():
    while True:
        choice = input('Welcome to the arcade please select:\n1 to play Rock, Paper, Jenah,\n2 to select Guess my number, or\nq for quit\n\n')
        if choice == '1':
            lang = input("Choose language: 'en' or 'es'\n> ").strip().lower()
            name = input("Enter your name:\n> ").strip() or "PlayerOne"
            play = RPS(name=name, lang=lang)
            play()
        elif choice == '2':
            name = input("Please enter your name:\n> ").strip() or "Player01"
            guess_number(name)
        elif choice == 'q'.lower():
            print('goodbye')
            time.sleep(3)
            sys.exit()
            
        else:
            print('please select 1,2 or q')

arcade()



