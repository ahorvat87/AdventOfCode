import re
fileName = "CalibrationValues.txt"
# fileName = "input.txt"
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

def rreplace(s, old, new, occurence):
    li = s.rsplit(old, occurence)
    return new.join(li)

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
        sortedList = []
        lineNumbers = []
        for letNum in leterNumbers:
            nesto = re.finditer(letNum, line)
            for x in re.finditer(letNum, line):
                # print(f"Ovo je index za {letNum}:  {x.start()}")
                lineNumbers.append([x.start(), letNum])
            # index = line.find(letNum)
            # if(index != -1):
            #     print(f"Index od {letNum}, kojemu je duzina {len(letNum)} u {line} je {index}")
            #     lineNumbers.append([index, letNum])
                # print(sorted(lineNumbers))
            if(lineNumbers):
                print(f"Ovo su sortirani: {sorted(lineNumbers)}")

        sortedList = sorted(lineNumbers)
        line1 = ""
        line2 = ""
        if(sortedList):
            wordFirst = sortedList[0][1]
            wordLast = sortedList[-1][1]
            print(f"Prvi: {wordFirst}")
            print(f"Zadnji: {wordLast}")
            line1 = line.replace(sortedList[0][1], str(returnNumbers(wordFirst)), 1)
            print(f"Promijenjen prvi: {line1}")
            # line2 = line.replace(sortedList[-1][1], str(returnNumbers(wordLast)), 1)
            line2 = rreplace(line, wordLast, str(returnNumbers(wordLast)), 1)
            print(f"Promijenjen zadnji: {line2}")

        if(not line1):
            for ch in line:
                if(ch.isdigit()):
                    numbers.append(ch)
                    break
        else:
            for ch in line1:
                if(ch.isdigit()):
                    numbers.append(ch)
                    break
        
        if(not line2):
            line = line[::-1]
            for ch in line:
                if(ch.isdigit()):
                    numbers.append(ch)
                    break
        else:
            line2 = line2[::-1]
            for ch in line2:
                if(ch.isdigit()):
                    numbers.append(ch)
                    break
        print(line)
        print(numbers)

print(allNumbers)

sum = 0
for num in allNumbers:
    sum += int(num)

print(f"Suma svih brojeva je: {sum}")


input()
