from tkinter import *
import arUco_video

def code2():
    import arUco_video

def sel1():
    global x
    x= var.get()
    selection = "Voce selecionou a entrada " + str(x)
    x=int(x)
    label.config(text = selection)
    code2()


root = Tk()


whatever_you_do = "Kilobots@UFSC"
msg = Message(root, text = whatever_you_do)
msg.config( font=('arial', 24, 'italic'))
msg.pack()

var = IntVar()
R1 = Radiobutton(root, text="Webcam 1", variable=var, value=0,
                  command=sel1)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Webcam 2", variable=var, value=1,
                  command=sel1)
R2.pack( anchor = W )

def close_window(): 
    root.destroy()

button = Button(root, text="Selecionar Entrada", command=close_window)
button.pack()

label = Label(root)
label.config(text = 'Nenhuma entrada selecionada')
label.pack()
root.mainloop()