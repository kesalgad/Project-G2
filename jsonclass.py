import json

class DataManager:
    def __init__(self, inventarios_file, bodegas_file, distribuidores_file, entregas_file):
        self.inventarios_file = inventarios_file
        self.bodegas_file = bodegas_file
        self.distribuidores_file = distribuidores_file
        self.entregas_file = entregas_file
        
    def read_inventarios(self):
        return self.read_json_file(self.inventarios_file)
    
    def write_inventarios(self, data):
        self.write_json_file(data, self.inventarios_file)
    
    def read_bodegas(self):
        return self.read_json_file(self.bodegas_file)
    
    def write_bodegas(self, data):
        self.write_json_file(data, self.bodegas_file)
    
    def read_distribuidores(self):
        return self.read_json_file(self.distribuidores_file)
    
    def write_distribuidores(self, data):
        self.write_json_file(data, self.distribuidores_file)
    
    def read_entregas(self):
        return self.read_json_file(self.entregas_file)
    
    def write_entregas(self, data):
        self.write_json_file(data, self.entregas_file)

dm = DataManager('inventarios.json', 'bodegas.json', 'distribuidores.json', 'entregas.json')

# read the current JSON data from the file
data = dm.read_json_file('inventarios.json')
# create a new inventory item
new_item = {'id': 2, 'codProducto': 'NR 0090', 'descripcion': 'Escritorio de Madera', 'unidades': 5, 'codBodega': 'B002'}
# add the new item to the inventarios list in the JSON data
data['inventarios'].append(new_item)
# write the updated JSON data back to the file
dm.write_json_file(data, 'inventarios.json')

# read the current JSON data from the file
data = dm.read_json_file('bodegas.json')
# create a new bodega
new_item = {'id': 2, 'codBodega': 'B002', 'provincia': 'Heredia', 'canton': 'Ulloa', 'gerente': 'Pedro Navaja', 'telefono': '2222-2222'}
# add the new item to the inventarios list in the JSON data
data['bodegas'].append(new_item)
# write the updated JSON data back to the file
dm.write_json_file(data, 'bodegas.json')

#read the current JSON data from the file
data = dm.read_json_file('distribuidores.json')
# create a new distribuidor
new_item = {'id': 2, 'Empresa': 'XXX', 'cedJuridica': '3101321654', 'Zona': 'SUR', 'Direccion': 'Zona Franca PZ', 'telefono': '2222-2222', 'email': 'info@xxx.com'}
# add the new item to the distribuidores list
data['distribuidores'].append(new_item)
# write the updated JSON data back to the file
dm.write_json_file(data, 'distribuidores.json')

#read the current JSON data from the file
data = dm.read_json_file('entregas.json')
#create a entrega
new_item = {'id': '1', 'codProducto': 'NR 0090', 'descripcion': 'Escritorio de Madera', 'unidades': '5', 'codBodega': 'B002'}
#add the new item to the entregas list
data['entregas'].append(new_item)
