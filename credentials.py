# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD
def main():
    uname=buildUsername()
    passwd = input("Create a new password: ")
    strongPassword=checkPassword(passwd)
    
    print("Account configured. Your new email address is",
        uname + "@marist.edu")

def getNames():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    names = [first, last]
    return names
def buildUsername():
    names = getNames()
    # TODO modify this to generate a Marist-style username
    uname = names[0] + "."+ names[1]
    return uname
def checkPassword(string):
    
    while (len(string))<8:
        print("Fool of a Took! That password is feeble!")
        string = input("Create a new password: ")
    print("The force is strong in this one…")
    return string
main()
