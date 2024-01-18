from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="black")
window.configure(themebg="black")
window.title('Calculator')
window.geometry("400x140")
var = StringVar()
result = ""
s = ttk.Style()
s.configure('.', font=('Helvetica', 12))

def clear():
    global result
    var.set("")
    result = ""
def press(num):
    global result
    result = result + str(num)
    var.set(result)
def equalpress():
    try:
        global result
        total = str(eval(result))
        var.set(total)
        result = ""
    except:
        var.set('error')
        result = ""
entry1 = ttk.Entry(window, width=40, font=("Arial",13), text=var)
entry1.grid(column=0, row=0, columnspan=5)

btn1 = ttk.Button(window, text="1", width=7, command=lambda:press(1))
btn1.grid(column=0, row=1)

btn2 = ttk.Button(window, text="2", width=7, command=lambda:press(2))
btn2.grid(column=1, row=1)

btn3 = ttk.Button(window, text="3", width=7, command=lambda:press(3))
btn3.grid(column=2, row=1)

btn4 = ttk.Button(window, text="4", width=7, command=lambda:press(4))
btn4.grid(column=0, row=2)

btn5 = ttk.Button(window, text="5", width=7, command=lambda:press(5))
btn5.grid(column=1, row=2)

btn6 = ttk.Button(window, text="6", width=7, command=lambda:press(6))
btn6.grid(column=2, row=2)

btn7 = ttk.Button(window, text="7", width=7, command=lambda:press(7))
btn7.grid(column=0, row=3)

btn8 = ttk.Button(window, text="8", width=7, command=lambda:press(8))
btn8.grid(column=1, row=3)

btn9 = ttk.Button(window, text="9", width=7, command=lambda:press(9))
btn9.grid(column=2, row=3)

btn10 = ttk.Button(window, text="0", width=7, command=lambda:press(0))
btn10.grid(column=1, row=4)

btn11 = ttk.Button(window, text="*", width=7, command=lambda:press("*"))
btn11.grid(column=3, row=1)

btn12 = ttk.Button(window, text="/", width=7, command=lambda:press("/"))
btn12.grid(column=3, row=2)

btn13 = ttk.Button(window, text="-", width=7, command=lambda:press("-"))
btn13.grid(column=3, row=3)

btn14 = ttk.Button(window, text="+", width=7, command=lambda:press("+"))
btn14.grid(column=3, row=4)

Clear = ttk.Button(window, text="X", width=7, command=clear)
Clear.grid(column=0, row=4)

Result = ttk.Button(window, text="=", width=7, command=equalpress)
Result.grid(column=2, row=4)

#btn15 = ttk.Button(window, text="√", width=7, command=lambda:press("√"))
#btn15.grid(column=4, row=0)

btn16 = ttk.Button(window, text="^", width=7, command=lambda:press("**"))
btn16.grid(column=4, row=1)

btn17 = ttk.Button(window, text="(", width=7, command=lambda:press("("))
btn17.grid(column=4, row=2)

btn17 = ttk.Button(window, text=")", width=7, command=lambda:press(")"))
btn17.grid(column=4, row=3)

btn18 = ttk.Button(window, text=",", width=7, command=lambda:press("."))
btn18.grid(column=4, row=4)














window.mainloop()



