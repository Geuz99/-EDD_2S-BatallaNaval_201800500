from tkinter import *
from tkinter import simpledialog, messagebox

from PIL import ImageTk, Image
import requests

base_url = 'http://192.168.1.9:18080'


class UserPAge:
    def __init__(self, window, user, password):
        self.window = window
        self.user = user
        self.password = password
        self.window.geometry('1116x718')
        self.window.resizable(0, 0)
        self.window.title('Profile: ' + user)
        self.window.iconbitmap('Imagenes\\icono.ico')
        self.window.protocol("WM_DELETE_WINDOW", self.salir)

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
                                   activebackground='#3847ff', command=self.salir)
        self.store_button.place(x=265, y=330)

        # BOTON REALIZAR MOVIMIENTOS
        self.move_button = Button(self.btsUsers_frame, text='Realizar movimientos', bg='#0000ff', fg='white',
                                  font=('yu gothic ui', 12, 'bold'), width=40, height=2, bd=0, cursor="pirate",
                                  activebackground='#3847ff', command=self.salir)
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

        # FRAME SUBRAYADO
        self.subra_down = Frame(self.btsUsers_frame, bg='black', width='450', height='10')
        self.subra_down.place(x=0, y=708)

    def editar(self):
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
        res = messagebox.askquestion("ATENCION!!!", "Esta a punto de eliminar su cuenta definitivamente. Esta seguro "
                                                    "con la accion que quiere realizar?")
        if res == 'yes':
            print('eliminada')
        elif res == 'no':
            print('no')
        else:
            messagebox.showwarning('error', 'Occurrio un error al realizar esta accion!')

    def tuto(self):
        print('tuto')

    def salir(self):
        # self.window.destroy()
        exit(0)
