import random

l = ['r', 'p', 's']

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Enter Rock('r'), Paper('p'), Scissors('s') or Quit('q'): ").lower()

    if user_input == 'q':
        print('Goodbye!')
        break

    if user_input not in ['r', 'p', 's']:
        print("Enter a valid input (r, p, s, or q)")
        continue

    comp_out = random.choice(l)
    
    print(f"Computer's choice: {comp_out}")

    if user_input == comp_out:
        print('Same choice, try again')
    elif (user_input == 'r' and comp_out == 's') or \
         (user_input == 'p' and comp_out == 'r') or \
         (user_input == 's' and comp_out == 'p'):
        print('You win!')
        user_wins += 1
    else:
        print('Computer wins!')
        computer_wins += 1

print(f"Your wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
