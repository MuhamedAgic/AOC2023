import sys
import pandas as pd
from copy import deepcopy

def day_15_part_1(filename):
    input = open(filename, "r").read().strip()
        
    ans = 0
    for val in input.split(","):
        hash_val = 0
        for c in val:
            hash_val = ((hash_val + ord(c)) * 17) % 256
        ans += hash_val
    print(ans)
    return ans
        
filename = "D:/git/magic/aoc2023/aoc2023/src/15/input.txt"
ans1 = day_15_part_1(filename)
print(f"Part one {ans1}")

# 506395 te laag
# 514283 te hoog

# ans2 = day_eight_part_two(filename)
# print(f"Part two {ans2}")
