# If you're looking for a better dick generator (including graphics), please go to
# https://github.com/OwlsNeck/python-cock-generator
# i made this at like 3am to learn how to work with classes in python

from os import system
from random import choice

class penis:
    def __init__(self, pLength, pGirth, testeCount):
        self.pLength = pLength
        self.pGirth = pGirth
        self.testeCount = testeCount

    def show(self):
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

def buildPenis():
    inches = [1,2,3,4,5,6,7,8,9,10,11,12] # 12 inches makes a foot
    balls = [1,2] # imagine having 1 ball lmao (im really sorry if you do only have 1 testicle that must be devastating)

    length = choice(inches)
    girth = choice(inches)
    numOfBalls = choice(balls)

    result = penis(length, girth, numOfBalls)
    result.show()

def main():
    system("clear")
    buildPenis()

if __name__ == "__main__":
    while True:
        main()
        input("Press ENTER to create another penis...")