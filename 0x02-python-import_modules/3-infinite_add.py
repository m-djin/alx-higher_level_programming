#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumnum = 0
    for i in range(1, len(argv)):
        sumnum += int(argv[i])
    print("{}".format(sumnum))
