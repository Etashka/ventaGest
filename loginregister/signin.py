#Aqui está el signin
from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
import ttkbootstrap as ttk
import os
import subprocess
from tkinter import ttk
from database import connect_to_database
from utils import on_enter, on_leave
from PIL import Image
Image.CUBIC = Image.BICUBIC

#!/usr/bin/env python
# -*- coding: utf-8 -*-

root = Tk()

root.title('Inicio de Sesion')
root.geometry('950x500+300+200')  
root.configure(bg= "#fff")
root.resizable (False,False)



def open_new_window():
    root.withdraw()  # Oculta la ventana principal
    subprocess.Popen(['python', 'C:\\Users\\nara\\Desktop\\Atento 2024\\Proyectos\\Taskify\\loginregister\\signup.py'])

    

def signin():
    username = user.get()
    password = code.get()


    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tu_tabla WHERE name = ? AND password = ?', (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        messagebox.showinfo('Inicio de sesión', 'Inicio de sesión exitoso')
        subprocess.run(['python', 'C:\\Users\\nara\\Desktop\\Atento 2024\\Proyectos\\Taskify\\loginregister\\22022024.py'])
    else:
        messagebox.showerror('Error', 'Usuario o contraseña incorrectos')

       

ruta_imagen = os.path.join("C:\\", "Users", "nara", "Desktop", "Atento 2024", "Proyectos", "Taskify", "images", "Login.png")
img = PhotoImage(file=ruta_imagen)
Label(root, image=img, bg='white').place(x=50,y=50)



frame = Frame(root, width=350, height=350, bg="white")
frame.place (x=480, y=70)

heading =Label(frame,text="Inicio de sesión", fg='#57a1f8',bg='white', font="Helvetica 14")
heading.place(x=100, y=50)


#usuario
user = Entry(frame, width=25, fg='black', border=0, bg="white", font="Helvetica 9")
user.place(x=30, y=80)
user.insert(0, 'Nombre de Usuario')
user.bind('<FocusIn>', lambda e: on_enter(e, user, 'Nombre de Usuario'))
user.bind('<FocusOut>', lambda e: on_leave(e, user, 'Nombre de Usuario'))

Frame(frame, width=296, height=1, bg='black').place(x=25, y=107)


code = Entry(frame, width=25, fg='black', border=0, bg="white", font="Helvetica 9")
code.place(x=30, y=150)
code.insert(0, 'Contraseña')
code.bind('<FocusIn>', lambda e: on_enter(e, code, 'Contraseña'))
code.bind('<FocusOut>', lambda e: on_leave(e, code, 'Contraseña'))

Frame(frame, width=295, height=1, bg='black').place(x=25, y=177)


#frase de abajo y signin
Button(frame,width=39, pady=7,text='Iniciar Sesión', bg='#57a1f8', fg='white',border=0, command=signin).place(x=35, y=204)
label= Label(frame,text="¿No tienes cuenta?", fg='black', bg='white', font="Helvetica 12")
label.place(x=75, y=270)

sign_up= Button (frame, width=12, text='Crear Cuenta', border=0,bg='white', cursor='hand2',fg='#57a1f8',command=open_new_window)
sign_up.place(x=215, y=270)




root.mainloop()




