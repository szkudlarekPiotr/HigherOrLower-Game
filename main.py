import random
from art import logo, vs
from game_data import data

print(logo)

game_continue = True
account_b = random.choice(data)
score = 0


def account_info():
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")


def followers_check():
    guess = input("Make a guess: ").lower()
    if account_a['follower_count'] > account_b['follower_count']:
        if guess == 'a':
            print("Superb!")
            return True
        else:
            print("Wrong!")
            return False
    elif account_b['follower_count'] > account_a['follower_count']:
        if guess == 'b':
            print("Superb!")
            return True
        else:
            print("Wrong!")
            return False


while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    account_info()
    game_continue = followers_check()
    if game_continue:
        score += 1
        print(f"Your current score is: {score}")
    else:
        print(f"Your final score is: {score}")

