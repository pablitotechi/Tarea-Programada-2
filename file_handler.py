import os
import pickle

class FileHandler:
    def __init__(self, filename, table_size):
        self.filename = filename
        self.table_size = table_size
        self.table = [None] * table_size  # Crear la tabla vacía

        # Verificar si el archivo ya existe
        if os.path.exists(self.filename):
            self.table = self.load_table()  # Cargar la tabla desde el archivo

    def load_table(self):
        """ Cargar la tabla desde el archivo """
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

    def save_table(self):
        """ Guardar la tabla en un archivo """
        with open(self.filename, 'wb') as f:
            pickle.dump(self.table, f)

    def insert(self, key, data):
        """ Insertar datos en la tabla usando la clave """
        if 0 <= key < self.table_size:
            if self.table[key] is None:  # Si la posición está vacía
                self.table[key] = data
            else:
                print(f"Colisión registrada en {key}-col.dat.")
        else:
            print(f"Clave fuera de rango: {key}")

    def search(self, key):
        """ Buscar datos en la tabla usando la clave """
        if 0 <= key < self.table_size:
            return self.table[key]
        return None
