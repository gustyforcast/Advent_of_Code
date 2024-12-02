
# Part 1

with open('Day_1_input.txt', 'r') as f:
    d = f.read().split('\n\n')
    cal = [h.split('\n') for h in d]

    out_list = []
    for l in cal:
        out_list.append([])
        for b in l:
            out_list[-1].append(int(b))

    elf_dict = {}
    top_elf = 0
    index = 0
    top_cal = 0
    for elf in out_list:
        elf_sum = 0
        for food in elf:
            elf_sum += food

        elf_dict[elf_sum] = index

        if elf_sum > top_cal:
            top_elf = index
            top_cal = elf_sum
        index += 1

    print(f'Elf Index: {index}')
    print(f'Calories: {top_cal}')

    ordered_cals = sorted(list(elf_dict.keys()), reverse=True)
    total_cals = 0
    for i in ordered_cals[:3]:
        total_cals += i

    print(f'Total Calories: {total_cals}')



