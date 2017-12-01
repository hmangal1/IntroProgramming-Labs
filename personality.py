# Lab 10  - AI Personality
# Herrick Mangal
# Demonstrates the use of a matrix for looking up values.
# December 1, 2017
###
from graphics import *
# emotional state supported by this AI
angry     = 0
disgusted = 1
fearful   = 2
happy     = 3
sad       = 4
surprised = 5

# kinds of interaction from which the user may choose
actions = [ "reward", "punish", "joke", "threaten", "quit" ]
reward   = 0
punish   = 1
joke     = 2
threaten = 3
quit     = 4

# responses that this AI may have when feeling each emotion
responses = [
        "Stop it! You're making me angry!"
    ,   "Ugh! Why don't you just go away?"
    ,   "No, please... don't!"
    ,   "I feel so happy right now!"
    ,   "You're really bringing me down."
    ,   "Oh my goodness, how unexpected!"
    ]

# personality matrix
personality = [
        # reward  punish  joke   threaten
        [ happy,     sad,   disgusted, angry ] # angry
    ,   [ angry,     angry, disgusted, fearful ] # disgusted
    ,   [ surprised, sad,   surprised, fearful ] # fearful
    ,   [ happy,     sad,   happy,     surprised ] # happy
    ,   [ surprised, sad,   happy,     angry ] # sad
    ,   [ happy,     sad,   happy,     fearful ] # surprised
    ]

def main():
    showIntro()
    primaryLoop()
    ending()
def showIntro():
    app=GraphWin("AI Personality",750,300)
    app.setCoords(0,0,10,10)

    Text(Point(5,7),"Hello! My name is Alice Ingall.").draw(app)
    Text(Point(5,5),"I am programmed to respond to four different actions:"
        " reward, punish, joke, or threaten.").draw(app)
    Text(Point(5,3),"To interact with me, enter one of these actions at the prompt.").draw(app)

    inputBox=Entry(Point(5,2),8)
    inputBox.draw(app)

    while app.getKey() != "Return":pass
    choice=str(inputBox.getText())

    app.close()
    return choice
   
def ending():
    print("Goodbye.")
def showResponse(output,emotion):
    outputStr=responses[emotion]
    output.setText(outputStr)
def primaryLoop():
    app=GraphWin("AI Personality",400,100)
    app.setCoords(0,0,10,10)
    output= Text(Point(5,5),"").draw(app)

    currentEmotion = happy
    while True:
        showResponse(output,currentEmotion)
        userAction = getNextInteraction()
        currentEmotion = lookupNewEmotion(currentEmotion, userAction)

def getNextInteraction():
    choice = showIntro()
    if choice == "reward":
        return 0
    elif choice == "punish":
        return 1
    elif choice == "joke":
        return 2
    elif choice == "threaten":
        return 3

def lookupNewEmotion(emotion, action):
    return personality[emotion][action]

main()
