fileName = "CalibrationValues2.txt"
file = open(fileName)

leterNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
allNumbers = []
numbers = []
word = ""
sum = 0

def returnNumbers(word):
    match word:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9

with file as f:
    for line in f:
        line = line.rstrip('\n')
        if(numbers):
            number = str(numbers[0])
            number += str(numbers[-1])
            allNumbers.append(number)
            print(f"Ovo je broj koji se računa: {number}")
            number = ''
            sum = 0
            for num in allNumbers:
                sum += int(num)

            print(f"Suma svih brojeva je: {sum}")
            print()

        numbers.clear()
        print(f"Ovo je linija: {line}")
        lineNumbers = []
        for letNum in leterNumbers:
            index = line.find(letNum)
            if(index != -1):
                print(f"Index od {letNum}, kojemu je duzina {len(letNum)} u {line} je {index}")
                lineNumbers.append([index, letNum])
                # print(sorted(lineNumbers))

        sortedList = sorted(lineNumbers)
        if(sortedList):
            wordFirst = sortedList[0][1]
            wordLast = sortedList[-1][1]
            line = line.replace(sortedList[0][1], str(returnNumbers(wordFirst)))
            line = line.replace(sortedList[-1][1], str(returnNumbers(wordLast)))
        print(f"Ovo je replaceano: {line}")

        for ch in line:
            if(ch.isdigit()):
                numbers.append(ch)
        print(line)
        print(numbers)

print(allNumbers)

sum = 0
for num in allNumbers:
    sum += int(num)

print(f"Suma svih brojeva je: {sum}")


input()
