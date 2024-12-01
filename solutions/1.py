import numpy as np

from utils.config import dir_data

data = np.loadtxt(dir_data.joinpath('1.txt'))

#####
# Part One
#####

# sort each column in ascending order, for each column seperatly
c1_sort = np.sort(data[:, 0])
c2_sort = np.sort(data[:, 1])

# get differences of each row
diff = c2_sort - c1_sort

# get sum of absolut diff values
result = int(np.sum(np.abs(diff)))

# print the result
print(f"Solution Part A: {result}")

#####
# Part Two
#####

# loop over each element in c1_sort and check how often it occurs in c2_sort
# mulitiply the number with the occurence and sum it up

result = 0
for i in c1_sort:
    result += np.sum(c2_sort == i) * i

# print the result
print(f"Solution Part B: {int(result)}")