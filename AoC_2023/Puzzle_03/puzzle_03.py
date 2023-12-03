import re

fileName = "input.txt"
file = open(fileName)
file2 = open(fileName)

simbols = ["+", "-", "*", "/", "=", "#", "$", "%", "@", "&"]

def findSimbol(simbol):
    if(simbol == "aa"):
        print()

prevLine = ""
curLine = ""
linija3Simbols = ""

linesAndSimbolPositions = []
linesAndNumbers = []
lineNumber = 1

# Find all positions of all simbols
p = '[\d]+'
with file as f:
    for line in f:
        line = line.rstrip("\n")
        # print(f"Ovo je linija:\n{line}")

        simbolPositions = [pos for pos, c in enumerate(line) if c in simbols]
        addLineSimbols = [lineNumber, simbolPositions]
        linesAndSimbolPositions.append(addLineSimbols)

        lineNumber += 1

# Find numbers and their positions
lineNumber = 0
with file2 as f2:
    for line in f2:
        line = line.rstrip("\n")
        # print(f"Ovo je linija:\n{line}")

        numbers = []
        if re.search(p, line) is not None:
            for catch in re.finditer(p, line):
                print(catch[0])
                print(catch.span())
                print(catch.start()-1)
                print(catch.end()+1)
                numbers.append(catch[0])

        addLineNumbers = [lineNumber, numbers]
        linesAndNumbers.append(addLineNumbers)

        lineNumber += 1


for l in linesAndSimbolPositions:        
    print(f"{l}")

for n in linesAndNumbers:        
    print(f"{n}")