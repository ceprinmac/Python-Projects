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


from tkinter import *
import tkinter as tk

# Be sure to import our other modules 
# so we can have access to them
import FileTransfer_main
import FileTransfer_func


def load_gui(self):
    
    # Source UI
    self.lbl_source = tk.Label(self.master, text="Select Source Folder:")
    self.lbl_source.grid(row=0,column=0,padx=(30,0),pady=(30,5),sticky='news')
    self.txt_source = tk.Entry(self.master, textvariable=self.varSource, width=30)
    self.txt_source.grid(row=1,column=0,padx=(10,0),pady=(5,5),sticky='news')
    self.btn_source = tk.Button(self.master, text="Browse", command=lambda: FileTransfer_func.select_source_folder(self))
    self.btn_source.grid(row=2,column=0,padx=(10,0),pady=(5,5),sticky='news')

    # Destination UI
    self.lbl_destination = tk.Label(self.master, text="Select Destination Folder:")
    self.lbl_destination.grid(row=4,column=0,padx=(30,0),pady=(30,5),sticky='news')
    self.txt_destination = tk.Entry(self.master, textvariable=self.varDestination, width=30)
    self.txt_destination.grid(row=5,column=0,padx=(10,0),pady=(5,5),sticky='news')
    self.btn_destination = tk.Button(self.master, text="Browse", command=lambda: FileTransfer_func.select_destination_folder(self))
    self.btn_destination.grid(row=6,column=0,padx=(10,0),pady=(5,5),sticky='news')

    # Check File UI
    self.btn_source = tk.Button(self.master, text="Start File Check", command=lambda: FileTransfer_func.perform_file_check(self))
    self.btn_source.grid(row=8,column=0,padx=(10,0),pady=(30,5),sticky='news')
    
    
    

    



if __name__ == "__main__":
    pass
