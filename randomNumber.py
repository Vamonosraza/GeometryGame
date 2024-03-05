import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    attempts = 0
    while True:
        user_input = input("Enter your guess:")
        if user_input.lower() == "exit":
            print(f"The secret number was {secret_number}. GoodBye!")
            break
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Try a higher number.")
            elif user_guess > secret_number:
                print("Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
