import json

class DataManager:
    def __init__(self, inventarios_file, bodegas_file, distribuidores_file, entregas_file):
        self.inventarios_file = inventarios_file
        self.bodegas_file = bodegas_file
        self.distribuidores_file = distribuidores_file
        self.entregas_file = entregas_file

    def read_inventarios(self):
        with open(self.inventarios_file, 'r') as f:
            data = json.load(f)
        return data

    def write_inventarios(self, data):
        with open(self.inventarios_file, 'a') as f:
            json.dump(data, f, indent=4)
            f.write('\n')
        f.close()

    def read_bodegas(self):
        with open(self.bodegas_file, 'r') as f:
            data = json.load(f)
        return data

    def write_bodegas(self, data):
        with open(self.bodegas_file, 'a') as f:
            json.dump(data, f, indent=4)
            f.write('\n')
        f.close()

    def read_distribuidores(self):
        with open(self.distribuidores_file, 'r') as f:
            data = json.load(f)
        return data

    def write_distribuidores(self, data):
        with open(self.distribuidores_file, 'a') as f:
            json.dump(data, f, indent=4)
            f.write('\n')
        f.close()

    def read_entregas(self):
        with open(self.entregas_file, 'r') as f:
            data = json.load(f)
        return data

    def write_entregas(self, data):
        with open(self.entregas_file, 'a') as f:
            json.dump(data, f, indent=4)
            f.write('\n')
        f.close()
