animalName=("Dog").lower()

def main():
    print("Thinking of an animal...\n")
    guess = (input("Guess the name of an animal.")).lower()
    while (7>0):
        if (guess == animalName):
            print("Congratulations, you guessed correctly.")
            break
        elif (guess=="quit"):
            break
        else:
            guess = input("Incorrect, please try again.")
   
    
main()
        
        
    
    
