from time import sleep
from random import randint

OPTIONS = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}

# pairs of (player, computer) where the player wins
WINNING_PLAYS = [(1, 3), (2, 1), (3, 2)]

print('Welcome to ROCK, PAPER, SCISSORS game!')
print('=' * 43)
print('Please choose one of the following options:')

sleep(2)

print('1 - ROCK')
print('2 - PAPER')
print('3 - SCISSORS')

choice = 0
while choice not in OPTIONS:
    try:
        choice = int(input('Enter your choice (1, 2, or 3): '))
    except ValueError:
        choice = 0
    if choice not in OPTIONS:
        print('Invalid option! Please type 1, 2, or 3.')

random_choice = randint(1, 3)

print(f'\nYou chose {OPTIONS[choice]}')
sleep(1)
print(f'The computer chose {OPTIONS[random_choice]}\n')
sleep(1)

if choice == random_choice:
    print("It's a TIE!")
elif (choice, random_choice) in WINNING_PLAYS:
    print('You WIN!')
else:
    print('You LOSE!')





