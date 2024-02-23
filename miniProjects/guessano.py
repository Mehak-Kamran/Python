#Guess the Number

import random

targetno=random.randint(1,100)




while True:
    
    user_input=input("Enter a no between 1-100 OR Wanna Quit? Press 'Q' ")
    if(user_input=='Q'):
        print("Number was ",targetno)
        break
    else:
        user_input= int(user_input)
        if (user_input==targetno):
            print("Congratulations You guessed the no correct....!")
            break
        elif(user_input<targetno):
            print("Your guess is small , try to guess a big no....!")
        else:
            print("Your no is too big try to guess small no ....!")

print("-----Game Over----------")