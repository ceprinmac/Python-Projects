
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

import os
import tkinter as tk
from tkinter import filedialog, messagebox  
import shutil
import os
import time

# Be sure to import our other modules 
# so we can have access to them
import FileTransfer_gui
import FileTransfer_main


# Function to select the source folder  
def select_source_folder(self):  
    folder = filedialog.askdirectory()  
    if folder:  
        self.varSource.set(folder)  

# Function to select the destination folder  
def select_destination_folder(self):  
    folder = filedialog.askdirectory()
    if folder:  
        self.varDestination.set(folder)  

# Function to perform the file check process  
def perform_file_check(self):  
    source_folder = self.varSource.get()  
    destination_folder = self.varDestination.get()
    files = os.listdir(source_folder)
    
    if not source_folder or not destination_folder:  
        messagebox.showerror("Error", "Please select both source and destination folders.")  
        return  
    
    # Displaying for checking files and copying  
    messagebox.showinfo("File Check", f"Checking files in {source_folder}\n"   
                                       f"Copying to {destination_folder}")  
    # Get the current time  
    currentTime = time.time()  

    for filename in files:
        #we are saying move the files represented by 'filename' to their new destination
        filePath = os.path.join(source_folder, filename)

        # Check if it's a file (not a directory)  
        if os.path.isfile(filePath):  
            # Get the last modified time of the file  
            lastModifiedTime = os.path.getmtime(filePath)

            # Check if the file is new or modified in the last 24 hours (86400 seconds)  
            if (currentTime - lastModifiedTime) < 86400:  
                # Copy the file to the destination folder  
                shutil.copy(filePath, destination_folder)  
                print(f'Copied: {filename}')

    messagebox.showinfo("File Check", "File copying process completed.")





if __name__ == "__main__":
    pass
