# If you're looking for a better dick generator (including graphics), please go to
# https://github.com/OwlsNeck/python-cock-generator
# i made this at like 3am to learn how to work with classes in python

from os import system
import random

class penis: # this is the penis, penis defined, also can show the penis from this here
    def __init__(self, pLength, pGirth, testeCount):
        self.pLength = pLength
        self.pGirth = pGirth
        self.testeCount = testeCount

    def show(self): # this function will be used to tell the user all about their new penis
        if self.pLength == 1:
            print(f"Penis length is {self.pLength} inch.")
        else:
            print(f"Penis length is {self.pLength} inches.")

        if self.pGirth == 1:
            print(f"Penis girth is {self.pGirth} inch.")
        else:
            print(f"Penis girth is {self.pGirth} inches.")

        if self.testeCount == 1:
            print(f"{self.testeCount} ball.")
        else:
            print(f"{self.testeCount} balls.")

def buildPenis(): # gives the penis its specs, like length, girth, and how many balls
    inches = [1,2,3,4,5,6,7,8,9,10,11,12] # 12 inches makes a foot
    balls = [1,2] # imagine having 1 ball lmao (im really sorry if you do only have 1 testicle that must be devastating)

    length = random.choice(inches)
    girth = random.choice(inches)
    numOfBalls = random.choice(balls)

    result = penis(length, girth, numOfBalls)
    result.show()

def main(): # main function, gets called at start of program
    buildPenis()

while True: # infinite loop keeps window open
    system("clear") # clears screen so results are more apparent
    main()
    input("Press ENTER to create another penis...") # keeps loop from running wild