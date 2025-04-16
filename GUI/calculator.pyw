from tkinter import Tk, Label, Entry, Button

def fn_sumar():
    num1 = input_1.get()
    num2 = input_2.get()
    result = float(num1) + float(num2)

    input_3.delete(0, 'end')
    input_3.insert(0, result)
    pass

root = Tk()
root.title('Calculator')
root.geometry('450x300')

lbl_1 = Label(root, text='Primer Número')
lbl_1.place(x=10, y=10, width=100, height=30)
input_1 = Entry(root, bg='pink')
input_1.place(x=120, y=10, width=100, height=30)

btn = Button(root, text='Sumar', command=fn_sumar)
btn.place(x=230, y=10, width=80, height=30)

lbl_2 = Label(root, text='Segundo Número')
lbl_2.place(x=10, y=50, width=100, height=30)
input_2 = Entry(root, bg='pink')
input_2.place(x=120, y=50, width=100, height=30)

lbl_3 = Label(root, text='Resultado')
lbl_3.place(x=10, y=90, width=100, height=30)
input_3 = Entry(root, bg='pink')
input_3.place(x=120, y=90, width=100, height=30)

root.mainloop()