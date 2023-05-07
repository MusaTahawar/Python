import random
musa_input = input("Enter a choice (rock, paper, scissors):")
game_actions = ["rock", "paper", "scissors"]
bot_input = random.choice(game_actions)
print("\nI chose", musa_input, "computer chose", bot_input)
if musa_input == bot_input:
    print(musa_input, "It's a tie!")
elif musa_input == "rock":
    if bot_input == "scissors":
        print("Rock smashes scissors! Musa win!")
else:
    print("Paper covers rock! You lose.")

if musa_input == "paper":
    if bot_input == "rock":
        print("Paper covers rock! Musa win!")
else:
    print("Scissors cuts paper! You lose.")
if musa_input == "scissors":
    if bot_input == "paper":
        print("Scissors cuts paper! Musa win!")
else:
    print("Rock smashes scissors! You lose.")
