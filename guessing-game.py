animalName=("Dog").lower()

def main():
    print("Thinking of an animal...\n")
    guess = (input("Guess the name of an animal.")).lower()
    while (7>0):
        if (guess == animalName):
            response=input("Congratulations, you guessed correctly. Respond y if you like this animal, n if not.")
            if(response=="y"):
                print("User likes dogs.")
                break
            elif(response=="n"):
                print("User does not like dogs.")
                break
            else:
                response=input("Invalid response, please try again.")
                if(response=="y"):
                    print("User likes dogs.")
                    break
                elif(response=="n"):
                    print("User does not like dogs.")
                    break
                else:
                    response=input("Invalid response, please try again.")
                
        elif (guess.startswith("q")):
            break
        else:
            guess = input("Incorrect, please try again.")
   
    
main()
        
        
    
    
