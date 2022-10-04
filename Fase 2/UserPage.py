from os import remove
from tkinter import *
from tkinter import simpledialog, messagebox
from Matriz import Matriz

from PIL import ImageTk, Image
import requests

base_url = 'http://192.168.1.9:18080'


class UserPage:
    def __init__(self, window, user, password):
        self.window = window
        self.user = user
        self.password = password
        self.window.geometry('1116x718')
        self.window.resizable(0, 0)
        self.window.title('Profile: ' + user)
        self.window.iconbitmap('Imagenes\\icono.ico')
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\bg1.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # FRAME BOTONES USUARIOS
        self.btsUsers_frame = Frame(self.window, bg='#809fff', width='450', height='1080')
        self.btsUsers_frame.place(x=0, y=0)

        # FRAME SUBRAYADO
        self.subra = Frame(self.btsUsers_frame, bg='black', width='450', height='10')
        self.subra.place(x=0, y=45)

        # USER IMAGEN
        self.user_image = Image.open('Imagenes\\user.png')
        photo = ImageTk.PhotoImage(self.user_image)
        self.user_image_label = Label(self.btsUsers_frame, image=photo, bg='#809fff')
        self.user_image_label.image = photo
        self.user_image_label.place(x=195, y=90)

        # TEXTO NOMBRE DE USUARIO
        self.txt = 'BIENVENIDO      ' + user
        self.heading = Label(self.btsUsers_frame, text=self.txt, font=('yu gothic ui', 22, 'bold'), bg='#809fff',
                             fg='white')
        self.heading.place(x=0.5, y=7, width=450, height=40)

        # BOTON EDITAR PERFIL
        self.edit_button = Button(self.btsUsers_frame, text='Editar perfil', bg='#1affff', fg='black',
                                  font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                  activebackground='#3847ff', command=self.editar)
        self.edit_button.place(x=65, y=200)

        # BOTON ELIMINAR PERFIL
        self.delete_button = Button(self.btsUsers_frame, text='Eliminar cuenta', bg='#00ff00', fg='black',
                                    font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                    activebackground='#3847ff', command=self.eliminar)
        self.delete_button.place(x=245, y=200)

        # BOTON VER TUTORIAL
        self.tuto_button = Button(self.btsUsers_frame, text='Ver tutorial', bg='#cc33ff', fg='black',
                                  font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                  activebackground='#3847ff', command=self.tuto)
        self.tuto_button.place(x=45, y=330)

        # BOTON VER ARTICULOS DE LA TIENDA
        self.store_button = Button(self.btsUsers_frame, text='Tienda', bg='#ff6600', fg='black',
                                   font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                   activebackground='#3847ff', command=self.store)
        self.store_button.place(x=265, y=330)

        # BOTON REALIZAR MOVIMIENTOS
        self.move_button = Button(self.btsUsers_frame, text='Realizar movimientos', bg='#0000ff', fg='white',
                                  font=('yu gothic ui', 12, 'bold'), width=40, height=2, bd=0, cursor="pirate",
                                  activebackground='#3847ff', command=self.startMoves)
        self.move_button.place(x=44, y=460)

        # BOTON SALIR
        self.move_button = Button(self.btsUsers_frame, text='Salir al menu principal', bg='#ff0000', fg='white',
                                  font=('yu gothic ui', 12, 'bold'), width=40, height=2, bd=0, cursor="pirate",
                                  activebackground='#3847ff', command=self.salir)
        self.move_button.place(x=44, y=540)

        # FRAME LEFT
        self.barra_left = Frame(self.btsUsers_frame, bg='black', width='10', height='850')
        self.barra_left.place(x=0, y=48)

        # FRAME RIGHT
        self.barra_right = Frame(self.btsUsers_frame, bg='black', width='10', height='850')
        self.barra_right.place(x=440, y=48)

        # MOVIMIENTOS
        self.configfile = Text(self.window, wrap=WORD, font=("Comic Sans MS", 20, "bold"))
        self.txt_tuto = 'TUTORIAL'
        self.heading = Label(self.window, text=self.txt_tuto, font=('yu gothic ui', 22), bg='#809fff',
                             fg='white')

        # TIENDA
        self.txt_tienda = 'TIENDA'
        self.tienda = Label(self.window, text=self.txt_tienda, font=('Rockwell', 22), bg='#4d79ff',
                            fg='white')

        # FRAME TIENDA
        self.tienda_frame = Frame(self.window, bg='#4d79ff', width='1060', height='738', highlightbackground="black",
                                  highlightthickness=9)

        # TEXTO TOKEN DISPONIBLE
        self.txt_tokens = 'Tokens Disponibles'
        self.tokens = Label(self.tienda_frame, text=self.txt_tokens, font=('Rockwell', 18), bg='#4d79ff',
                            fg='black')

        # LA TIENDA
        self.configfile_tienda = Text(self.window, wrap=WORD, font=("Comic Sans MS", 30, "bold"))

        # TEXTO CATEGORIA
        self.txt_categoria = 'Seleccione Categoria:'
        self.categoria = Label(self.tienda_frame, text=self.txt_categoria, font=('Rockwell', 13), bg='#4d79ff',
                               fg='black')

        # TEXTO NOMBRE
        self.txt_nombre = 'Seleccione Nombre:'
        self.nombre = Label(self.tienda_frame, text=self.txt_nombre, font=('Rockwell', 13), bg='#4d79ff',
                            fg='black')
        # ENTRY CATEGORIA
        self.categoria_entry = Entry(self.tienda_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                     font=('yu gothic ui', 14, 'bold'))

        # ENTRY NOMBRE ITEM
        self.item_entry = Entry(self.tienda_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                font=('yu gothic ui', 14, 'bold'))

        # BOTON EDITAR PERFIL
        self.comprar_button = Button(self.tienda_frame, text='COMPRAR', bg='#00ff00', fg='red',
                                     font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                     activebackground='#cc6600', command=self.editar)
        self.comprar_button.place(x=65, y=200)

    def store(self):
        self.deletetuto()
        self.window.geometry('1510x785')
        self.tienda = Label(self.window, text=self.txt_tienda, font=('Rockwell', 22), bg='#4d79ff',
                            fg='white')
        self.tienda.place(x=450, y=0, width=1110, height=65)
        self.tienda_frame = Frame(self.window, bg='#4d79ff', width='1060', height='738', highlightbackground="black",
                                  highlightthickness=9)
        self.tienda_frame.place(x=450, y=48)
        self.tokens = Label(self.tienda_frame, text=self.txt_tokens, font=('Rockwell', 18), bg='#4d79ff',
                            fg='black')
        self.tokens.place(x=810, y=0, width=230, height=35)
        self.configfile_tienda = Text(self.window, wrap=WORD, font=("Trajan", 16), bg='#809fff', fg='white')
        self.configfile_tienda.place(x=480, y=110, width=990, height=520)
        self.categoria = Label(self.tienda_frame, text=self.txt_categoria, font=('Rockwell', 13), bg='#4d79ff',
                               fg='black')
        self.categoria.place(x=25, y=610, width=230, height=35)
        self.nombre = Label(self.tienda_frame, text=self.txt_nombre, font=('Rockwell', 13), bg='#4d79ff',
                            fg='black')
        self.nombre.place(x=450, y=610, width=230, height=35)
        self.categoria_entry = Entry(self.tienda_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='white',
                                     font=('yu gothic ui', 14, 'bold'))
        self.categoria_entry.place(x=235, y=610)
        self.item_entry = Entry(self.tienda_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='white',
                                font=('yu gothic ui', 14, 'bold'))
        self.item_entry.place(x=650, y=610)
        self.comprar_button = Button(self.tienda_frame, text='COMPRAR', bg='#00ff00', fg='red',
                                     font=('yu gothic ui', 12, 'bold'), width=10, height=1, bd=0, cursor="pirate",
                                     activebackground='#cc6600', command=self.comprar)
        self.comprar_button.place(x=910, y=610)
        res = requests.get(f'{base_url}/tienda')
        data = res.text
        with open('Tienda', 'w') as f:
            f.write(data)
        with open('Tienda', 'r') as f:
            self.configfile_tienda.insert(INSERT, f.read())

    def editar(self):
        self.deletetuto()
        self.restaurarWin()
        usernew = simpledialog.askstring("USUARIO", "INGRESE SU NUEVO USUARIO", parent=self.window)
        passwordnew = simpledialog.askstring("CONTRASEÑA", "INGRESE SU NUEVA CONTRASEÑA", parent=self.window)
        edadnew = simpledialog.askstring("CONTRASEÑA", "INGRESE SU NUEVA EDAD", parent=self.window)
        res = requests.get(
            f'{base_url}/login/editar/' + self.user + '/' + self.password + '/' + usernew + '/' + passwordnew + '/' + edadnew)
        data = res.text
        if data == 'editado':
            messagebox.showinfo("EDITADO", "El perfil ha sido actualizado correctamente")
            self.txt = 'BIENVENIDO      ' + usernew
            self.heading = Label(self.btsUsers_frame, text=self.txt, font=('yu gothic ui', 22, 'bold'), bg='#809fff',
                                 fg='white')
            self.heading.place(x=0.5, y=7, width=450, height=40)
        else:
            messagebox.showerror("ERROR", "HA OCURRIDO ALGUN ERROR, POR FAVOR INTENTELO DE NUEVO")

    def eliminar(self):
        self.deletetuto()
        self.restaurarWin()
        res = messagebox.askquestion("ATENCION!!!", "Esta a punto de eliminar su cuenta definitivamente. Esta seguro "
                                                    "con la accion que quiere realizar?")
        if res == 'yes':
            messagebox.showwarning("ELIMINADA", "Lamentamos que hallas decidido dejarnos. Esperemos pronto tenerte "
                                                "otra vez de vuelta. Hasta pronto...!")
            self.window.destroy()
        elif res == 'no':
            print('no')
        else:
            messagebox.showwarning('error', 'Occurrio un error al realizar esta accion!')

    def tuto(self):
        self.restaurarWin()
        self.configfile = Text(self.window, wrap=WORD, font=("Comic Sans MS", 20, "bold"))
        self.configfile.place(x=610, y=140, width=350, height=510)
        self.heading = Label(self.window, text=self.txt_tuto, font=('yu gothic ui', 22), bg='#809fff',
                             fg='white')
        self.heading.place(x=455, y=0, width=665, height=85)
        res = requests.get(f'{base_url}/tutorial')
        data = res.text
        with open('Tutorial', 'w') as f:
            f.write(data)
        with open('Tutorial', 'r') as f:
            self.configfile.insert(INSERT, f.read())

    def salir(self):
        try:
            remove("Tutorial")
        except FileNotFoundError as e:
            print(e)
            self.window.destroy()

    def on_closing(self):
        res = messagebox.askquestion("Salir", "Estas seguro que quieres salir de la aplicacion?")
        if res == 'yes':
            exit(0)
        elif res == 'no':
            print('no')

    def startMoves(self):
        self.restaurarWin()
        mxm = simpledialog.askinteger("Input", "INGRESE EL NUMERO DE FILAS DE SU TABLERO", parent=self.window)
        if mxm < 10:
            messagebox.showerror("error", "El tamaño del tablero debe ser mayor a 10")
        if mxm == 10:
            self.tablero1()
        elif 10 < mxm <= 20:
            self.tablero2()
        elif mxm > 20:
            self.tablero3(mxm)

    def tablero1(self):
        portaaviones = 1
        submarino = 2
        destructores = 3
        buques = 4
        TableroTop(self.window, portaaviones, submarino, destructores, buques)

    def tablero2(self):
        portaaviones = 2
        submarino = 4
        destructores = 6
        buques = 8

    def tablero3(self, m):
        portaaviones = int(((m - 1) / 10) + 1)
        submarino = int(((m - 1) / 10) + 2)
        destructores = int(((m - 1) / 10) + 3)
        buques = int(((m - 1) / 10) + 4)

    def restaurarWin(self):
        self.window.geometry('1116x718')
        self.tienda_frame.destroy()
        self.tienda.destroy()
        self.configfile_tienda.destroy()
        self.categoria.destroy()
        self.nombre.destroy()
        self.categoria_entry.destroy()
        self.item_entry.destroy()
        self.comprar_button.destroy()

    def deletetuto(self):
        self.heading.destroy()
        self.configfile.destroy()

    def dame_categorias(self, categorias):
        with open('Tutorial', 'r') as f:
            f.read()

    def newLine(self, linea):
        resultado = linea.splitlines()
        return len(resultado)

    def comprar(self):
        messagebox.showinfo("u got it Haz",
                            "comprado el item " + self.item_entry.get() + "de la categoria " + self.categoria_entry.get())


class Tablero:
    def __init__(self, window, portaviones, submarino, destructores, buques):
        self.window = window
        self.portaaviones = portaviones
        self.submarino = submarino
        self.destructores = destructores
        self.busques = buques
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title('Batalla naval')
        self.window.iconbitmap('Imagenes\\icono.ico')
        #self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\bg1.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')


def TableroTop(window, portaviones, submarino, destructores, buques):
    win = Toplevel()
    Tablero(win, portaviones, submarino, destructores, buques)
    window.withdraw()
    win.deiconify()
    print("--------------")
    matrizPrueba = Matriz()

    print("--------------")
    matrizPrueba.Grafo()
