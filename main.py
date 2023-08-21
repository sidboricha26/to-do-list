import tkinter
#Import tkinker library
from tkinter import *

#Create an instance of tkinter frame or window
root = Tk()
#Set the title of the frame
root.title("TO-DO LIST")
#Set the geometry of tkinter frame
root.geometry("720x500+400+100") # width x height + x + y
#Set width and height as false to make the window of fixed size
root.resizable(False, False) #(width, height)

task_list = []

# call function when you want to add a task to the tasklist
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
# call function when you want to delete a task from the tasklist
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
             tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file=open('tasklist.txt', 'w')
        file.close()

# call function when we click on entry box
def click(*args):
    task_entry.configure(state=NORMAL)
    task_entry.delete(0, 'end')

#icon
Image_icon = PhotoImage(file="Images/task.png")
root.iconphoto(False, Image_icon)

#header part with heading and images
frame2 = Frame(root, width=720, height=90, bg="#2c698d")

#heading
heading = Label(root, text="ALL TASK", font="Goldplay 30 bold", fg="white", bg="#2c698d")
heading.place(x=260, y=20)

#images
dockImage = PhotoImage(file="Images/dock.png")
Label(root, image=dockImage, bg='#2c698d').place(x=50, y=35)
noteImage = PhotoImage(file="Images/task.png")
Label(root, image=noteImage, bg='#2c698d').place(x=620, y=25)

frame2.pack()

#main #textfield
frame = Frame(root, width=280, height=50, bg="white")
frame.place(x=425, y=150)

task = StringVar()
task_entry = Entry(frame, width=18, font="Goldplay 20", bd=3, relief="ridge")
#Add text in Entry box
task_entry.insert(0, 'Enter your task.....')
task_entry.configure(state=DISABLED)
task_entry.place(x=10, y=7)
task_entry.focus()
# Use bind method
task_entry.bind("<Button-1>", click)

button = Button(frame, text="ADD", font="Goldplay 25 bold", width=10, bg="#6380da", fg="#fff", bd=0, command=addTask)
button.pack(pady=100, padx=42)

#listbox
frame1 = Frame(root, bd=3, width=20, height=30, bg="#32405b")
frame1.pack(side=LEFT, padx=8)

listbox = Listbox(frame1, font=("Goldplay", 15), width=35, height=15, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff", borderwidth=3, relief="ridge")
listbox.pack(side = LEFT, fill=BOTH)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand= scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon = PhotoImage(file="Images/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side= BOTTOM, padx= 100, pady= 90)

root.mainloop()