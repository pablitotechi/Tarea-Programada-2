from file_handler import FileHandler

def buscar_datos(file_handler):
    try:
        key = int(input("Introduce la llave (entre 0 y 749): "))

        if not (0 <= key <= 749):
            print("La llave debe estar entre 0 y 749.")
            return

        # Buscar el registro en la tabla
        record = file_handler.get(key)

        if record is None:
            print("El registro está vacío.")
        else:
            print("Registro encontrado:")
            if isinstance(record, list):
                print(f"En info.dat: {record[0].strip()}")
                print("Colisiones:")
                for r in record[1:]:
                    print(r.strip())
            else:
                print(record.strip())
    except ValueError:
        print("La llave debe ser un número entero entre 0 y 749.")
