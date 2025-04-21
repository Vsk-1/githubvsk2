import random

number_to_guess = random.randint(1, 100)
attempt = int(input('How many attempts do u want to guess the number(1-5): '))
attempts_left = attempt

while attempts_left > 0:
    try:
        guess = int(input(f'Guess the number between 1 and 100 (Attempts left: {attempts_left}): '))

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break

        attempts_left -= 1

        if attempts_left == 0:
            print(f'OOPS! You ran out of attempts. The number was {number_to_guess}.')
            print('...BETTER LUCK NEXT TIME...')
        
    except ValueError:
        print('Please enter a valid number')
