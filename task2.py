import sys

def sum2biggest (list):
    first = None
    second = None

    for v in list:
        if first == None:
            first = v
        elif v >= first:
            second = first
            first = v
        elif second == None or second < v:
            second = v
    
    return first + second
