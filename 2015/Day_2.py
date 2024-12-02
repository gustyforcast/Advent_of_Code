
total = 0

with open('Day_2input.txt', 'r') as f:
    lines = f.readlines()

    for present in lines:
        wrap = present.strip('\n').split('x')
        w = int(wrap[0])
        h = int(wrap[1])
        l = int(wrap[2])

        total += (2*l*w + 2*w*h + 2*h*l)
    
    print(total)