import random

from laptop_gaming import Laptop_Gaming
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\One.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Two.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Three.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Four.jpg", "D:\\Workspace\\krakedev\\modulo_5\\poo\\img\\Five.jpg"]

        root.title('Ingresar datos')

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text = 'Marca').grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text = 'Procesador').grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text = 'Memoria').grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text = 'Tarjeta grafica').grid(row=3, column=0)
        self.tar_grafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tar_grafica).grid(row=3, column=1)

        ttk.Label(self.root, text = 'Precio').grid(row=4, column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=4, column=1)

        ttk.Button(self.root, text='Agregar laptop', command=self.agregar_laptop).grid(row=5, column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=300, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)

    def agregar_laptop(self):
        nueva_laptop = Laptop_Gaming(self.marca.get(), self.procesador.get(), self.memoria.get(), self.tar_grafica.get(), self.precio.get())
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

app = App(root)
root.mainloop()