#guess the number
import random
print("The computer has chosen a number between 0 and 100,"\
      +"try guessing it in 4 or less guesses")
num=random.randint(0,100)
count=0
guess=int(input("Make a guess"))
count+=1
while guess!=num and count<=4 :
    if guess>num :
        guess=int(input("Lower your guess:"))
        count+=1
    elif guess<num :
        guess=int(input("Raise your guess"))
        count+=1
        
if guess==num and count<=4 :
    print("You guessed the number ",num," correct in ",count," guessses")
else:
    print("you took more tha 4 guesses")


input("\n\nPress enter to exit")
