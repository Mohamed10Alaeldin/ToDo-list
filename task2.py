from tkinter import *
win = Tk() 
win.geometry("350x400+600+200")
win.resizable(0, 0)
win.title("Calculator")
# <------ ~funtions of buttons~ -------->

# whenever insertion button is clicked
def btn_click(item):
    global expression
    expression += item
    input_text.set(expression)
# reset 
def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("0")
# when the user clicks on Return key (Enter <--)
def Enter_key_pressed(event):
    bt_equal() # redirected to equals function
# do the math
def bt_equal():
    global expression
    expression = input_text.get()
    # check if the expression is valid or not
    try:
        result = str(eval(expression)) # convert the expression string to result
        input_text.set(result) # print the result on input_text
    except:
        input_text.set("Invalid")
    expression = ""

# ------------- initialize --------------
win.bind('<Return>', Enter_key_pressed) # if the user clicks the enter key on keyboard
input_text = StringVar() #used to get the instance of input field
expression = ""
input_text.set("0")

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=0)
input_frame.pack(side=TOP)
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT) 
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) #increase the height of input field 

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

# first row
clear = Button(btns_frame, text = "C", fg = "white", width = 32, height = 3, bd = 0, bg = "#1874CD", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#FFF8DC", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("7")).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("8")).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("9")).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#FFF8DC", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("4")).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("5")).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("6")).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#FFF8DC", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
one = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("1")).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("2")).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("3")).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#FFF8DC", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row
zero = Button(btns_frame, text = "0", fg = "white", width = 21, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "#228B22", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#FF9912", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()