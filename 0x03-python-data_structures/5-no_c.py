#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        new_string = my_string.translate({ord("c"): None})
        next_string = new_string.translate({ord("C"):None})
        return next_string
    return my_string
