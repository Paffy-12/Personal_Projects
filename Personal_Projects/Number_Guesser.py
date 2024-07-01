import random

while True:
    try:
        x = int(input("Enter the lower range: "))
        y = int(input("Enter the upper range: "))
        if x > y:
            print("Lower range should be less than or equal to the upper range. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter integers only.")

num = random.randint(x, y)
print("I have selected a number between", x, "and", y)

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess == num:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Incorrect. Try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("The number was:", num)
