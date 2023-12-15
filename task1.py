import tkinter as tk
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

task_list = ['Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation about project',
    'take a nap',
    'Learn something',
    'paint canvas',
    'listen to recitition',
    "read for exams",
    "revise math rulus",
    "revise math rulus",
    "revise math rulus",
    "revise math rulus",
    "revise math rulus",
    "revise math rulus"
    ]


for item in task_list:
    lb.insert(tk.END, item) # end means add the item to (end of the list)
sb = tk.Scrollbar(frame)
sb.pack(side=tk.RIGHT, fill=tk.BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = tk.Entry(
    window,
    font=('times', 24)
    )

my_entry.pack(pady=20)
window.mainloop()
