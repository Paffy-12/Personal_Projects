import random
import time

operators = ['+', '-', '*']

def generate_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(operators)
    exp = f"{num1} {op} {num2}"
    return exp, eval(exp)

def timed_math_challenge(num_questions=5, time_limit=30):
    score = 0
    start_time = time.time()

    print(f"You have {time_limit} seconds to answer {num_questions} questions.")
    print("Let's begin!")

    for _ in range(num_questions):
        if time.time() - start_time > time_limit:
            print("\nTime's up!")
            break

        problem, correct_answer = generate_problem()
        print(f"\n{problem} = ", end="")
        
        user_answer = input()
        
        try:
            if int(user_answer) == int(correct_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\nChallenge complete!")
    print(f"Score: {score}/{num_questions}")
    print(f"Time taken: {total_time:.2f} seconds")

print("Welcome to the Timed Math Challenge!")
while True:
    choice = input("Generate problem set? (y/n): ")
    if choice.lower() == 'n':
        break
    elif choice.lower() == 'y':
        timed_math_challenge()
    else:
        print("Enter a valid input (y/n)")