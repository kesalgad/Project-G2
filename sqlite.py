import sqlite3

class SQLite:
    def __init__(self):
        self.conn = sqlite3.connect('AppInventario.db')
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS inventarios 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                codProducto TEXT PRIMARY KEY AUTOINCREMENT NOT NULL,
                                descripcion TEXT NOT NULL,
                                unidades INTEGER NOT NULL,
                                codBodega TEXT NOT NULL,)""")
        self.conn.commit()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bodegas
                            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            codBodega TEXT NOT NULL,
                            provincia TEXT NOT NULL,
                            canton TEXT NOT NULL,
                            gerente TEXT NOT NULL,
                            telefono TEXT NOT NULL,)""")
        self.conn.commit()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS distribuidores
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            empresa TEXT NOT NULL,
                            cedJuridica TEXT NOT NULL,
                            zona TEXT NOT NULL,
                            direccion TEXT NOT NULL,
                            telefono TEXT NOT NULL,
                            email TEXT NOT NULL,)""")
        self.conn.commit
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS entregas
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            distribuidor TEXT NOT NULL,
                            unidades INTEGER NOT NULL,
                            fechaEntrega TEXT NOT NULL,)""")
        self.conn.commit()        
                            