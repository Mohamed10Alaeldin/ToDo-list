import tkinter as tk
from tkinter import messagebox
# window is the perant window
window = tk.Tk()
# size and (x, y) points
window.geometry('500x450+600+200')
window.title('First GUI-bases program')
# config use for background color
window.config(bg='#223441')
# resizing is off
window.resizable(0,0)
# --------- functions ------------ #
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(tk.END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    if tk.ANCHOR:
        lb.delete(tk.ANCHOR)
    else:
        messagebox.showwarning("warning", "Please select some task.")
def updateTask():
    task = my_entry.get()
    if tk.ANCHOR and task != "":
        deleteTask()
        lb.insert(tk.ANCHOR, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please select some task.")

        
def Enter_key_pressed(event):
    updateTask()
def Delete_key_pressed(event):
    deleteTask()

# frame to hold the widgets
frame = tk.Frame(window)
# extra padding around frame from outside
frame.pack(pady = 10)
lb = tk.Listbox(
    frame, # Listbox is placed on the frame window.
    width=25,
    height=8,
    font=('Times', 18),
    bd=0, # border is zero
    fg='#464646', # text color
    highlightthickness=0,
    selectbackground='#a6a6a6', # color of the focused item in the Listbox.
    activestyle="none",  
)

lb.pack(side=tk.LEFT, fill=tk.BOTH)
sb = tk.Scrollbar(frame)
sb.pack(side=tk.RIGHT, fill=tk.BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = tk.Entry(
    window,
    font=('times', 24)
    )
my_entry.pack(pady=20)
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

addTask_btn = tk.Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command= newTask
)
addTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

delTask_btn = tk.Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command= deleteTask
)
delTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

updTask_btn = tk.Button(
    button_frame,
    text='Update Task',
    font=('times 14'),
    bg='orange',
    padx=20,
    pady=20,
    command= updateTask
)
updTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

file1 = open("Database.txt", "r")
while True:
    task = file1.readline()
    if not task:break
    lb.insert(tk.END,task)
file1.close()

def callback():
    f = open("Database.txt","w")
    tasks = list(lb.get(0,tk.END))
    for task in tasks:
        task = task.strip()
        f.write(task)
        f.write("\n")
        
    f.close()
    window.destroy()

window.bind("<Return>",Enter_key_pressed)
window.bind("<Delete>",Delete_key_pressed)
window.protocol("WM_DELETE_WINDOW", callback)
window.mainloop()

