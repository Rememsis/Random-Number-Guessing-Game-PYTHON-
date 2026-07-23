import random
number = random.randint(1,10000)
number_of_guesses = 0
number_of_chances = 5
while number_of_guesses < number_of_chances:
    print('Guess a number between 1 and 10000:')
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1
    if guess < number:
        print('Too Low')
        print(f"You have {number_of_chances - number_of_guesses} chances left to guess the magic number!")
    if guess > number:
        print('Too High')
        print(f"You have {number_of_chances - number_of_guesses} chances left to guess the magic number!")
    if guess == number:
        print("You got the magic number!")
        break

    if {number_of_guesses} == 20:
        print(f"Aww, you ran out of guesses. The Magic number was {number}.")
