import tkinter
#Import tkinker library
from tkinter import *

#Create an instance of tkinter frame or window
root = Tk()
#Set the title of the frame
root.title("TO-DO LIST")
#Set the geometry of tkinter frame
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

#icon
Image_icon = PhotoImage(file="Images/task.png")
root.iconphoto(False, Image_icon)

#top bar
TopImage = PhotoImage(file="Images/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="Images/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="Images/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

#main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=2)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0)
button.place(x=300, y=0)

#listbox
frame1 = Frame(root, bd=3, width=700, height=200, bg="#32405b")
frame1.pack(pady=(168, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height= 16, bg="#32405b")
listbox.pack(side = LEFT, fill=BOTH, padx=2)


root.mainloop()