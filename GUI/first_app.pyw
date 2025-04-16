from tkinter import Tk, Label, Button

def mensaje():
    print('Este es el mensajede un boton...')

root = Tk()
root.title('Hola Mundo!')
root.geometry('500x300')

lbl = Label(root, text='Este es un input')
lbl.pack()

btn = Button(root, text='Presioname', bg='orange', command=mensaje)
btn.pack()

root.mainloop()