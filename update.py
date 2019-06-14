# updatefilenamesinafolder
This script is used to update all the file names inside a folder.

import os

path = 'Your Path goes here'

new_name = "New file name"

for file in os.listdir(path):

    dst = new_name + file.split("-")[-1]
    src = path + file
    dst = path + dst
    os.rename(src,dst)

print("Completed all files!!!")
