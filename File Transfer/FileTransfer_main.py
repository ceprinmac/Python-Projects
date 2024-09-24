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
from tkinter import filedialog as fd

# other modules
import FileTransfer_gui
import FileTransfer_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(200,350) #(Height, Width)
        self.master.maxsize(200,350)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        # Variables to hold folder paths  
        self.varSource = StringVar()  
        self.varDestination = StringVar()

        FileTransfer_gui.load_gui(self)










if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
