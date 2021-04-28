import random
number = random.randint(1,9)
chance=0
while chance < 5:
    guess=int(input("Enter your guess: "))
    if guess == number:
        print("Congrats! You Won!")
    elif guess < number:
        print("You lose, The number is", number )
    else:
        print("You lose, the guess was too high")
    chance=chance+1

