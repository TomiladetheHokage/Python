# Looking at some methods in the os module

import os
import datetime

os.rename("new file", "file")
if os.path.exists("file"):
    print("File name has been changed")

file = open("temp file", "w")
file.write("some text")
file.close()

os.remove("temp file")
print("new file has been removed")

print(os.path.exists("lyric"))
print(os.path.getsize("guests")) #returns size in bytes

time = os.path.getmtime("guests")
timer = datetime.datetime.fromtimestamp(time)
print(timer)