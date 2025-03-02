# main.py
from file_handler import FileHandler
from menu import menu

def main():
    data_folder = "/Users/pablogarro/data/segundaprogramada/data/data_entrada"
    output_folder = "/Users/pablogarro/data/segundaprogramada/data/data_salida"

    info_filename = "data_table.pkl"
    table_size = 750  # Asegúrate de que la tabla tenga un tamaño adecuado
    file_handler = FileHandler(info_filename, table_size)
    menu(file_handler, data_folder, output_folder)

if __name__ == "__main__":
    main()
