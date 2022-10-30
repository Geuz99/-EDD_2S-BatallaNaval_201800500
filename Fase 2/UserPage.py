import random
from os import remove
from tkinter import *
from tkinter import simpledialog, messagebox
from Matriz import Matriz

from PIL import ImageTk, Image
import requests
from Graph import Graph

from eth_account import Account
import secrets

base_url = 'http://192.168.1.9:18080'


class UserPage:
    def __init__(self, window, user, password, tokens):
        self.window = window
        self.user = user
        self.password = password
        self.monedas = tokens
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
        self.tokens_entry = Entry(self.tienda_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                  font=('yu gothic ui', 14, 'bold'))  # add3f

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

        # BOTON COMPRAR (TIENDA)
        self.comprar_button = Button(self.tienda_frame, text='COMPRAR', bg='#00ff00', fg='red',
                                     font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                     activebackground='#cc6600', command=self.editar)


        # BOTON WALLET (STORE)
        self.wallet_button = Button(self.tienda_frame, text='Wallet', bg='#1f7a7a', fg='#ffff00',
                                     font=('yu gothic ui', 12, 'bold'), width=15, height=4, bd=0, cursor="pirate",
                                     activebackground='#cc6600', command=self.wallet)


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
        self.tokens_entry = Entry(self.tienda_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                  font=('yu gothic ui', 14, 'bold'))  # add3f
        self.tokens_entry.insert(0, self.monedas)
        self.tokens_entry.place(x=720, y=0, width=75, height=35) # add3f
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
        self.wallet_button = Button(self.tienda_frame, text='Wallet', bg='#1f7a7a', fg='#ffff00',
                                    font=('yu gothic ui', 12, 'bold'), width=10, height=1, bd=2, cursor="pirate",
                                    activebackground='#cc6600', command=self.wallet)
        self.wallet_button.place(x=21, y=4)
        res = requests.get(f'{base_url}/tienda')
        data = res.text
        with open('Tienda', 'w') as f:
            f.write(data)
        with open('Tienda', 'r') as f:
            self.configfile_tienda.insert(INSERT, f.read())

    def wallet(self):
        res = messagebox.askquestion("WALLET FREE USAC!", "Aun no cuentas con tu wallet?, deseas crear una?")
        if res == 'yes':
            priv = secrets.token_hex(32)
            priv_key = "0x" + priv
            print("Llave privada, no se de compartir.", priv_key)
            acct = Account.from_key(priv_key)
            print("From wallet:", acct.address)
        elif res == 'no':
            messagebox.showinfo("NO APOYAS AL PARO?", "OJO necesitaras una para realizar compras en esta plataforma")
        else:
            messagebox.showwarning('error', 'Occurrio un error al realizar esta accion!')



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
            res = requests.get(
                f'{base_url}/login/eliminar/' + self.user + '/' + self.password)
            data = res.text
            if data == 'correcto':
                messagebox.showwarning("ELIMINADA", "Lamentamos que hallas decidido dejarnos. Esperemos pronto tenerte "
                                                    "otra vez de vuelta. Hasta pronto...!")
            else:
                messagebox.showwarning('error', 'Occurrio un error al realizar esta accion!')
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
            self.tablero1(mxm)
        elif 10 < mxm <= 20:
            self.tablero2(mxm)
        elif mxm > 20:
            self.tablero3(mxm)

    def tablero1(self, m):
        portaaviones = 1
        submarino = 2
        destructores = 3
        buques = 4
        colocacion(self.window, portaaviones, submarino, destructores, buques, m)

    def tablero2(self, m):
        portaaviones = 2
        submarino = 4
        destructores = 6
        buques = 8
        colocacion(self.window, portaaviones, submarino, destructores, buques, m)

    def tablero3(self, m):
        portaaviones = int(((m - 1) / 10) + 1)
        submarino = int(((m - 1) / 10) + 2)
        destructores = int(((m - 1) / 10) + 3)
        buques = int(((m - 1) / 10) + 4)
        colocacion(self.window, portaaviones, submarino, destructores, buques, m)

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
    def __init__(self, window, portaviones, submarino, destructores, buques, mxm):
        self.barcos_p1 = 0
        self.pointsj1 = 0
        self.acertadosj1 = 0
        self.noacertadosj1 = 0
        self.barcos_p2 = 0
        self.pointsj2 = 0
        self.acertadosj2 = 0
        self.noacertadosj2 = 0
        self.window = window
        self.portaaviones = portaviones
        self.submarino = submarino
        self.destructores = destructores
        self.busques = buques
        self.portaaviones2 = portaviones
        self.submarino2 = submarino
        self.destructores2 = destructores
        self.busques2 = buques
        self.mxm = mxm
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title('Batalla naval')
        self.window.iconbitmap('Imagenes\\icono.ico')
        self.matriz = Matriz()
        self.matriz2 = Matriz()
        self.graph = Graph(mxm + 1)
        self.graph2 = Graph(mxm + 1)
        # self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\bg1.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # BOTONES DE BARCOS
        self.p_button = Button(self.window, text='Portaaviones', bg='#1affff', fg='black',
                               font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                               activebackground='#3847ff', command=self.p)
        self.p_button.place(x=65, y=710)
        self.s_button = Button(self.window, text='Submarinos', bg='#1affff', fg='black',
                               font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                               activebackground='#3847ff', command=self.s)
        self.s_button.place(x=65, y=790)
        self.d_button = Button(self.window, text='Destructores', bg='#1affff', fg='black',
                               font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                               activebackground='#3847ff', command=self.d)
        self.d_button.place(x=65, y=870)
        self.b_button = Button(self.window, text='Buques', bg='#1affff', fg='black',
                               font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                               activebackground='#3847ff', command=self.b)
        self.b_button.place(x=65, y=950)
        self.start_button = Button(self.window, text='COMENZAR', bg='red', fg='white',
                                   font=('yu gothic ui', 12, 'bold'), width=85, height=3, bd=0, cursor="pirate",
                                   activebackground='#3847ff', command=self.comenzar)
        self.start_button.place(x=590, y=830)

        self.p2_button = Button(self.window, text='Portaaviones', bg='#1affff', fg='black',
                                font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                activebackground='#3847ff', command=self.p2)
        self.p2_button.place(x=1760, y=710)
        self.s2_button = Button(self.window, text='Submarinos', bg='#1affff', fg='black',
                                font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                activebackground='#3847ff', command=self.s2)
        self.s2_button.place(x=1760, y=790)
        self.d2_button = Button(self.window, text='Destructores', bg='#1affff', fg='black',
                                font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                activebackground='#3847ff', command=self.d2)
        self.d2_button.place(x=1760, y=870)
        self.b2_button = Button(self.window, text='Buques', bg='#1affff', fg='black',
                                font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                activebackground='#3847ff', command=self.b2)
        self.b2_button.place(x=1760, y=950)

        # LABELS JUGADORES
        self.player1_label = Label(self.window, text='JUGADOR 1', bg='#1f7a7a', fg='white',
                                   font=('yu gothic ui', 30, 'bold'))
        self.player1_label.place(x=310, y=10)
        self.player2_label = Label(self.window, text='JUGADOR 2', bg='#1f7a7a', fg='white',
                                   font=('yu gothic ui', 30, 'bold'))
        self.player2_label.place(x=1410, y=10)
        self.vs_label = Label(self.window, text='VS', bg='#1f7a7a', fg='white',
                              font=('yu gothic ui', 30, 'bold'))
        self.vs_label.place(x=935, y=300)

        # JUEGO COMENZADO...
        self.xplayer1_label = Label(self.window, text='COORDENADA EN X:', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.yplayer1_label = Label(self.window, text='COORDENADA EN Y:', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.xplayer1_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'))
        self.yplayer1_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'))
        self.shootp1_button = Button(self.window, text='Disparar', bg='#1affff', fg='black',
                                     font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                     activebackground='#3847ff', command=self.jugabilidad1)
        self.xplayer2_label = Label(self.window, text='COORDENADA EN X:', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.yplayer2_label = Label(self.window, text='COORDENADA EN Y:', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.xplayer2_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'))
        self.yplayer2_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'))
        self.shootp2_button = Button(self.window, text='Disparar', bg='#1affff', fg='black',
                                     font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                     activebackground='#3847ff', command=self.jugabilidad2)

        self.random_button = Button(self.window, text='RANDOM', bg='#3377ff', fg='black',
                                    font=('yu gothic ui', 12, 'bold'), width=40, height=3, bd=0, cursor="pirate",
                                    activebackground='#3847ff', command=self.random)
        self.random_button.place(x=785, y=480)

        self.randomj2_button = Button(self.window, text='Random', bg='#33cc33', fg='black',
                                      font=('yu gothic ui', 12, 'bold'), width=10, height=3, bd=0, cursor="pirate",
                                      activebackground='#3847ff', command=self.randomxy)

        # LABELS DE PUNTUACION JVJ
        self.pointsj1_label = Label(self.window, text='Puntos', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 10, 'bold'))
        self.pointsj1_label.place(x=30, y=80)
        self.pointsj1_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'), justify='center')
        self.pointsj1_entry.place(x=30, y=120, width=50, height=36)
        self.pointsj1_entry.insert(0, 0)

        self.acertadosj1_label = Label(self.window, text='Acertados', bg='#009933', fg='white',
                                       font=('yu gothic ui', 10, 'bold'))
        self.acertadosj1_label.place(x=25, y=180)
        self.acertadosj1_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                       font=('yu gothic ui', 14, 'bold'), justify='center')
        self.acertadosj1_entry.place(x=30, y=230, width=50, height=36)
        self.acertadosj1_entry.insert(0, 0)

        self.noacertadosj1_label = Label(self.window, text='No Acertados', bg='#e60000', fg='white',
                                         font=('yu gothic ui', 10, 'bold'))
        self.noacertadosj1_label.place(x=20, y=290)
        self.noacertadosj1_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                         font=('yu gothic ui', 14, 'bold'), justify='center')
        self.noacertadosj1_entry.place(x=30, y=340, width=50, height=36)
        self.noacertadosj1_entry.insert(0, 0)

        self.pointsj2_label = Label(self.window, text='Puntos', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 10, 'bold'))
        self.pointsj2_label.place(x=1830, y=80)
        self.pointsj2_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'), justify='center')
        self.pointsj2_entry.place(x=1830, y=120, width=50, height=36)
        self.pointsj2_entry.insert(0, 0)

        self.acertadosj2_label = Label(self.window, text='Acertados', bg='#009933', fg='white',
                                       font=('yu gothic ui', 10, 'bold'))
        self.acertadosj2_label.place(x=1825, y=180)
        self.acertadosj2_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                       font=('yu gothic ui', 14, 'bold'), justify='center')
        self.acertadosj2_entry.place(x=1830, y=230, width=50, height=36)
        self.acertadosj2_entry.insert(0, 0)

        self.noacertadosj2_label = Label(self.window, text='No Acertados', bg='#e60000', fg='white',
                                         font=('yu gothic ui', 10, 'bold'))
        self.noacertadosj2_label.place(x=1815, y=290)
        self.noacertadosj2_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                         font=('yu gothic ui', 14, 'bold'), justify='center')
        self.noacertadosj2_entry.place(x=1830, y=340, width=50, height=36)
        self.noacertadosj2_entry.insert(0, 0)

        # TABLERO DE BOTONES

        # TABLERO IZQUIERDO
        nfil = 1 / mxm
        ncol = 1 / mxm
        f1 = Frame(self.window)
        f1.config(bg="white")
        f1.place(x=130, y=80, width=600, height=600)
        self.btnlista = []
        for i in range(mxm):
            self.btnlista.append([])
            for j in range(int(mxm)):
                self.btnlista[i].append(Button(f1))
                self.btnlista[i][j].config(bg="white", borderwidth=1, relief="solid")
                self.btnlista[i][j].place(relx=ncol * i, rely=nfil * j, relwidth=ncol, relheigh=nfil)

        # TABLERO DERECHO
        f2 = Frame(self.window)
        f2.config(bg="white")
        f2.place(x=1200, y=80, width=600, height=600)
        self.btnlista2 = []
        for i in range(mxm):
            self.btnlista2.append([])
            for j in range(int(mxm)):
                self.btnlista2[i].append(Button(f2))
                self.btnlista2[i][j].config(bg="white", borderwidth=1, relief="solid")
                self.btnlista2[i][j].place(relx=ncol * i, rely=nfil * j, relwidth=ncol, relheigh=nfil)

        '''# IMAGEN CUANDO COLOQUE COORDENADAS
        self.photo = PhotoImage(file="Imagenes/x.png")'''

    def randomxy(self):
        x = random.randint(1, self.mxm)
        y = random.randint(1, self.mxm)
        self.xplayer2_entry.delete(0, 'end')
        self.xplayer2_entry.insert(0, x)
        self.yplayer2_entry.delete(0, 'end')
        self.yplayer2_entry.insert(0, y)

    def random(self):
        while self.portaaviones != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                forma = random.randint(0, 1)
                if forma == 0:
                    self.portaaviones = self.portaaviones - 1
                    for i in range(4):
                        self.barcos_p1 = self.barcos_p1 + 1
                        self.btnlista[int(x - 1)][int(y - 1) + i].config(bg="#A52A2A", borderwidth=2,
                                                                         relief="solid")
                        self.matriz.insertarNodo(x, y + i, "P")
                elif forma == 1:
                    self.portaaviones = self.portaaviones - 1
                    for i in range(4):
                        self.barcos_p1 = self.barcos_p1 + 1
                        self.btnlista[int(x - 1) + i][int(y - 1)].config(bg="#A52A2A", borderwidth=2,
                                                                         relief="solid")
                        self.matriz.insertarNodo(x + i, y, "P")
            else:
                break

        while self.portaaviones2 != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista2[x - 1][y - 1].cget('bg') == "white":
                forma = random.randint(0, 1)
                if forma == 0:
                    self.portaaviones2 = self.portaaviones2 - 1
                    for i in range(4):
                        self.barcos_p2 = self.barcos_p2 + 1
                        self.btnlista2[int(x - 1)][int(y - 1) + i].config(bg="#A52A2A", borderwidth=2,
                                                                          relief="solid")
                        self.matriz2.insertarNodo(x, y + i, "P")
                elif forma == 1:
                    self.portaaviones2 = self.portaaviones2 - 1
                    for i in range(4):
                        self.barcos_p2 = self.barcos_p2 + 1
                        self.btnlista2[int(x - 1) + i][int(y - 1)].config(bg="#A52A2A", borderwidth=2,
                                                                          relief="solid")
                        self.matriz2.insertarNodo(x + i, y, "P")
            else:
                break

        while self.submarino != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                forma = random.randint(0, 1)
                if forma == 0:
                    self.submarino = self.submarino - 1
                    for i in range(3):
                        self.barcos_p1 = self.barcos_p1 + 1
                        self.btnlista[int(x - 1)][int(y - 1) + i].config(bg="#000080", borderwidth=2,
                                                                         relief="solid")
                        self.matriz.insertarNodo(x, y + i, "S")
                elif forma == 1:
                    self.submarino = self.submarino - 1
                    for i in range(3):
                        self.barcos_p1 = self.barcos_p1 + 1
                        self.btnlista[int(x - 1) + i][int(y - 1)].config(bg="#000080", borderwidth=2,
                                                                         relief="solid")
                        self.matriz.insertarNodo(x + i, y, "S")
            else:
                break

        while self.submarino2 != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista2[x - 1][y - 1].cget('bg') == "white":
                forma = random.randint(0, 1)
                if forma == 0:
                    self.submarino2 = self.submarino2 - 1
                    for i in range(3):
                        self.barcos_p2 = self.barcos_p2 + 1
                        self.btnlista2[int(x - 1)][int(y - 1) + i].config(bg="#000080", borderwidth=2,
                                                                          relief="solid")
                        self.matriz2.insertarNodo(x, y + i, "S")
                elif forma == 1:
                    self.submarino2 = self.submarino2 - 1
                    for i in range(3):
                        self.barcos_p2 = self.barcos_p2 + 1
                        self.btnlista2[int(x - 1) + i][int(y - 1)].config(bg="#000080", borderwidth=2,
                                                                          relief="solid")
                        self.matriz2.insertarNodo(x + i, y, "S")
            else:
                break

        while self.destructores != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                forma = random.randint(0, 1)
                if forma == 0:
                    self.destructores = self.destructores - 1
                    for i in range(2):
                        self.barcos_p1 = self.barcos_p1 + 1
                        self.btnlista[int(x - 1)][int(y - 1) + i].config(bg="#808080", borderwidth=2,
                                                                         relief="solid")
                        self.matriz.insertarNodo(x, y + i, "D")
                elif forma == 1:
                    self.destructores = self.destructores - 1
                    for i in range(2):
                        self.barcos_p1 = self.barcos_p1 + 1
                        self.btnlista[int(x - 1) + i][int(y - 1)].config(bg="#808080", borderwidth=2,
                                                                         relief="solid")
                        self.matriz.insertarNodo(x + i, y, "D")
            else:
                break

        while self.destructores2 != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista2[x - 1][y - 1].cget('bg') == "white":
                forma = random.randint(0, 1)
                if forma == 0:
                    self.destructores2 = self.destructores2 - 1
                    for i in range(2):
                        self.barcos_p2 = self.barcos_p2 + 1
                        self.btnlista2[int(x - 1)][int(y - 1) + i].config(bg="#808080", borderwidth=2,
                                                                          relief="solid")
                        self.matriz2.insertarNodo(x, y + i, "D")
                elif forma == 1:
                    self.destructores2 = self.destructores2 - 1
                    for i in range(2):
                        self.barcos_p2 = self.barcos_p2 + 1
                        self.btnlista2[int(x - 1) + i][int(y - 1)].config(bg="#808080", borderwidth=2,
                                                                          relief="solid")
                        self.matriz2.insertarNodo(x + i, y, "D")
            else:
                break

        while self.busques != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                self.busques = self.busques - 1
                self.btnlista[int(x - 1)][int(y - 1)].config(bg="#008080", borderwidth=2, relief="solid")
                self.matriz.insertarNodo(x, y, "B")
                self.barcos_p1 = self.barcos_p1 + 1
            else:
                break

        while self.busques2 != 0:
            x = random.randint(1, self.mxm)
            y = random.randint(1, self.mxm)
            if self.btnlista2[x - 1][y - 1].cget('bg') == "white":
                self.busques2 = self.busques2 - 1
                self.btnlista2[int(x - 1)][int(y - 1)].config(bg="#008080", borderwidth=2, relief="solid")
                self.matriz2.insertarNodo(x, y, "B")
                self.barcos_p2 = self.barcos_p2 + 1
            else:
                break

    def prueba(self):
        self.graph.add_edge(0, 3)
        self.graph.add_edge(1, 1)
        self.graph.add_edge(1, 8)
        self.graph.add_edge(2, 7)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(4, 3)
        self.graph.add_edge(4, 8)
        self.graph.add_edge(6, 1)
        self.graph.add_edge(6, 5)
        self.graph.add_edge(7, 2)
        self.graph.add_edge(7, 9)
        self.graph.add_edge(9, 2)
        self.graph.add_edge(9, 6)
        self.graph.print_agraph()

    def who_start(self):
        comienza = random.randint(0, 1)
        if comienza == 0:
            return 0
        else:
            return 1

    def jugabilidad1(self):
        x = int(self.xplayer1_entry.get())
        y = int(self.yplayer1_entry.get())
        self.graph.add_edge(y, x)
        try:
            if self.btnlista2[x - 1][y - 1].cget('bg') == "white":
                self.btnlista2[x - 1][y - 1].config(bg="black")
                self.shootp1_button["state"] = "disable"
                self.shootp2_button["state"] = "normal"
                self.noacertadosj1 = self.noacertadosj1 + 1
                self.noacertadosj1_entry.delete(0, 'end')
                self.noacertadosj1_entry.insert(0, self.noacertadosj1)
                if self.pointsj1 != 0:
                    self.pointsj1 = self.pointsj1 - 1
                    self.pointsj1_entry.delete(0, 'end')
                    self.pointsj1_entry.insert(0, self.pointsj1)
            # elif self.btnlista2[x - 1][y - 1].cget('bg') == "black":
            #    messagebox.showerror("Error Jugador 1", "Ya haz colocado esta posicion")
            else:
                self.btnlista2[x - 1][y - 1].config(bg="black")
                messagebox.showinfo("OJO Jugador 1", "LE HAZ DADO A ALGUN BARCO")
                self.shootp1_button["state"] = "disable"
                self.shootp2_button["state"] = "normal"
                self.barcos_p2 = self.barcos_p2 - 1
                self.acertadosj1 = self.acertadosj1 + 1
                self.acertadosj1_entry.delete(0, 'end')
                self.acertadosj1_entry.insert(0, self.acertadosj1)
                self.pointsj1 = self.pointsj1 + 1
                self.pointsj1_entry.delete(0, 'end')
                self.pointsj1_entry.insert(0, self.pointsj1)
                if self.barcos_p2 == 0:
                    messagebox.showinfo("winner jugador 1", "Lograste derribar todos los barcos del enemigo")
                    self.shootp1_button["state"] = "disable"
                    self.shootp2_button["state"] = "disable"
                    reportesTop(self.window, "JUGADOR 1", self.graph)
        except IndexError:
            messagebox.showerror("Error", "Estas ingresando unas coordenadas erroneas")

    def jugabilidad2(self):
        x = int(self.xplayer2_entry.get())
        y = int(self.yplayer2_entry.get())
        self.graph2.add_edge(y, x)
        try:
            if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                self.btnlista[x - 1][y - 1].config(bg="black")
                self.shootp2_button["state"] = "disable"
                self.shootp1_button["state"] = "normal"
                self.noacertadosj2 = self.noacertadosj2 + 1
                self.noacertadosj2_entry.delete(0, 'end')
                self.noacertadosj2_entry.insert(0, self.noacertadosj2)
                if self.pointsj2 != 0:
                    self.pointsj2 = self.pointsj2 - 1
                    self.pointsj2_entry.delete(0, 'end')
                    self.pointsj2_entry.insert(0, self.pointsj2)
            # elif self.btnlista[x - 1][y - 1].cget('bg') == "black":
            #    messagebox.showerror("Error Jugador 2", "Ya haz colocado esta posicion")
            else:
                messagebox.showinfo("OJO Jugador 2", "LE HAZ DADO A ALGUN BARCO")
                self.btnlista[x - 1][y - 1].config(bg="black")
                self.shootp2_button["state"] = "disable"
                self.shootp1_button["state"] = "normal"
                self.barcos_p1 = self.barcos_p1 - 1
                self.acertadosj2 = self.acertadosj2 + 1
                self.acertadosj2_entry.delete(0, 'end')
                self.acertadosj2_entry.insert(0, self.acertadosj2)
                self.pointsj2 = self.pointsj2 + 1
                self.pointsj2_entry.delete(0, 'end')
                self.pointsj2_entry.insert(0, self.pointsj2)
                if self.barcos_p1 == 0:
                    messagebox.showinfo("winner jugador 2", "Lograste derribar todos los barcos del enemigo")
                    self.shootp1_button["state"] = "disable"
                    self.shootp2_button["state"] = "disable"
                    reportesTop(self.window, "JUGADOR 2", self.graph2)
        except IndexError:
            messagebox.showerror("Error", "Estas ingresando unas coordenadas erroneas")

    def colocarDisparos(self):
        self.xplayer1_label.place(x=130, y=740)
        self.yplayer1_label.place(x=130, y=790)
        self.xplayer1_entry.place(x=340, y=740, width=50, height=36)
        self.yplayer1_entry.place(x=340, y=790, width=50, height=36)
        self.shootp1_button.place(x=400, y=745)
        self.xplayer2_label.place(x=1200, y=740)
        self.yplayer2_label.place(x=1200, y=790)
        self.xplayer2_entry.place(x=1410, y=740, width=50, height=36)
        self.yplayer2_entry.place(x=1410, y=790, width=50, height=36)
        self.shootp2_button.place(x=1470, y=745)
        self.randomj2_button.place(x=1600, y=745)
        if self.who_start() == 0:
            self.shootp2_button["state"] = "disable"
        else:
            self.shootp2_button["state"] = "disable"

    def comenzar(self):
        if self.portaaviones == 0 and self.submarino == 0 and self.destructores == 0 and self.busques == 0 and self.portaaviones2 == 0 and self.submarino2 == 0 and self.destructores2 == 0 and self.busques2 == 0:
            self.matriz.imprimir()
            self.matriz2.imprimir()
            self.p_button.destroy()
            self.s_button.destroy()
            self.d_button.destroy()
            self.b_button.destroy()
            self.p2_button.destroy()
            self.s2_button.destroy()
            self.d2_button.destroy()
            self.b2_button.destroy()
            self.start_button.destroy()
            self.random_button.destroy()
            self.colocarDisparos()
            # self.prueba()

        else:
            messagebox.showinfo("Barcos", "aun falta barcos que colocar en el tablero")

    def p(self):
        while self.portaaviones != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
            else:
                if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                    forma = simpledialog.askstring("v vertical, h horizontal", "Ingrese una opcion", parent=self.window)
                    if forma == "v":
                        self.portaaviones = self.portaaviones - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "verticalmente")
                        for i in range(4):
                            self.barcos_p1 = self.barcos_p1 + 1
                            self.btnlista[int(x - 1)][int(y - 1) + i].config(bg="#A52A2A", borderwidth=2,
                                                                             relief="solid")
                            self.matriz.insertarNodo(x, y + i, "P")
                    elif forma == "h":
                        self.portaaviones = self.portaaviones - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "horizontalmente")
                        for i in range(4):
                            self.barcos_p1 = self.barcos_p1 + 1
                            self.btnlista[int(x - 1) + i][int(y - 1)].config(bg="#A52A2A", borderwidth=2,
                                                                             relief="solid")
                            self.matriz.insertarNodo(x + i, y, "P")
                    else:
                        messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def s(self):
        while self.submarino != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
            else:
                if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                    forma = simpledialog.askstring("v vertical, h horizontal", "Ingrese una opcion", parent=self.window)
                    if forma == "v":
                        self.submarino = self.submarino - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "verticalmente")
                        for i in range(3):
                            self.barcos_p1 = self.barcos_p1 + 1
                            self.btnlista[int(x - 1)][int(y - 1) + i].config(bg="#000080", borderwidth=2,
                                                                             relief="solid")
                            self.matriz.insertarNodo(x, y + i, "S")
                    elif forma == "h":
                        self.submarino = self.submarino - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "horizontalmente")
                        for i in range(3):
                            self.barcos_p1 = self.barcos_p1 + 1
                            self.btnlista[int(x - 1) + i][int(y - 1)].config(bg="#000080", borderwidth=2,
                                                                             relief="solid")
                            self.matriz.insertarNodo(x + i, y, "S")
                    else:
                        messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def d(self):
        while self.destructores != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
            else:
                if self.btnlista[x - 1][y - 1].cget('bg') == "white":

                    forma = simpledialog.askstring("v vertical, h horizontal", "Ingrese una opcion", parent=self.window)
                    if forma == "v":
                        self.destructores = self.destructores - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "verticalmente")
                        for i in range(2):
                            self.barcos_p1 = self.barcos_p1 + 1
                            self.btnlista[int(x - 1)][int(y - 1) + i].config(bg="#808080", borderwidth=2,
                                                                             relief="solid")
                            self.matriz.insertarNodo(x, y + i, "D")
                    elif forma == "h":
                        self.destructores = self.destructores - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "horizontalmente")
                        for i in range(2):
                            self.barcos_p1 = self.barcos_p1 + 1
                            self.btnlista[int(x - 1) + i][int(y - 1)].config(bg="#808080", borderwidth=2,
                                                                             relief="solid")
                            self.matriz.insertarNodo(x + i, y, "D")
                    else:
                        messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def b(self):
        while self.busques != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                break
            else:
                if self.btnlista[x - 1][y - 1].cget('bg') == "white":
                    messagebox.showinfo("Coordenadas",
                                        "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(y) + ")")
                    self.busques = self.busques - 1
                    self.btnlista[int(x - 1)][int(y - 1)].config(bg="#008080", borderwidth=2, relief="solid")
                    self.matriz.insertarNodo(x, y, "B")
                    self.barcos_p1 = self.barcos_p1 + 1
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def p2(self):
        while self.portaaviones2 != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
            else:
                if self.btnlista2[x - 1][y - 1].cget('bg') == "white":

                    forma = simpledialog.askstring("v vertical, h horizontal", "Ingrese una opcion", parent=self.window)
                    if forma == "v":
                        self.portaaviones2 = self.portaaviones2 - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "verticalmente")
                        for i in range(4):
                            self.barcos_p2 = self.barcos_p2 + 1
                            self.btnlista2[int(x - 1)][int(y - 1) + i].config(bg="#A52A2A", borderwidth=2,
                                                                              relief="solid")
                            self.matriz2.insertarNodo(x, y + i, "P")
                    elif forma == "h":
                        self.portaaviones2 = self.portaaviones2 - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "horizontalmente")
                        for i in range(4):
                            self.barcos_p2 = self.barcos_p2 + 1
                            self.btnlista2[int(x - 1) + i][int(y - 1)].config(bg="#A52A2A", borderwidth=2,
                                                                              relief="solid")
                            self.matriz2.insertarNodo(x + i, y, "P")
                    else:
                        messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def s2(self):
        while self.submarino2 != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
            else:
                if self.btnlista2[x - 1][y - 1].cget('bg') == "white":

                    forma = simpledialog.askstring("v vertical, h horizontal", "Ingrese una opcion", parent=self.window)
                    if forma == "v":
                        self.submarino2 = self.submarino2 - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "verticalmente")
                        for i in range(3):
                            self.barcos_p2 = self.barcos_p2 + 1
                            self.btnlista2[int(x - 1)][int(y - 1) + i].config(bg="#000080", borderwidth=2,
                                                                              relief="solid")
                            self.matriz2.insertarNodo(x, y + i, "S")
                    elif forma == "h":
                        self.submarino2 = self.submarino2 - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "horizontalmente")
                        for i in range(3):
                            self.barcos_p2 = self.barcos_p2 + 1
                            self.btnlista2[int(x - 1) + i][int(y - 1)].config(bg="#000080", borderwidth=2,
                                                                              relief="solid")
                            self.matriz2.insertarNodo(x + i, y, "S")
                    else:
                        messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def d2(self):
        while self.destructores2 != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
            else:
                if self.btnlista2[x - 1][y - 1].cget('bg') == "white":

                    forma = simpledialog.askstring("v vertical, h horizontal", "Ingrese una opcion", parent=self.window)
                    if forma == "v":
                        self.destructores2 = self.destructores2 - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "verticalmente")
                        for i in range(2):
                            self.barcos_p2 = self.barcos_p2 + 1
                            self.btnlista2[int(x - 1)][int(y - 1) + i].config(bg="#808080", borderwidth=2,
                                                                              relief="solid")
                            self.matriz2.insertarNodo(x, y + i, "D")
                    elif forma == "h":
                        self.destructores2 = self.destructores2 - 1
                        messagebox.showinfo("Coordenadas",
                                            "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(
                                                y) + ") " + "horizontalmente")
                        for i in range(2):
                            self.barcos_p2 = self.barcos_p2 + 1
                            self.btnlista2[int(x - 1) + i][int(y - 1)].config(bg="#808080", borderwidth=2,
                                                                              relief="solid")
                            self.matriz2.insertarNodo(x + i, y, "D")
                    else:
                        messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break

    def b2(self):
        while self.busques2 != 0:
            x = simpledialog.askinteger("x", "Ingrese una coordenada en x", parent=self.window)
            y = simpledialog.askinteger("y", "Ingrese una coordenada en y", parent=self.window)
            if (x - 1) > self.mxm or (y - 1) > self.mxm:
                messagebox.showerror("Error", "Las coordenadas ingresadas son malas")
                break
            else:
                if self.btnlista2[x - 1][y - 1].cget('bg') == "white":
                    messagebox.showinfo("Coordenadas",
                                        "Las coordenadas ingresadas son: " + "(" + str(x) + "," + str(y) + ")")
                    self.busques2 = self.busques2 - 1
                    self.btnlista2[int(x - 1)][int(y - 1)].config(bg="#008080", borderwidth=2, relief="solid")
                    self.matriz2.insertarNodo(x, y, "B")
                    self.barcos_p2 = self.barcos_p2 + 1
                else:
                    messagebox.showerror("Error", "ya existe un barco en esa pocision")
                    break


