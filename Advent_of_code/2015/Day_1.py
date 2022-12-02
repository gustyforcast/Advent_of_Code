import re

up_count, down_count = 0,0

with open('Day_1input.txt', 'r') as f:
    # for item in f.read():
    #     if item == ')':
    #         down_count += 1
    #     elif item == '(':
    #         up_count += 1
    #     else:
    #         print('Error')
        
    # # print(up_count-down_count)


    current_location = 0
    index = 0
    for item in f.read():
        if current_location == -1:
            print(index)
            break
        if item == ')':
            current_location -= 1
        elif item == '(':
            current_location += 1
        else:
            print('Error')
        index += 1


