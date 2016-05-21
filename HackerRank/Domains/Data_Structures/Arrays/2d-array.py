#!/bin/python3

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


max_sum = float("-inf")

for i in range(4):
    for j in range(4):
        hourglass = [each[j:j+3] for each in arr[i:i+3]]

        hourglass[1][0] = 0
        hourglass[1][2] = 0

        _sum = 0

        for line in hourglass:
            _sum += sum(line)

        if _sum > max_sum:
            max_sum = _sum

print(max_sum)
