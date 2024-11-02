import os

directory = "new dir"
for name in os.listdir(directory):
    fullname = os.path.join(directory, name)
    if os.path.isdir(fullname):
        print("{} is dir".format(fullname))
    else:
        print("{} is a file".format(fullname))
