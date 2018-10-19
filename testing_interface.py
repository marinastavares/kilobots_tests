from tkinter import *
import arUco_video

def code2():
    import arUco_video

def sel1():
    global x
    x= var.get()
    selection = "You selected the option " + str(x)
    x=int(x)
    label.config(text = selection)
    code2()

def sel2():
    global x
    x= var.get()
    selection1 = "You selected the option " + str(x)
    label.config(text = selection1)
    print(selection1)



root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Webcam 1", variable=var, value=0,
                  command=sel1)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Webcam 2", variable=var, value=1,
                  command=sel2)
R2.pack( anchor = W )

def close_window(): 
    root.destroy()

button = Button(root, text="QUIT", fg="red",command=close_window)
button.pack()

label = Label(root)
label.pack()
root.mainloop()