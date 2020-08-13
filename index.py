import math, csv

with open("stdDev.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total = 0
n = len(file_data)
for x in file_data:
    total += int(x[0])

mean = total/n

squaredList = []
for number in file_data:
    a = int(number[0])-mean
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum += i

stdDeviation = math.sqrt(sum/(len(file_data)-1))

if file_data[0][4] == str(int(sum)) and file_data[0][6] == str(stdDeviation) and file_data[0][1] == str(int(mean)):
    print("MEAN:", int(mean))
    print("STANDARD DEVIATION:", stdDeviation)
else:
    print("WRONG CALCULATION")
