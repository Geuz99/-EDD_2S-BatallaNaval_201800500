from os import remove
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import requests
import shutil
from subprocess import check_call
from graphviz import dot

base_url = 'http://192.168.1.9:18080'


class AdminPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1116x718')
        # self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title("EDD-ADMIN")
        self.window.iconbitmap('Imagenes\\icono.ico')
        self.window.protocol("WM_DELETE_WINDOW", self.salir)

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\bg1.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # FRAME BOTONES USUARIOS
        self.btsUsers_frame = Frame(self.window, bg='#809fff', width='450', height='800')
        self.btsUsers_frame.place(x=0, y=0)

        # FRAME SUBRAYADO
        self.subra = Frame(self.btsUsers_frame, bg='black', width='450', height='10')
        self.subra.place(x=0, y=45)

        # USER IMAGEN
        self.user_image = Image.open('Imagenes\\user.png')
        photo = ImageTk.PhotoImage(self.user_image)
        self.user_image_label = Label(self.btsUsers_frame, image=photo, bg='#809fff')
        self.user_image_label.image = photo
        self.user_image_label.place(x=195, y=110)

        # TEXTO NOMBRE DE USUARIO
        self.txt = 'USUARIO: EDD - Administrador'
        self.heading = Label(self.btsUsers_frame, text=self.txt, font=('yu gothic ui', 22, 'bold'), bg='#809fff',
                             fg='white')
        self.heading.place(x=0.5, y=7, width=450, height=35)

        # TEXTO LISTADO
        self.txt = 'LISTADO DE USUARIOS'
        self.heading = Label(self.btsUsers_frame, text=self.txt, font=('yu gothic ui', 13), bg='#809fff',
                             fg='white')
        self.heading.place(x=3, y=190, width=450, height=85)

        # BOTON DE USUARIOS ORDENADOS ASCENDENTE
        self.ascendente_button = Image.open('Imagenes\\btn1.png')
        photo = ImageTk.PhotoImage(self.ascendente_button)
        self.ascendente_button_label = Label(self.btsUsers_frame, image=photo, bg='#809fff')
        self.ascendente_button_label.image = photo
        self.ascendente_button_label.place(x=70, y=270)

        self.ascendente = Button(self.ascendente_button_label, text='Ascendente', bg='#3047ff', fg='white',
                                 font=('yu gothic ui', 12, 'bold'), width=25, bd=0, cursor='hand2',
                                 activebackground='#3847ff', command=self.ascendente)
        self.ascendente.place(relx=0.5, rely=0.5, anchor=CENTER)

        # BOTON DE USUARIOS ORDENADOS DESCENDENTE
        self.descendente_button = Image.open('Imagenes\\btn1.png')
        photo = ImageTk.PhotoImage(self.descendente_button)
        self.descendente_button_label = Label(self.btsUsers_frame, image=photo, bg='#809fff')
        self.descendente_button_label.image = photo
        self.descendente_button_label.place(x=70, y=350)

        self.descendente = Button(self.descendente_button_label, text='Descendente', bg='#3047ff', fg='white',
                                  font=('yu gothic ui', 12, 'bold'), width=25, bd=0, cursor='hand2',
                                  activebackground='#3847ff', command=self.descendente)
        self.descendente.place(relx=0.5, rely=0.5, anchor=CENTER)

        # TEXTO GRAFICA
        self.txt = 'GRAFICA'
        self.heading = Label(self.btsUsers_frame, text=self.txt, font=('yu gothic ui', 13), bg='#809fff',
                             fg='white')
        self.heading.place(x=3, y=420, width=450, height=85)

        # BOTON DE GENERAR ARBOL B
        self.arbol_button = Image.open('Imagenes\\btn1.png')
        photo = ImageTk.PhotoImage(self.arbol_button)
        self.arbol_button_label = Label(self.btsUsers_frame, image=photo, bg='#809fff')
        self.arbol_button_label.image = photo
        self.arbol_button_label.place(x=70, y=490)

        self.arbol = Button(self.arbol_button_label, text='Generar Arbol b', bg='#3047ff', fg='white',
                            font=('yu gothic ui', 12, 'bold'), width=25, bd=0, cursor='hand2',
                            activebackground='#3847ff', command=self.arbolb)
        self.arbol.place(relx=0.5, rely=0.5, anchor=CENTER)

        # BOTON DE SALIR
        self.salir = Button(self.btsUsers_frame, text='Salir', bg='#990000', fg='white',
                            font=('yu gothic ui', 12, 'bold'), width=10, bd=0, cursor='hand2',
                            activebackground='#3847ff', command=self.salir2)
        self.salir.place(x=175, y=650)

        # LOS USUARIOS
        self.configfile = Text(self.window, wrap=WORD)
        self.configfile.place(x=540, y=75, width=520, height=590)

    def ascendente(self):
        self.configfile.delete("1.0","end")
        res = requests.get(f'{base_url}/usuarios/ascendente')
        data = res.text
        with open('Usuarios Ascendentes', 'w') as f:
            f.write(data)
        with open('Usuarios Ascendentes', 'r') as f:
            self.configfile.insert(INSERT, f.read())

    def descendente(self):
        self.configfile.delete("1.0","end")
        res = requests.get(f'{base_url}/usuarios/descendente')
        data = res.text
        with open('Usuarios Descendentes', 'w') as f:
            f.write(data)
        with open('Usuarios Descendentes', 'r') as f:
            self.configfile.insert(INSERT, f.read())

    def arbolb(self):
        res = requests.get(f'{base_url}/arbolb')
        data = res.text
        shutil.copy(data, 'arbolb.dot')
        check_call(['dot', '-Tpng', 'arbolb.dot', '-o', 'arbolb.png'])
        img = Image.open('arbolb.png')
        img.show()

    def salir(self):
        res = messagebox.askquestion("Salir", "Estas seguro que quieres salir de la aplicacion?")
        if res == 'yes':
            try:
                remove("Usuarios Ascendentes")
                remove("Usuarios Descendentes")
                remove('arbolb.dot')
                remove('arbolb.png')
            except FileNotFoundError as e:
                print(e)
                exit(0)
        elif res == 'no':
            print('no')

    def salir2(self):
        self.window.destroy()
