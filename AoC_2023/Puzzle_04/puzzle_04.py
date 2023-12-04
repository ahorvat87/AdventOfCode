filename = "input.txt"
file = open(filename)

point = []
allCards = []
allPoints = []
allMatches = []

with file as f:
    for i, line in enumerate(f):
        try:
            point[i] += 1
        except:
            point.append(0)
            point[i] += 1

        line = line.rstrip("\n")

        cardSplit = line.split(":")
        allCards.append(cardSplit)

        numbers = cardSplit[1].split(" | ")

        winNumbers = numbers[0].lstrip(" ")
        winNumbers = winNumbers.replace("  ", " ")
        winNumbers = winNumbers.split(" ")

        myNumbers = numbers[1].lstrip(" ")
        myNumbers = myNumbers.replace("  ", " ")
        myNumbers = myNumbers.split(" ")

        points = 0
        first = True
        matches = 0

        for num in myNumbers:
            if num in winNumbers:
                if(first):
                    points = 1
                    # print(f"{cardSplit[0]} has number {num} which is first and win!")
                    first = False
                else:
                    points *= 2
                    # print(f"{cardSplit[0]} has number {num} which is win!")
                matches += 1

        allPoints.append(points)
        allMatches.append(matches)

        for addLine in range(matches):
            try:
                point[i+1+addLine] += point[i]
            except:
                point.append(0)
                point[i+1+addLine] += point[i]

print(sum(allPoints))
print(sum(point))