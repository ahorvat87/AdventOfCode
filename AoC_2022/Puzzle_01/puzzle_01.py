from operator import attrgetter

fileName = "Calories.txt"
file = open(fileName)

lefList = []
caloriesSum = 0

class Elf:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

counter = 1
with file as f:
    for line in f:
        checkLine = (line.rstrip('\n'))
        if not checkLine:
            name = f"Elf_{counter}"
            lefList.append(Elf(name, caloriesSum))
            caloriesSum = 0
            counter += 1
            pass

        if checkLine:
            caloriesSum += int(checkLine)

name = f"Elf_{counter}"
lefList.append(Elf(name, caloriesSum))

for elf in lefList:
    print(elf.name)
    print(elf.calories)
    print()
print()

bestElf = max(lefList, key =attrgetter('calories'))

print(f"Top 1 vilenjak: {bestElf.name} ima {bestElf.calories} kalorija")
print()

together = 0
for i in range(3):
    max_elf = max(lefList, key =attrgetter('calories'))
    print(f"{max_elf.name} ima {max_elf.calories} kalorija.")
    together += max_elf.calories
    lefList.remove(max_elf)

print()
print(f"Top 3 vilenjaka po kalorijama, zajedno imaju: {together} kalorija")
input()