#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_key = list(rom_num.keys())

    digit = 0
    last_r = 0
    list_digit = [0]

    for i in roman_string:
        for j in list_key:
            if j == i:
                if rom_num.get(i) <= last_r:
                    digit += to_subtract(list_digit)
                    list_digit = [rom_num.get(i)]
                else:
                    list_digit.append(rom_num.get(i))

                last_r = rom_num.get(i)

    digit += to_subtract(list_digit)

    return (digit)
