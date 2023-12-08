import sys
sys.setrecursionlimit(2000000) # wanted to set on 65 duizend miljoen

class Node:
    def __init__(self):
        self.location = "000"
        self.left = "000"
        self.right = "000"

    def __str__(self):
        return f"You are here: '{self.location}', left: '{self.left}', right: '{self.right}'"


def goto_zzz(steps_to_take, nodes, current_node_loc="AAA", at_current_step=0, steps_taken=0):
    if current_node_loc == "ZZZ":
        print(f"Total steps: {steps_taken}")
        return steps_taken

    if at_current_step == len(steps_to_take) - 1: # instructies opnieuw uitvoeren
        at_current_step = 0

    current_node = next((node for node in nodes if node.location == current_node_loc), None)
    print(f"{current_node}")
    if current_node is None:
        print("beltegoed is op, spreek je later!")
        return steps_taken

    current_step = steps_to_take[at_current_step]

    steps_taken += 1
    at_current_step += 1

    if current_step == "L":
        print(f"Going to '{current_node.left}'")
        goto_zzz(steps_to_take, nodes, current_node.left, at_current_step=at_current_step, steps_taken=steps_taken)
    elif current_step == "R":
        print(f"Going to '{current_node.right}'")
        goto_zzz(steps_to_take, nodes, current_node.right, at_current_step=at_current_step, steps_taken=steps_taken)

def day_eight_part_one(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    steps_to_take = lines[0]
    nodes = []
    print(steps_to_take)
    for idx, line in enumerate(lines):
        if idx > 1:
            location = line.split("=")[0].replace(" ", "")
            left     = line.split("=")[1].split(",")[0].replace(" (", "")
            right    = line.split("=")[1].split(",")[1].replace(" ", "").replace(")\n", "")
            if idx == len(lines):
                right    = line.split("=")[1].split(",")[1].replace(" ", "").replace(")", "")

            node = Node()
            node.location = location
            node.left = left
            node.right = right

            nodes.append(node)

    return goto_zzz(steps_to_take, nodes)

filename = "D:/git/magic/aoc2023/aoc2023/src/eight/input.txt"
ans1 = day_eight_part_one(filename)
print(f"Part one {ans1}")