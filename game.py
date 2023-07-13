import random


def generate_random_number():
    return random.randint(1, 10)


def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    computer_score = 0
    user_score = 0
    rounds = 5

    print("Welcome to the Random Number Competition!")
    print("Guess a number between 1 and 10.")
    print(f"You and the computer will each have {rounds} attempts.")

    for _ in range(rounds):
        computer_number = generate_random_number()
        user_guess = get_user_guess()

        print("Computer's number:", computer_number)
        print("Your guess:", user_guess)

        if user_guess == computer_number:
            user_score += 1
            computer_score += 1
            print("It's a tie!")
        elif user_guess > computer_number:
            user_score += 1
            print("Congratulations! You win this round.")
        else:
            computer_score += 1
            print("Sorry, the computer wins this round.")

        print("---------------")

    print("Game Over!")
    print("Final Scores:")
    print("Computer:", computer_score)
    print("You:", user_score)

    if user_score > computer_score:
        print("Congratulations! You win the competition.")
    elif computer_score > user_score:
        print("Sorry, the computer wins the competition.")
    else:
        print("It's a tie!")


play_game()
