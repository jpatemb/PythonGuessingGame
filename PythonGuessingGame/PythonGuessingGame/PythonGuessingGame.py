import random

def game():
    n = random.randint(1, 100)
    count = 1
    guess = int(input("I'm thinking of a number between 1 an 100. Can you guess what number it is?"))
    while n != "guess":
        if guess < n:
            print ("Too low")
            count += 1
            guess = int(input("Guess again:"))
        elif guess > n:
            print("Too high")
            count += 1
            guess = int(input("Guess again:"))
        elif guess == n:
            print("Correct! You guessed the number in " + str(count) + " tries!")
            response = input("Want to play again? (y for Yes, n for No)")
            if response.lower().startswith("y"):
                print("Ok! Then let's play again!")
                game()
            elif response.lower().startswith("n"):
                exit("Alright, thanks for playing!\n")
            else:
                print("Invalid input! Please enter y for Yes, or n for No")
game()