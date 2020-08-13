import math
from csv import reader

with open("stdDev.csv", newline="") as f:
    file_data = list(reader(f))

file_data.pop(0)

total = 0
for x in file_data:
    total += int(x[0])

mean = total/len(file_data)

squaredList = []
for number in file_data:
    squaredList.append((int(number[0])-mean)**2)

sum = 0
for i in squaredList:
    sum += i

stdDeviation = math.sqrt(sum/(len(file_data)-1))

if file_data[0][4] == str(int(sum)) and file_data[0][6] == str(stdDeviation) and file_data[0][1] == str(int(mean)):
    print("MEAN:", int(mean))
    print("STANDARD DEVIATION:", stdDeviation)
else:
    print("WRONG CALCULATION")
