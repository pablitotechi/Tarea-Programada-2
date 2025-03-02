from lector_data import load_data
from file_handler import FileHandler

def menu(file_handler, data_folder, output_folder):
    while True:
        print("\nMenú:")
        print("1. Cargar datos")
        print("2. Buscar datos")
        print("3. Salir")
        option = input("Elige una opción: ")

        if option == '1':
            load_data(file_handler, data_folder, output_folder)
        elif option == '2':
            key = int(input("Introduce la llave (entre 0 y 749): "))
            result = file_handler.search(key)
            if result is not None:
                print(f"Datos encontrados: {result}")
            else:
                print(f"No se encontraron datos para la llave {key}.")
        elif option == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
