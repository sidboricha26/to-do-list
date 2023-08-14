import tkinter
#Import tkinker library
from tkinter import *

#Create an instance of tkinter frame or window
root = Tk()
#Set the title of the frame
root.title("TO-DO LIST")
#Set the geometry of tkinter frame
root.geometry("450x630")
root.resizable(False, False)

task_list = []

#icon
Image_icon = PhotoImage(file="Images/task.png")
root.iconphoto(False, Image_icon)

#top bar
TopImage = PhotoImage(file="Images/topbar.png")
Label(root, image=TopImage).pack()

root.mainloop()