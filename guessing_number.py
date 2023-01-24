import random

num = random.randrange(0,10)
chances = 5
wrong = []
print("5 chances are given.")

while chances != 0 :
    your_guess_number = int(input("Guess number : "))
    if your_guess_number in wrong :
        print("You already guessed this number. Guess others.")
        print(f"{chances} left. Guess again.")
        continue
    if your_guess_number == num :
        print("You got the point!")
        break
    else :
        wrong.append(your_guess_number)
        chances -= 1
        print(f"{chances} left. Guess again.")