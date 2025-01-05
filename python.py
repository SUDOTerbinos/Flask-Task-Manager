import random


number_to_guess = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed it right!")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
