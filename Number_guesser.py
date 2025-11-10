import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range == 0:
        print("Enter number greater than 0")
        quit()

    random_number = random.randint(0, top_of_range)
    answer = input("Guess the number: ")
    answer = int(answer)
    guesses = 0
    while True:
        guesses += 1
        if answer == random_number:
            print("Correct guess!")
            break
        elif answer < random_number:
            answer = input("Guess higher: ")
            answer = int(answer)
        else:
            answer = input("Guess lower: ")
            answer = int(answer)

    print("You guessed the correct answer in " + str(guesses) + " attempt(s)!")


else:
    print("Enter a number next time!")
    quit()