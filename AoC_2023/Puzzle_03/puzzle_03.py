import re

fileName = "input.txt"
file = open(fileName)
file2 = open(fileName)

simbols = ["+", "-", "*", "/", "=", "#", "$", "%", "@", "&"]
# simbols = ["*"]

linesAndSimbolPositions = []
linesAndNumbers = []
lineNumber = 1

# Find all positions of all simbols
p = '[\d]+'
with file as f:
    for line in f:
        line = line.rstrip("\n")

        simbolPositions = [pos for pos, c in enumerate(line) if c in simbols]
        addLineSimbols = [lineNumber, simbolPositions]
        linesAndSimbolPositions.append(addLineSimbols)

        lineNumber += 1

# Find numbers and their positions
lineNumber = 0
numbersToUse = []
with file2 as f2:
    for line in f2:
        line = line.rstrip("\n")

        numbers = []
        if re.search(p, line) is not None:
            for catch in re.finditer(p, line):
                print(catch[0])
                print(catch.span())

                if(catch.start() == 0):
                    startNumberPos = catch.start()
                else:
                    startNumberPos = catch.start()-1
                print(startNumberPos)
                endNumberPos = catch.end()
                print(endNumberPos)

                linePrev = []
                lineCurr = []
                lineNext = []
                length = len(linesAndSimbolPositions)

                if(lineNumber != 1):
                    linePrev = linesAndSimbolPositions[lineNumber - 1][1]

                lineCurr = linesAndSimbolPositions[lineNumber][1]

                if(lineNumber < length-1):
                    lineNext = linesAndSimbolPositions[lineNumber + 1][1]
                else:
                    lineNext = []

                if(linePrev):
                    for simbolPos in linePrev:
                        if(simbolPos >= startNumberPos and simbolPos <= endNumberPos):
                            numbersToUse.append(catch[0])

                for simbolPos in lineCurr:
                    if(simbolPos >= startNumberPos and simbolPos <= endNumberPos):
                        numbersToUse.append(catch[0])
                
                if(lineNext):
                    for simbolPos in lineNext:
                        if(simbolPos >= startNumberPos and simbolPos <= endNumberPos):
                            numbersToUse.append(catch[0])

                print("******************")
                print(f"Previous line {linePrev}")
                print(f"Current line {linesAndSimbolPositions[lineNumber][0]}: {lineCurr}")
                print(f"Next linija: {lineNext}")
                print("******************")
                
                numbers.append(catch[0])

        addLineNumbers = [lineNumber, numbers]
        linesAndNumbers.append(addLineNumbers)

        lineNumber += 1


for l in linesAndSimbolPositions:
    print(f"{l}")

print(linesAndNumbers)
print(f"Numbers to use: {numbersToUse}")

sum = 0
for number in numbersToUse:
    sum += int(number)

print(f"Part one result: {sum}")