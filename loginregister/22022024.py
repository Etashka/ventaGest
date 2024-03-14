
 #Este es el archivo de la ventana en la que se puede ver una tabla y un form con la carga de los datos. 
from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation
from ttkbootstrap.toast import ToastNotification 
import pyodbc

server = 'DESKTOP-8SVO4TR'
bbdd = 'ATENTO_CAPACITACION'
user = ''
password = ''

class Contact_info(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding= (20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.name = ttk.StringVar(value= "")
        self.email = ttk.StringVar(value= "")
        self.password = ttk.StringVar(value= "")
        self.page = ttk.StringVar(value= "0")
        self.data = []
        self.rows_per_page = 5
        self.colors = master_window.style.colors

        instruction_text = "Por favor ingrese su información:"
        instruction =  ttk.Label(self, text=instruction_text, width = 50 )
        instruction.pack(fill=X, pady=10)

        self.create_form_entry ("Nombre: ", self.name)
        self.create_form_entry ("Contraseña: ", self.password)
        self.create_form_entry ("Correo electronico: ", self.email)
        self.create_form_entry ("Pagina Web: ", self.page)

        self.create_meter()
        self.create_buttonbox()

        self.table = self.create_table()


        

    def prev_page(self):
        
        current_page_index = int(self.page.get())

        
        if current_page_index > 0:
            self.page.set(str(current_page_index - 1))
            self.update_table()
        self.update_table()

    def next_page(self):
        current_page_index = int(self.page.get())
        self.page.set(str(current_page_index + 1))
        self.update_table()
        

    def update_table(self):
        # Obtener los datos de la base de datos
        try:
            connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bbdd+';UID='+user+';PWD='+password)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM tu_tabla")
            rows = cursor.fetchall()
        except pyodbc.Error as x:
            print("Ocurrió un error durante la consulta de datos:", x)

       
        current_page_index = int(self.page.get())

        
        start_index = current_page_index * self.rows_per_page
        end_index = start_index + self.rows_per_page

        
        page_rows = rows[start_index:end_index]

        
        self.table.set_rowdata(page_rows)





    #Creando los inputs
    def create_form_entry(self, label,variable):
        
        form_field_container = ttk.Frame(self)
        form_field_container.pack( fill= X, expand=YES, pady=5)

        form_field_label = ttk.Label(master = form_field_container, text=label, width = 15 )
        form_field_label.pack(side= LEFT, padx=12)
        
        form_input = ttk.Entry(master = form_field_container, textvariable= variable)
        if label.lower().startswith("contraseña"):
            form_input.config(show="•")
        form_input.pack(side= LEFT, padx=5, fill=X, expand= YES)

        add_regex_validation(form_input, r'^[a-zA-Z0-9_.@ ]*$')
        return form_input




    #Creando medidor
    
    def create_meter(self):
        self.page.set('0')
        self.meter = ttk.Meter(
            master=self,
            metersize=220,
            padding=5,
            amounttotal=100,
            amountused=len(self.data),
            metertype="full",
            subtext="Contraseñas Guardadas",  
            interactive=True
        )
        
        self.meter.pack()
        

    

    def update_meter(self):
        self.meter.amountusedvar.set(len(self.data))
    
    
        

    #Creando botones
    def create_buttonbox(self):
        button_container = ttk.Frame (self)
        button_container.pack(fill=X, expand=YES, pady=(15,10))

        cancel_btn = ttk.Button(
            master=button_container,
            text= "Cancelar",
            command= self.on_cancel,
            bootstyle = DANGER,
            width= 6,
        )
        cancel_btn.pack(side=RIGHT, padx=5)

        submit_btn = ttk.Button(
            master=button_container,
            text= "Enviar",
            command= self.on_submit,
            bootstyle = SUCCESS,
            width= 6,
        )

        submit_btn.pack(side=RIGHT, padx=5)
        
   

    #Acción cuando se hace click en "Enviar"

    def on_submit(self):
        name = self.name.get()
        password = self.password.get()
        email = self.email.get()
        page = self.page.get()

        try:
            connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bbdd+';UID='+user+';PWD='+password)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tu_tabla(name,password,email,page) VALUES (?, ?, ?, ?)",(name, password, email, page))
            cursor.commit()

            rowcount = cursor.rowcount
            if rowcount > 0:
                print("Se insertó una fila correctamente.")
            else:
                print("No se insertó ninguna fila.")

            cursor.execute("SELECT * FROM tu_tabla")
            rows = cursor.fetchall()

            for row in rows:
                print(f"id: {row[0]}, Nombre: {row[1]}, Contraseña: {row[2]}, Correo electrónico: {row[3]},Pagina Web: {row[4]} ")

            self.data.append((name, email, password,page))
            self.table.destroy()
            self.table = self.create_table()

            self.update_meter()

            toast = ToastNotification(
                title="Envío Correcto",
                message="Su información ha sido enviada de forma correcta.",
                duration=3000,
            )

            toast.show_toast()

        except pyodbc.Error as x:
            print("Ocurrió un error durante la inserción de datos:", x)


            
    
    #Acción cuando se hace click en "Cancelar"
    def on_cancel(self):
        self.quit()
        
    
   ############    TABLA 
    
    def create_table(self):
        coldata = [
            {"text": "ID"},
            {"text": "Nombre"},
            {"text": "Contraseña"},
            {"text": "Correo Electronico"},   
            {"text": "Pagina web"},
            
        ]
        table = Tableview(
                master=self,
                coldata=coldata,
                rowdata=[("", "", "", "", "")] * self.rows_per_page,   
                paginated=True,
                searchable=True,
                bootstyle=PRIMARY,
                stripecolor=(self.colors.light, None),
            )

        
        try:
            connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bbdd+';UID='+user+';PWD='+password)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM tu_tabla")
            rows = cursor.fetchall()
            self.data = rows
        except pyodbc.Error as x:
            print("Ocurrió un error durante la consulta de datos:", x)

        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(self.colors.light, None),
        )

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        
        return table
    
    ################################

        

    



    

    




if __name__== "__main__":
    app = ttk.Window("Informacion de contacto", "superhero", resizable =(True,True))
    Contact_info(app)
   
    app.mainloop()
