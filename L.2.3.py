my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
first_number = 0
while first_number <= len(my_list):
    if my_list[first_number] == 0:
        first_number += 1
        continue
    elif my_list[first_number] > 0:
        print(my_list[first_number])
        first_number += 1
    else:
        break