#Aqui está el signup

from tkinter import * 
from tkinter import messagebox
from tkinter import Tk
import ast
import os
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import subprocess
from database import connect_to_database
import pyodbc
from utils import on_enter, on_leave
#!/usr/bin/env python
# -*- coding: utf-8 -*-

window = Tk()
window.title("Crear Usuario")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)



def open_new_window():
    window.withdraw()  
    subprocess.Popen(['python', 'C:\\Users\\nara\\Desktop\\Atento 2024\\Proyectos\\Taskify\\loginregister\\signin.py'])



def signup():
    name = user.get()
    password = code.get()
    conform_password = conform_code.get()
    if password == conform_password:
        try:
            conn = connect_to_database()
            cursor = conn.cursor()
            query = "INSERT INTO tu_tabla (name, password) VALUES (?, ?)"
            cursor.execute(query, (name, password))
            conn.commit()
            messagebox.showinfo('Creación de cuenta', 'Cuenta Creada Correctamente')
        except Exception as e:
            messagebox.showerror('Error', str(e))
    else:
        messagebox.showerror('Error', 'Ambas contraseñas deben coincidir')
    

image_path = "C:\\Users\\nara\\Desktop\\Atento 2024\\Proyectos\\Taskify\\images\\Logup.png"

#imagen
ruta_imagen = os.path.join("C:\\", "Users", "nara", "Desktop", "Atento 2024", "Proyectos", "Taskify", "images", "Logup.png")
img = PhotoImage(file=ruta_imagen)
Label(window, image=img, bg='white').place(x=50,y=90)

frame= Frame(window,width=350,height=390, bg='#fff')
frame.place (x=480, y=50)

heading =Label(frame,text="Crear Usuario", fg='#57a1f8',bg='white', font="Helvetica 14")
heading.place(x=100, y=50)

# input nombre 

user = Entry(frame, width=25, fg='black', border=0, bg="white", font="Helvetica 9")
user.place(x=30, y=80)
user.insert(0, 'Nombre de Usuario')
user.bind('<FocusIn>', lambda e: on_enter(e,user, 'Nombre de Usuario'))
user.bind('<FocusOut>', lambda e: on_leave(e,user, 'Nombre de Usuario'))

Frame(frame, width=296, height=1, bg='black').place(x=25, y=107)

#input contraseña

code = Entry(frame, width=25, fg='black', border=0, bg="white", font="Helvetica 9")
code.place(x=30, y=150)
code.insert(0, 'Contraseña')
code.bind('<FocusIn>', lambda e: on_enter(e,code, 'Contraseña'))
code.bind('<FocusOut>', lambda e: on_leave(e, code, 'Contraseña'))

Frame(frame, width=296, height=1, bg='black').place(x=25, y=177)

#input reingreso contraseña

conform_code = Entry(frame, width=25, fg='black', border=0, bg="white", font="Helvetica 9")
conform_code.place(x=30, y=220)
conform_code.insert(0, 'Reingrese Contraseña')
conform_code.bind('<FocusIn>', lambda e: on_enter(e,conform_code, 'Reingrese Contraseña'))
conform_code.bind('<FocusOut>', lambda e: on_leave(e,conform_code, 'Reingrese Contraseña'))

Frame(frame, width=296, height=1, bg='black').place(x=25, y=247)

#boton

Button(frame,width=39, pady=7,text='Crear', bg='#57a1f8', fg='white',border=0,command=signup).place(x=35, y=280)
label= Label(frame,text="¿Ya tienes cuenta?", fg='black', bg='white', font="Helvetica 12")
label.place(x=50, y=340)
signin= Button(frame,width=14, text='Ingresar a tu cuenta', border=0,bg='white',cursor='hand2', fg='#57a1f8', command=open_new_window)
signin.place(x=200,y=340)




window.mainloop()