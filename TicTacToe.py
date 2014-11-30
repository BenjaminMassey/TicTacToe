vLine = "|"
hLine = "-"
spots = dict()
spots["a"] = "a"
spots["b"] = "b"
spots["c"] = "c"
spots["d"] = "d"
spots["e"] = "e"
spots["f"] = "f"
spots["g"] = "g"
spots["h"] = "h"
spots["i"] = "i"
gameXWon = False
gameOWon = False

def firstLine():
    print(" " + spots["a"] + vLine + spots["b"] + vLine + spots["c"])
def hDivider():
    print(hLine + hLine + hLine + hLine + hLine + hLine + hLine)
def secondLine():
    print(" " + spots["d"] + vLine + spots["e"] + vLine + spots["f"])
def thirdLine():
    print(" " + spots["g"] + vLine + spots["h"] + vLine + spots["i"])
def showBoard():
    firstLine()
    hDivider()
    secondLine()
    hDivider()
    thirdLine()
def getInput(check):
    Input = input(check + ": ")
    if Input == "a":
        spots["a"] = check
    if Input == "b":
        spots["b"] = check
    if Input == "c":
        spots["c"] = check
    if Input == "d":
        spots["d"] = check
    if Input == "e":
        spots["e"] = check
    if Input == "f":
        spots["f"] = check
    if Input == "g":
        spots["g"] = check
    if Input == "h":
        spots["h"] = check
    if Input == "i":
        spots["i"] = check

def checkWin(check):
    if spots["a"] == check and spots["b"] == check and spots["c"] == check:
        return True
    if spots["d"] == check and spots["e"] == check and spots["f"] == check:
        return True
    if spots["g"] == check and spots["h"] == check and spots["i"] == check:
        return True
    if spots["a"] == check and spots["d"] == check and spots["g"] == check:
        return True
    if spots["b"] == check and spots["e"] == check and spots["h"] == check:
        return True
    if spots["c"] == check and spots["f"] == check and spots["i"] == check:
        return True
    if spots["a"] == check and spots["e"] == check and spots["i"] == check:
        return True
    if spots["c"] == check and spots["e"] == check and spots["g"] == check:
        return True
    return False

print("This is a very simple text-based tic tac toe game. You will not be playing against a friend of yours,")
print("who will work at the same computer as you. You will see a tic tac toe board like this one:")
showBoard()
print("Just type what corresponding letter you would like to land on. It will start with X and then alternate.")
while gameXWon == False and gameOWon == False:
    getInput("X")
    showBoard()
    if checkWin("X"):
        gameXWon = True
    if gameXWon == False:
        getInput("O")
        showBoard()
        if checkWin("O"):
            gameOWon = True

if gameXWon:
    print("Congratulations! X won the game!")
if gameOWon:
    print("Congratulations! O won the game!")
