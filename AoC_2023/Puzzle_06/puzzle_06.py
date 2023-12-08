file = open("input.txt").read().split("\n")

time = file[0].split()
distance = file[1].split()

print(file)
print(time)
print(distance)

newTime = ""
for ti in range(1, len(time)):
    newTime += time[ti]

newDistance = ""
for ti in range(1, len(distance)):
    newDistance += distance[ti]

print(newDistance)

numbersOfWin = []

for i in range(1, len(time)):
    counter = 0
    print(counter)
    # counter = 0
    for t in range(int(time[i])):
        if(int(t) * (int(time[i]) - int(t)) > int(distance[i])):
            rez = int(t) * (int(time[i]) - int(t))
            print(rez)
            print(distance[i])
            print(int(t) * (int(time[i]) - int(t)) > int(distance[i]))
            counter += 1
    print(f"Counter: {counter} ********")
    numbersOfWin.append(counter)


print(numbersOfWin)
result = 1

for num in numbersOfWin:
    result *= num

print(result)


counter = 0
win = []
for t in range(int(newTime)):
    if((int(t) * (int(newTime) - int(t))) < int(newDistance)):
            rez = int(t) * (int(newTime) - int(t))
            counter += 1
    else:
        break
win.append(counter)

result = 1

for num in win:
    result *= num
print(result)

upper = int(newTime) - result
print(upper)

print(f"Part 2 result: {upper - result + 1}")