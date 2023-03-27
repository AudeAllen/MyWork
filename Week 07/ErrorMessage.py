FILENAME = "Count.txt"


def readNumber():
 try:
    with open(FILENAME) as f:
        number = int(f.read())
        return number
        print({number})

 except IOError:
 # this file will be created when we write back.
 # no file assumes first time running
 # ie 0 previous runs
    return 0
    print("sddslkdslkdslkkds")



