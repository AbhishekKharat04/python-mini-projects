import random
number=random.randint(1,100)
for i in range(5):
    guess=int(input("Guess: "))
    if guess==number:
        print("Correct!")
        break
    elif guess<number:
        print("Too low")
    else:
        print("Too high")
else:
    print("Number was",number)