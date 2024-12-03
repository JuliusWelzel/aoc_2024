import re

from utils.config import dir_data

#####
# Part One
#####

# load data
with open(dir_data.joinpath('3.txt')) as f:
    data = f.read()
    
# define patten
pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern_mul, data)

# multiply number in each row and sum it up
result = 0
for match in matches:
    result += int(match[0]) * int(match[1])
    
# print the result
print(f"Solution Part One: {result}")

#####
# Part Two
#####

with open(dir_data.joinpath('3.txt')) as f:
    data = f.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", data)
    on = True
    ans = 0
    for a, b, c, d in matches:
        if c == "don't()":
            on = False
        elif d == "do()":
            on = True
        elif on:
            ans += int(a) * int(b)
            
# Print the result
print(f"Solution Part Two with Conditional Handling: {ans}")