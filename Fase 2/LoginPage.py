from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import requests

from PIL import ImageTk, Image
import AdminPage
import UserPage

base_url = 'http://192.168.1.9:18080'


def adminTop():
    win = Toplevel()
    AdminPage.AdminPage(win)
    window.withdraw()
    win.deiconify()


def UserTop(user, password, tokens):
    win = Toplevel()
    UserPage.UserPage(win, user, password, tokens)
    window.withdraw()
    win.deiconify()


class CargaPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('512x300')
        self.window.resizable(0, 0)
        self.window.title("Carga de usuarios")
        self.window.iconbitmap('Imagenes\\icono.ico')

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\inicio.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # FRAME LOGIN
        self.carga_frame = Frame(self.window, bg='#b3ffb3', width='300', height='500')
        self.carga_frame.place(x=250, y=0)

        # BOTON DE CARGAR
        self.salir = Button(self.carga_frame, text='Cargar', bg='#00e600', fg='white',
                            font=('yu gothic ui', 12, 'bold'), width=10, bd=0, cursor='hand2',
                            activebackground='#3847ff', command=self.carga)
        self.salir.place(x=85, y=75)

        # BOTON DE SALIR
        self.salir = Button(self.carga_frame, text='Salir', bg='#990000', fg='white',
                            font=('yu gothic ui', 12, 'bold'), width=10, bd=0, cursor='hand2',
                            activebackground='#3847ff', command=self.on_closing)
        self.salir.place(x=85, y=185)

    def carga(self):
        filename = askopenfilename()
        res = requests.get(f'{base_url}/carga/' + filename)
        data = res.text
        if data == 'Cargado con exito':
            messagebox.showinfo("Diviertete", "Archivo cargado con exito")
            win = Toplevel()
            LoginPage(win)
            window.withdraw()
            win.deiconify()
        else:
            messagebox.showerror("ERROR", "El acrhivo no fue cargado con exito")

    def on_closing(self):
        exit(0)


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1116x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title("cliente v.1")
        self.window.iconbitmap('Imagenes\\icono.ico')
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # FONDO DE PANTALLA
        self.bg_frame = Image.open('Imagenes\\bg1.jpeg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # FRAME LOGIN
        self.lgn_frame = Frame(self.window, bg='#1f7a7a', width='1150', height='800')
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.txt = 'BIENVENIDO'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 35, 'bold'), bg='#1f7a7a', fg='white')
        self.heading.place(x=160, y=5, width=300, height=85)

        # IMAGEN IZQUIERDA
        # BG IMAGEN
        self.side_image = Image.open('Imagenes\\bg2.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#1f7a7a')
        self.side_image_label.image = photo
        self.side_image_label.place(x=100, y=80)

        # SIGN IN IMAGEN
        self.sign_in_image = Image.open('Imagenes\\login.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#1f7a7a')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=780, y=180)

        self.sign_in_label = Label(self.lgn_frame, text='Login', bg='#1f7a7a', fg='white',
                                   font=('yu gothic ui', 20, 'bold'))
        self.sign_in_label.place(x=810, y=310)

        # USUARIO
        self.username_label = Label(self.lgn_frame, text='Usuario:', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.username_label.place(x=633, y=400)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'))
        self.username_entry.place(x=750, y=405)

        self.username_line = Canvas(self.lgn_frame, width=250, height=2.0, bg='white', highlightthickness=0)
        self.username_line.place(x=740, y=438)

        # CONTRASEÑA
        self.password_label = Label(self.lgn_frame, text='Contraseña:', bg='#1f7a7a', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.password_label.place(x=600, y=510)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#1f7a7a', fg='black',
                                    font=('yu gothic ui', 14, 'bold'))
        self.password_entry.place(x=750, y=510)

        self.password_line = Canvas(self.lgn_frame, width=250, height=2.0, bg='white', highlightthickness=0)
        self.password_line.place(x=740, y=545)

        # BOTON DE LOGIN
        self.lgn_button = Image.open('Imagenes\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#1f7a7a')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=699, y=610)

        self.login = Button(self.lgn_button_label, text='INICIAR SESION', bg='#3047ff', fg='white',
                            font=('yu gothic ui', 12, 'bold'), width=25, bd=0, cursor='hand2',
                            activebackground='#3847ff', command=self.ingresar)
        self.login.place(relx=0.5, rely=0.5, anchor=CENTER)

    def ingresar(self):
        user = "EDD"
        password = "edd123"
        edad = "50"
        if self.username_entry.get() == user and self.password_entry.get() == password:
            adminTop()
        else:
            usuario = self.username_entry.get()
            contra = self.password_entry.get()
            res = requests.get(f'{base_url}/login/' + usuario + '/' + contra)
            data = res.text
            if data == 'correcto':
                res_tokens = requests.get(f'{base_url}/login/tokens/' + usuario + '/' + contra)
                tokens = res_tokens.text
                UserTop(usuario, contra, tokens)
            else:
                messagebox.showwarning("ERROR", "Usuario / clave Invalida")

    def on_closing(self):
        res = messagebox.askquestion("Salir", "Estas seguro que quieres salir de la aplicacion?")
        if res == 'yes':
            exit(0)
        elif res == 'no':
            print('no')


if __name__ == '__main__':
    window = Tk()
    # CargaPage(window)
    # LoginPage(window)
    UserTop('geuz', 'loki', "5000")

    window.mainloop()
