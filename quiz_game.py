print("Welcome to the computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing != 'yes':
    quit()

print("Okay! Let's play :) ")

score = 0

#-----------------#

answer = input("What's the full form of CPU? ")

if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

#-----------------#

answer = input("What's the full form of NLH? ")

if answer.lower() == "no limit hold'em":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")


#-----------------#

answer = input("What's the full form of OS? ")

if answer.lower() == "operating system":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")


print("You got", score, "questions correct!")