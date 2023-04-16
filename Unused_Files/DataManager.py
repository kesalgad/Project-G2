import json

class DataManager:
    def __init__(self, inventarios_file, bodegas_file, distribuidores_file, entregas_file):
        self.inventarios_file = inventarios_file
        self.bodegas_file = bodegas_file
        self.distribuidores_file = distribuidores_file
        self.entregas_file = entregas_file

    def read_inventarios(self):
        try:
            with open(self.inventarios_file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return {}

    def write_inventarios(self, data):
        try:
            with open(self.inventarios_file, 'a') as f:
                json.dump(data, f, indent=4)
                f.write('\n')
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def read_bodegas(self):
        try:
            with open(self.bodegas_file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return {}

    def write_bodegas(self, data):
        try:
            with open(self.bodegas_file, 'a') as f:
                json.dump(data, f, indent=4)
                f.write('\n')
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def read_distribuidores(self):
        try:
            with open(self.distribuidores_file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return {}

    def write_distribuidores(self, data):
        try:
            with open(self.distribuidores_file, 'a') as f:
                json.dump(data, f, indent=4)
                f.write('\n')
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def read_entregas(self):
        try:
            with open(self.entregas_file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return {}

    def write_entregas(self, data):
        try:
            with open(self.entregas_file, 'a') as f:
                json.dump(data, f, indent=4)
                f.write('\n')
        except FileNotFoundError as e:
            print(f"Error: {e}")
