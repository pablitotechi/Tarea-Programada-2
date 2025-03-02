import os
from hash_function import calculate_hash

def load_data(file_handler, data_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Carpeta '{output_folder}' creada.")
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            print(f"Procesando archivo: {filename}")
            with open(os.path.join(data_folder, filename), 'r') as file:
                next(file)

                for line in file:
                    try:
                        # Dividir por el delimitador ";"
                        columns = line.split(';')

                        if len(columns) >= 9:
                            start_time = columns[0]  # start_time
                            duracion = columns[1]  # duracion
                            end_time = columns[2]  # end_time
                            game_id = columns[3]  # game_id
                            teams = columns[4]  # teams
                            yards = columns[5]  # yards
                            qtr = columns[6]  # qtr
                            date = columns[7]  # date
                            time = columns[8]  # time

                            key = calculate_hash(date, qtr, teams)

                            if 0 <= key < 750:
                                punt_play = f"{date};{qtr};{teams}"
                                file_handler.insert(key, punt_play)
                                output_filename = os.path.join(output_folder, f"{key}-col.dat")
                                with open(output_filename, 'w') as output_file:
                                    output_file.write(punt_play)
                                    print(f"Archivo guardado: {output_filename}")
                            else:
                                print(f"Clave fuera de rango: {key}")
                        else:
                            print(f"Línea mal formateada (ignorando): {line.strip()}")
                    except Exception as e:
                        print(f"Línea mal formateada (ignorando): {line.strip()} | Error: {e}")
