# Determine which games would have been possible if the bag
# had been loaded with only 12 red cubes, 13 green cubes,
# and 14 blue cubes. What is the sum of the IDs of those games?

fileName = "input.txt"
file = open(fileName)

def checkNumberOfCubes(numberColor):
    number = int(numberColor[0])
    color = numberColor[1]
    if(color == "red" and number <=12):
        return True
    elif(color == "green" and number <=13):
        return True
    elif(color == "blue" and number <=14):
        return True
    else:
        return False

# ************ PART 1 ************

# sum = 0

# with file as f:
#     for line in f:
#         line = line.rstrip('\n')
#         gameSplit = line.split(":")
#         sets = gameSplit[1].split(";")
#         for set in sets:
#             cubes = set.split(",")
#             for cube in cubes:
#                 cube = cube.lstrip(" ").split(" ")
#                 itsOk = checkNumberOfCubes(cube)
#                 if(not itsOk):
#                     print(f"{gameSplit[0]} nije dobar! Vraća {itsOk}")
#                     print()
#                     break
#             if(not itsOk):
#                 break
            
#         if(itsOk):
#             gameNumber = gameSplit[0].split(" ")
#             sum += int(gameNumber[1])
#             print(f"{gameSplit[0]} je dobar i zbraja se. Njegov number je: {gameNumber[1]}")
#             print(f"Sum je: {sum}")
#             print()

# print(sum)


# maxRed = 0
# maxGreen = 0
# maxBlue = 0

# def findMaxNumber(numberColor):
#     number = numberColor[0]
#     color = numberColor[1]

#     if(color == "red"):
#          if(number < maxRed):
#                 maxRed = number
#     elif(color == "green"):
#         if(number < maxGreen):
#             maxGreen = number
#     elif(color == "blue"):
#         if(number < maxBlue):
#             maxBlue = number

# ************ PART 2 ************

totalSum = 0

with file as f:
    for line in f:
        line = line.rstrip('\n')
        gameSplit = line.split(":")
        sets = gameSplit[1].split(";")
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                cube = cube.lstrip(" ").split(" ")
                number = int(cube[0])
                color = cube[1]

                if color == "red":
                    if(number > maxRed):
                        maxRed = number
                elif(color == "green"):
                    if(number > maxGreen):
                        maxGreen = number
                elif(color == "blue"):
                    if(number > maxBlue):
                        maxBlue = number

        print(f"{gameSplit[0]}")
        print(f"Crvena: {maxRed}, zelena: {maxGreen}, plava: {maxBlue}")
        print()

        multiplied = maxRed * maxGreen * maxBlue
        totalSum += multiplied

print(totalSum)