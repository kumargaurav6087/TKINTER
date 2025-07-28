'''
# Tkinter - it helps to create GUI applications (Graphical user interface)

# Hello world
# step 1: import tkinter
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
inp = Label(window , text = "Hello world!")
inp.pack()

# step 4: main loop
window.mainloop()


# Basic modification using tkinter
# step 1: import tkinter
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
window.title("simple")
window.geometry("500x700")
window.config(bg="yellow")

# step 4: main loop
mainloop()


# Frames and buttons using tkinter
# step 1: import tkinter
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
window.title("simple")
window.geometry("500x700")
window.config(bg="black")
frame1 = Frame(window  , width=300 ,height=300 , cursor="dot")
frame2 = Frame(window , width=300 ,height=300 , cursor="dotbox")

button1 = Button(frame1 , text = "button1", bg = "blue")
button2 = Button(frame2 , text = "button2", bg = "red")
button3 = Button(frame1 , text = "login" , fg ="red")

frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)
button1.pack()
button2.pack()
button3.pack()

# step 4: main loop
mainloop()


# Entry box and grid layout
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
window.title("simple")
window.geometry("250x50")
label1 = Label(window,text = "mail")
label2 = Label(window,text = "password")

e1 = Entry(window, width =40 , borderwidth = 5)
e2 = Entry(window, width =40 , borderwidth = 5)

label1.grid(row = 0 , column =1)
label2.grid(row = 1, column =1 )
e1.grid(row = 0 , column = 2)
e2.grid(row = 1 , column = 2)
# step 4: main loop
mainloop()


# Pack

from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
window.title("simple")
window.geometry("500x5000")
label1 = Label(window, text = "Label-1", bg ="black" ,fg = "red")
label2 = Label(window, text = "Label-2", bg ="blue" ,fg = "red")
label3 = Label(window, text = "Label-3", bg ="green" ,fg = "red")


label1.pack(side = TOP , fill = X , expand = False)
label2.pack(side = LEFT , fill = Y , expand = False)
label3.pack(side = RIGHT , fill = Y , expand = False)

# step 4: main loop
mainloop()


# Handling buttons
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
window.title("simple")
window.geometry("500x500")
def log_entry():
    print("Logged in")

button1 = Button(window,text = "LOGIN" , command = log_entry , width = 12 , bg = "red" , fg = "blue" , font = ("bold",12) , activebackground= "black" , activeforeground="white"  )
button1.pack()

# step 4: main loop
mainloop()


# Menubar
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs

menu = Menu(window)
#file = Menu(menu,tearoff= 1)
file = Menu(menu,tearoff= 0)
file.add_command(label = "New")
file.add_command(label = "Open")
file.add_command(label = "Save")
file.add_command(label = "Save as")
file.add_separator()
file.add_command(label = "Exit" , command= window.quit)
menu.add_cascade(label = "File" , menu = file)
window.config(menu = menu)

# step 4: main loop
mainloop()

# step 1: import tkinter
from tkinter import*
import tkinter.messagebox
# step 2: gui interaction
window = Tk()
# step 3: adding inputs
#tkinter.messagebox.showinfo("info","Running out time")
#tkinter.messagebox.showerror("info","Running out time")
tkinter.messagebox.showwarning("info","Running out time")
#question = tkinter.messagebox.askyesno("Weather","Will it rain")
#question = tkinter.messagebox.askokcancel("Weather","Will it rain")
question = tkinter.messagebox.askretrycancel("Weather","Will it rain")
if question == True:
    print("Take an Umbrella")

else:
    print("Okay")

# step 4: main loop
mainloop()

# Drawing

# step 1: import tkinter
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
c = Canvas(window,width = 500 , height= 500)
c.pack()
c.create_line(0,0,500,500 , width = 5 , fill = "black" , dash = (3,3))
c.create_line(0,500,500,0 , width = 5 , fill = "black" , dash = (3,3))
c.create_rectangle(150,240,450,150 , fill = "red" , outline = "Yellow" , width = 5)

# step 4: main loop
mainloop()


# How to create message box in a window

# step1 : import tkinter
from tkinter import*

# step2: gui interafce
window = Tk()

# step3: adding inputs
window.geometry("500x500")
#message = Message(window, text ="Python")
#message.pack()


#var = StringVar()
#message = Message(window,textvariable = var , relief = RAISED , padx = 20 , pady=20)
#var.set("window")
#message.pack()

var = StringVar()
ent_var = StringVar()
def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window,textvariable=var , relief=RAISED , padx=50, pady=50)
entry = Entry(window, textvariable=ent_var)
button = Button(window, text = "Ok" , command = insert )
message.pack()
entry.pack()
button.pack()

# step4 : main loop
mainloop()


# Check box

# step 1: import tkinter
from tkinter import*

# step 2: gui interaction
window = Tk()

# step 3: adding inputs
window.geometry("500x500")
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()

checkb1 = Checkbutton(window,text="apple" , onvalue=1 , offvalue=0 , height=2 , width = 10)
checkb2 = Checkbutton(window,text="mango" , onvalue=1 , offvalue=0 , height=2 , width = 10)
checkb3 = Checkbutton(window,text="Plum" , onvalue=1 , offvalue=0 , height=2 , width = 10)

checkb1.pack()
checkb2.pack()
checkb3.pack()
# step 4: main loop
mainloop()

# place
# step1 : import tkinter
from tkinter import*

# step2: gui interface
window = Tk()

# step3: adding inputs
window.geometry("500x500")
button = Button(window,text = "Button", width = 12)
button.place(x= 200, y =250)
# step4: mainloop
mainloop()
'''



