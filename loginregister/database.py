#base datos 
import pyodbc

server = 'tu_server'
bbdd = 'tu_ddbb'
user = ''
password = ''

def connect_to_database():
    # Conexión a la base de datos
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+bbdd+';UID='+user+';PWD='+password)
    return conn