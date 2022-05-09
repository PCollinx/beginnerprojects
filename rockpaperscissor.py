import random
import math

def play():
    user = input("Choose 'r' for rock, 'p' for paper and 's' for scissors: \n")
    user = user.lower()

    computer = random.choice(['r', 's', 'p'])

    if computer == user:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)

def is_win(user, computer):
        if (user == 's' and computer == 'p') or (user == 'p' and computer == 'r') or (user == 'r' and computer == 's'):
            return True
        return False

def play_out_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    while (player_wins < wins_necessary) or (computer_wins < wins_necessary):
        result, user, computer = play()

        if result == 0:
            print(f"You chose {user} and the computer chose {computer}. it is a tie! \n")

        elif result == 1:
            player_wins += 1
            print(f"You chose {user} and the computer chose {computer}. You won!\n")

        else:
            computer_wins += 1
            print(f"You chose {user} and the computer chose {computer}. You lost! \n")
        print('\n')

    if computer_wins > player_wins:
        print(f"The computer won the best out of {n} games")

    else:
        print(f"You won best out of {n} games")






if __name__ == '__main__':
    play_out_of(3)
