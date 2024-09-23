#
# Python Ver:   3.12.6
#
# Author:       Prince M. Macaldo
#
# Purpose:      The purpose of the provided code is
#               to automate the task of copying new or
#               recently modified files from the source folder
#               to the destination folder once per day,
#               saving you time and manpower.
#
#               File Transfer Assignment (The Tech Academy)



import shutil
import os
import time

# Set where the source of the files are
source = 'C:/Users/user/Desktop/Development/Python-Projects/folderA/'

# Set the destination path to folderB
destination = 'C:/Users/user/Desktop/Development/Python-Projects/folderB/'
files = os.listdir(source)

# Get the current time  
currentTime = time.time()  

for filename in files:
    #we are saying move the files represented by 'filename' to their new destination
    filePath = os.path.join(source, filename)

    # Check if it's a file (not a directory)  
    if os.path.isfile(filePath):  
        # Get the last modified time of the file  
        lastModifiedTime = os.path.getmtime(filePath)

        # Check if the file is new or modified in the last 24 hours (86400 seconds)  
        if (currentTime - lastModifiedTime) < 86400:  
            # Copy the file to the destination folder  
            shutil.copy(filePath, destination)  
            print(f'Copied: {filename}')  

print("File copying process completed.")
