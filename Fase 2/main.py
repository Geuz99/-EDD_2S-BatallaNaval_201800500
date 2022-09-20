from tkinter import *
from PIL import ImageTk, Image


class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1116x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title("")
        self.window.iconbitmap('Imagenes\\icono.ico')

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
        self.username_label.place(x=600, y=400)

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
                            activebackground='#3847ff')
        self.login.place(relx=0.5, rely=0.5, anchor=CENTER)


def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


if __name__ == '__main__':
    page()
