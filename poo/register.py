import tkinter as tk
import random
from tkinter import ttk
from laptop_business import Laptop_Business
from PIL import Image, ImageTk

class Register:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\One.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Two.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Three.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Four.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Five.jpg"]

        root.title('Registrar laptop')
        root.geometry('800x500')

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text='Marca:', anchor='e').place(relx=.01, rely=.01, relwidth=0.25, relheight=.06)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca, width=20).place(relx=0.28, rely=.01, relwidth=.25, relheight=.06)

        ttk.Label(self.root, text='Procesador:', anchor='e').place(relx=.01, rely=.08, relwidth=0.25, relheight=.06)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador, width=20).place(relx=0.28, rely=.08, relwidth=0.25, relheight=.06)

        ttk.Label(self.root, text='Memoria RAM:', anchor='e').place(relx=.01, rely=0.15, relwidth=0.25, relheight=.06)
        self.memoria_ram = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria_ram, width=20).place(relx=0.28, rely=0.15, relwidth=0.25, relheight=.06)

        ttk.Label(self.root, text='Tarjeta Grafica:', anchor='e').place(relx=.01, rely=0.22, relwidth=0.25, relheight=.06)
        self.tarjeta_grafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tarjeta_grafica, width=20).place(relx=0.28, rely=0.22, relwidth=0.25, relheight=.06)
        
        ttk.Label(self.root, text='Precio:', anchor='e').place(relx=.01, rely=0.29, relwidth=0.25, relheight=.06)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio, width=20).place(relx=0.28, rely=0.29, relwidth=0.25, relheight=.06)

        ttk.Button(self.root, text='Agregar laptop', command=self.agregar_laptop).place(relx=0.38, rely=0.37, relwidth=0.15, relheight=0.06)

        self.mostrar_laptops = tk.Text(self.root)
        self.mostrar_laptops.place(relx=0.08, rely=0.45, relwidth=0.45, relheight=0.40)

        self.canva = tk.Canvas(self.root, bg='lightblue')
        self.canva.place(relx=0.55, rely=0.45, relwidth=0.36, relheight=0.40)
                
    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria_ram.get(), self.tarjeta_grafica.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f'{nueva_laptop}')
        self.mostrar_imagen_aleatoria()

    def mostrar_imagen_aleatoria(self):
        imagen_path = random.choice(self.imagenes)
        image = Image.open(imagen_path)
        image = image.resize((290, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.canva.create_image(0, 0, anchor=tk.NW, image = photo)
        self.canva.image = photo


root = tk.Tk()
app = Register(root)
root.mainloop()