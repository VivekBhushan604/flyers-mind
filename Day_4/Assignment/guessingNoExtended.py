import random

secret_number = random.randint(1, 10)

attempts = 0
score = 100

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 10.\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("\n🎉 Correct!")
        print(f"Number was {secret_number}")
        print(f"Attempts: {attempts}")
        print(f"Final Score: {score}")
        break

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    score = max(0, score - 10)