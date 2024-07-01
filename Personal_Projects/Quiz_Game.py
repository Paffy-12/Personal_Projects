import random  

print("Welcome to my computer quiz!")

q_and_a = {
    1: ("Which river is the longest in the world?", "Nile"),
    2: ("In which year did the Titanic sink?", "1912"),
    3: ("What planet is known as the Red Planet?", "Mars"),
    4: ("Who is the author of 'To Kill a Mockingbird'?", "Harper Lee"),
    5: ("How many players are on a soccer team?", "11"),
    6: ("What is the name of the coffee shop in the TV show 'Friends'?", "Central Perk"),
    7: ("What is the name of the largest ocean on Earth?", "Pacific Ocean"),
    8: ("What is the most widely spoken language in the world?", "Mandarin"),
    9: ("In which country would you find the Great Barrier Reef?", "Australia"),
    10: ("What is the capital of France?", "Paris")
}

while True:
    playing = input("Do you want to play? (y/n): ").lower()
    if playing == 'n':
        print("Thanks for playing!")
        break
    elif playing == 'y':
        num = random.randint(1, 10)
        question, correct_answer = q_and_a[num]
        print(question)
        res = input().strip()
        if res == correct_answer:
            print("Correct!!!")
        else:
            print("Incorrect!!!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