def colocacion(window, portaviones, submarino, destructores, buques, mxm):
    win = Toplevel()
    Tablero(win, portaviones, submarino, destructores, buques, mxm)
    # window.withdraw()
    win.deiconify()


def reportesTop(window, ganador, graph):
    win = Toplevel()
    Reportes(win, ganador, graph)
    # window.withdraw()
    win.deiconify()


class Reportes:
    def __init__(self, window, ganador, graph):
        self.window = window
        self.ganador = ganador
        self.graph = graph
        self.window.geometry('716x318')
        self.window.resizable(0, 0)
        self.window.title('Reportes ' + self.ganador)
        self.window.iconbitmap('Imagenes\\icono.ico')
        # self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\bg1.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # BOTONES DE REPORTES
        self.lista_button = Button(self.window, text='Mostrar Lista', bg='#66ff66', fg='black',
                                   font=('yu gothic ui', 12, 'bold'), width=25, height=8, bd=0, cursor="pirate",
                                   activebackground='#3847ff', command=self.graphoLista)
        self.lista_button.place(x=50, y=75)
        self.grapho_button = Button(self.window, text='Mostrar Grafo', bg='#ffcc66', fg='black',
                                    font=('yu gothic ui', 12, 'bold'), width=25, height=8, bd=0, cursor="pirate",
                                    activebackground='#3847ff', command=self.grapho)
        self.grapho_button.place(x=420, y=75)

    def graphoLista(self):
        self.graph.showList()

    def grapho(self):
        self.graph.showGraph()
