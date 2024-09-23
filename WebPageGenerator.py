#
# Python Ver:   3.12.6
#
# Author:       Prince M. Macaldo
#
# Purpose:      Creates a GUI that allows the user to input text and
#               initiate the web page generation process 
#
#               Web Page Generator Assignment (The Tech Academy)



import webbrowser
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        # define our master frame configuration
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 200))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varBody = StringVar()
        
        self.lblFName = Label(self.master,text='New heading: ', font=("Helvetica", 12), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,5), sticky=W)
        
        self.txtBody = Entry(self.master, text=self.varBody, width=50, font=("Helvetica", 12), fg='white', bg='darkgray')
        self.txtBody.grid(row=1,column=0, padx=(30,0),pady=(5,0),sticky=N+E+S+W)

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=6, column=0, padx=(0,0), pady=(30,0), sticky=NE)

    
    def submit(self):
        # getting the input from the user
        head = self.varBody.get()
        # adding the html code
        html = "<html><body><h1> {} </h1></body></html>".format(head)
        # overwrite the html file
        f = open("index.html", "w")
        f.write("{}".format(html))
        f.close()
        # open in new tab
        webbrowser.open_new('index.html')




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
