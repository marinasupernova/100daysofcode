import random
number = random.randint(1,100)
number_of_guesses = 0
while number_of_guesses < 10:
    print("Guess a number between 1 and 100")
    guess = input()
    guess = int(guess)
    number_of_guesses += 1
    if guess == number:
        print("Correct! You win! That's the magic number!")
        break
    if number_of_guesses >= 10:
        print(f"Aww, you ran out of guesses. The magic number was {number}")




        #number_of_guesses[i] += 1 10line
        #if guess == magic_number 11 line magic_number = 7 there is no set magic number of yours - it is a random one