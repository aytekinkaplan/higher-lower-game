import random
from data import data


def get_random_account():
    """ Rastgele bir hesap seç ve döndür. """
    return random.choice(data)


def compare_accounts(account_a, account_b):
    """ İki hesabı takipçi sayısına göre karşılaştır. """
    if account_a['follower_count'] > account_b['follower_count']:
        return "a"
    else:
        return "b"


def higher_lower_game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = compare_accounts(account_a, account_b)

        if guess == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

    return score