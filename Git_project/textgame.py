import time
import random


def print_slow(text):
    for char in text.split():
        print(char, end=' ', flush=True)
        time.sleep(0.15)
    print()


def start_game():
    # function to start the game
    print_slow('welcome to the text based advanture Game!')
    print_slow('You are standing in front of a dark cave.')
    print_slow('Do you want to enter the cave yes/no?')

    choice = input().lower()
    if choice == 'yes':
        enter_cave()
    elif choice == 'no':
        print_slow('you decided to not to enter in the cave and go back to home.')
    else:
        print('invalid choice: Please enter yes/no')
        start_game()


def enter_cave():
    print_slow('Now you are in the dark cave.')
    print_slow('You see two paths ahead.One to right and one to left.')
    print_slow('Which path do you choose?:Right/Left')

    choice = input().lower()
    if choice == 'left':
        left_path()

    elif choice == 'right':
        right_path()

    else:
        print_slow('Invalid entry: Please choose Right/Left path')
        enter_cave()


def left_path():
    print_slow('You taken left path.')
    lis_events = random.choices(['you find a treasure chest!', 'you encounter a sleeping DRAGON.'])
    print_slow(''.join(lis_events))
    if ''.join(lis_events) == 'you find a treasure chest!':
        print_slow('Do you want to open it? Yes/No?')
    elif ''.join(lis_events) == 'you encounter a sleeping DRAGON.':
        print_slow('Do you want sneak pass the DRAGON or turn back? sneak/turn?')

    # choice = input().lower()

    if ''.join(lis_events) == 'you find a treasure chest!':
        choice = input().lower()
        if choice == 'yes':
            print_slow('You open the chest and find a pile of gold!')
            print_slow('Congratulations! You Win the game!')

        elif choice == 'no':
            print_slow('you decided to not open the chest and continue exploring.')
            print_slow('you find nothing else and exit the cave.')

        else:
            print_slow('Invalid Input:Please enter yes/no.')
            left_path()

    elif ''.join(lis_events) == 'you encounter a sleeping DRAGON.':
        # print_slow('Do you want sneak pass the DRAGON or turn back? sneak/turn?')
        choice = input().lower()
        if choice == 'sneak':
            print_slow('You try to sneak pass the dragon.')
            print_slow('DRAGON wakes up and eat you...')
            print_slow('GAME OVER!')

        elif choice == 'turn':
            print_slow('you decided to turn back and take the left path.')
            right_path()
        else:
            print_slow('Invalid input: please enter sneak/turn.')


def right_path():
    print_slow('You taken right path.')
    lis_events = random.choices(['you find a treasure chest!', 'you encounter a sleeping DRAGON.'])
    print_slow(''.join(lis_events))
    if ''.join(lis_events) == 'you find a treasure chest!':
        print_slow('Do you want to open it? Yes/No?')
    elif ''.join(lis_events) == 'you encounter a sleeping DRAGON.':
        print_slow('Do you want sneak pass the DRAGON or turn back? sneak/turn?')

    # choice = input().lower()

    if ''.join(lis_events) == 'you find a treasure chest!':
        choice = input().lower()
        if choice == 'yes':
            print_slow('You open the chest and find a pile of gold!')
            print_slow('Congratulations! You Win the game!')

        elif choice == 'no':
            print_slow('you decided to not open the chest and continue exploring.')
            print_slow('you find nothing else and exit the cave.')

        else:
            print_slow('Invalid Input:Please enter yes/no.')
            right_path()

    elif ''.join(lis_events) == 'you encounter a sleeping DRAGON.':
        # print_slow('Do you want sneak pass the DRAGON or turn back? sneak/turn?')
        choice = input().lower()
        if choice == 'sneak':
            print_slow('You try to sneak pass the dragon.')
            print_slow('DRAGON wakes up and eat you...')
            print_slow('GAME OVER!')

        elif choice == 'turn':
            print_slow('you decided to turn back and take the left path.')
            left_path()
        else:
            print_slow('Invalid input: please enter sneak/turn.')


start_game()
