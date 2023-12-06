from operator import *
from functools import reduce # python3 compatibility

def get_amount_winning_possibilities(race_time, race_distance_record):
    amount_winning_possibilities = 0

    driven_distance = 0
    for mm_p_s in range(race_time):
        time_left = race_time - mm_p_s
        if mm_p_s * time_left > race_distance_record:
            amount_winning_possibilities += 1

    return amount_winning_possibilities

def day_6_part_1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    race_times = lines[0].split(":")[1].split()
    race_distances = lines[1].split(":")[1].split()

    race_times = [int(x) for x in race_times]
    race_distances = [int(x) for x in race_distances]

    print(f"Race times {race_times}")
    print(f"Race distances {race_distances}")

    millimeter_per_second = 0

    winning_possibilities_all_rounds = []
    for i in range(len(race_times)):
        current_amount_possibilities = get_amount_winning_possibilities(race_times[i], race_distances[i])
        winning_possibilities_all_rounds.append(current_amount_possibilities)

    print(f"winning possibilities all rounds: {winning_possibilities_all_rounds}")
    print(reduce(mul, winning_possibilities_all_rounds, 1))
    return reduce(mul, winning_possibilities_all_rounds, 1)

filename = "D:/git/magic/aoc2023/aoc2023/src/six/input.txt"
day_6_part_1(filename)