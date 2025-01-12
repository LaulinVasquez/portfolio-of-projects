import random

def hello_world_game():
    name = input("Enter your name: ").capitalize()
    print("Welcome to the 'Hello, World!' Game!")
    print("Your goal is to guess the secret number!")
    print("Type 'exit' at any time to quit the game.\n")

    secret_number = random.randint(1, 20)  # Random number between 1 and 20
    attempts = 0

    while True:
        user = input("Enter your guess (1-20): ")
        
        if user.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            break

        if not user.isdigit():
            print("Please enter a valid number between 1 and 10.\n")
            continue

        guess = int(user)
        attempts += 1

        if guess < 1 or guess > 20:
            print("Your guess is out of range! Try again.\n")
        elif guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"Hello {name}, to the World! You win!")
            break

# Run the game
if __name__ == "__main__":
    hello_world_game()
