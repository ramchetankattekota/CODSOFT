import random

choices = ["rock", "paper", "scissors"]

while True:

    user = input("\nChoose rock, paper, or scissors: ").lower()

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")

    else:
        print("Computer Wins!")

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
