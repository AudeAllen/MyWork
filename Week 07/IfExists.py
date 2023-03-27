# I am assuming that os is already imported
import os
filename = 'test.txt'
if os.path.exists(filename):
    print (filename, "already exists")
else:
    print(filename, "does not exist do you want to create it?")