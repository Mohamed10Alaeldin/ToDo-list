import tkinter as tk
from tkinter import messagebox
# window is the perant window
window = tk.Tk()
# size and (x, y) points
window.geometry('500x450+500+200')
window.title('First GUI-bases program')
# config use for background color
window.config(bg='#223441')
# resizing is off
window.resizable(width=False, height=False)
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
# task_list = ['Eat apple',
#     'drink water',
#     'go gym',
#     'write software',
#     'write documentation about project',
#     'take a nap',
#     'Learn something',
#     'paint canvas',
#     'listen to recitition',
#     "read for exams",
#     "revise math rulus"
#     ]


# for item in task_list:
#     lb.insert(tk.END, item) # end means add the item to (end of the list)
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

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(tk.END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

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

def deleteTask():
    if tk.ANCHOR:
        lb.delete(tk.ANCHOR)
    else:
        messagebox.showwarning("warning", "Please select some task.")

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
window.mainloop()
