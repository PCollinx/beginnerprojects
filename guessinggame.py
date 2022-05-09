import random


a = int(input('What is the number you wish to start from?\n'))
b = int(input('What is the number you wish to end?\n'))


def validate_range(start, end):
    number_range = list(range(start, end))
    if len(number_range) > 20:
        return print('number has to be lower than 20')
    elif len(number_range) < 5:
        return print('number has to be greater than 5')
    number_of_chances = round(len(number_range) / 4)
    return number_of_chances


def guessing_game(low, high, rounds):
    print(f'you are to guess a number between {low} and {high} and you have  {rounds} rounds')
    number = random.randint(low, high)

    for i in range(rounds):
        try:
            guess = int(input('Guess a number: '))
            if guess == number:
                print('You got it, you\'re a genius')
                return
            elif guess > number:
                print('Try lower')
            elif guess < number:
                print('Try higher')
        except ValueError:
            print('Please enter a valid number')
    print(f'You didn\'t enter a valid number in {rounds} rounds, you lost.')

rounds = validate_range(a, b)
if bool(rounds) != False:
    guessing_game(a, b, rounds)
else:
    print('Your range should be greater than 5 and less than 20')


