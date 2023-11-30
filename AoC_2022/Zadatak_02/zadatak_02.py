fileName = "strategy.txt"
file = open(fileName)

myScore = 0
myNewScore = 0
currentPlay = ''

win = 6
draw = 3
loss = 0

rock = 1
papper = 2
scissors = 3

def getResultForCurrentPlay():
    match currentPlay:
        case "A X":
            return draw + rock
        case "A Y":
            return win + papper
        case "A Z":
            return loss + scissors
        case "B X":
            return loss + rock
        case "B Y":
            return draw + papper
        case "B Z":
            return win + scissors
        case "C X":
            return win + rock
        case "C Y":
            return loss + papper
        case "C Z":
            return draw + scissors

# X - gubi
# Y - draw
# Z - win

# A - X Kamen  1
# B - Y Papir  2
# C - Z Škare  3

def getNewResults():
    player1 = currentPlay[0]
    if(currentPlay[2] == 'X'):
        if(player1 == 'A'):
            return loss + scissors
        elif(player1 == 'B'):
            return loss + rock
        elif(player1 == 'C'):
            return loss + papper
    elif(currentPlay[2] == 'Y'):
        if(player1 == 'A'):
            return draw + rock
        elif(player1 == 'B'):
            return draw + papper
        elif(player1 == 'C'):
            return draw + scissors
    elif(currentPlay[2] == 'Z'):
        if(player1 == 'A'):
            return win + papper
        elif(player1 == 'B'):
            return win + scissors
        elif(player1 == 'C'):
            return win + rock

with file as f:
        for gameRound in f:
            # currentPlay = (gameRound.rstrip('\n').split())
            currentPlay = gameRound.rstrip('\n')
            print(currentPlay)
            # print(getResultForCurrentPlay())
            myScore += getResultForCurrentPlay()
            print(currentPlay[0])
            print(currentPlay[2])
            print(getNewResults())
            myNewScore += getNewResults()

print()
print(f"Moj prvi score: {myScore}")
print(f"Moj novi score: {myNewScore}")
input()