#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cc'})
    return new_string
