import os.path
FILENAME = "count.txt"

def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number))


if not os.path.isfile(FILENAME):
 print ("File does not exist")
 #initialise file here
writeNumber(0)


def readNumber():
 try:
    with open(FILENAME) as f:
        number = int(f.read())

 except IOError:
 # this file will be created when we write back.
 # no file assumes first time running
 # ie 0 previous runs
    return 0
    Print("there has been an Error")




