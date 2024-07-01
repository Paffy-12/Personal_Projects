import random


def roll():
    roll = random.randint(1, 6)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 20
scores = [0 for _ in range(players)]

while max(scores) < max_score:
    for i in range(players):
        print("\nPlayer number", i + 1, "turn has just started!")
        print("Your total score is:", scores[i], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        scores[i] += current_score
        print("Your total score is:", scores[i])

winner_index = scores.index(max(scores))
print("Player number", winner_index + 1, "is the winner with a score of:", max(scores))