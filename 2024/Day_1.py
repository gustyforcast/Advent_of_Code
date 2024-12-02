import os


def do_the_thing(pair):
    left, right = pair
    sorted_left = sorted([int(x) for x in list(left)])
    sorted_right = sorted([int(x) for x in list(right)])
    # sum_list = [sorted_left[a] - sorted_right[a] for a in range(len(sorted_left))]
    sum_list = list(map(lambda a, b: [a,b], sorted_left, sorted_right))
    sum_breakdown = [g[1] - g[0] for g in [sorted(a) for a in sum_list]]
    return sum(sum_breakdown)


current_location = os.path.dirname(__file__)
read_file = os.path.join(current_location, "Day_1_input.txt")
with open(read_file, "r") as f:
    lines = f.readlines()
    data = [line.strip("\n").split("   ") for line in lines]
    distances = [do_the_thing(item) for item in data]
    print(sum(distances))
