# ⚙️ Sistema de Carga y Búsqueda de Jugadas de Fútbol Americano

Este proyecto en Python permite cargar datos desde archivos `.csv`, procesarlos con una función hash personalizada y almacenarlos en archivos individuales. Además, proporciona un menú interactivo para buscar jugadas a partir de una clave hash calculada.

---

## 📁 Estructura del Proyecto

```bash
.
├── main.py               # Script principal con el menú interactivo
├── lector_data.py        # Lógica para cargar y procesar los archivos CSV
├── file_handler.py       # Clase para manejar inserciones y búsquedas de datos
├── hash_function.py      # Contiene la función personalizada 'calculate_hash'
├── data/                 # Carpeta con archivos .csv de entrada
├── output/               # Carpeta donde se guardan archivos por clave hash
📦 Requisitos
Este proyecto utiliza únicamente la biblioteca estándar de Python. No requiere instalación de paquetes externos.

🚀 Cómo ejecutar
Asegúrate de tener los archivos CSV en la carpeta data/

Ejecuta el menú principal:

bash
Copiar
Editar
python main.py
🧭 Menú de Usuario
Al ejecutar main.py, verás el siguiente menú:

markdown
Copiar
Editar
Menú:
1. Cargar datos
2. Buscar datos
3. Salir
1️⃣ Cargar datos
Lee todos los archivos .csv en la carpeta data/.

Cada línea válida se procesa para extraer los campos:

date, qtr, teams

Se calcula una clave hash con calculate_hash(date, qtr, teams)

Si la clave está entre 0 y 749:

Se inserta en file_handler

Se guarda un archivo output/{key}-col.dat con la jugada

2️⃣ Buscar datos
Introduce una clave (entre 0 y 749)

El sistema buscará la jugada en la base de datos simulada (file_handler)

3️⃣ Salir
Finaliza el programa

🧪 Ejemplo de línea válida en CSV
cs
Copiar
Editar
12:00;00:30;12:30;G123;TeamA vs TeamB;35;2;2022-09-01;12:05
🔑 Ejemplo de uso de hashing
La clave se calcula con una función personalizada basada en date, qtr y teams. Asegúrate de que calculate_hash en hash_function.py devuelva un entero entre 0 y 749.

📂 Ejemplo de archivo de salida
bash
Copiar
Editar
output/
├── 123-col.dat   # Contiene la jugada: "2022-09-01;2;TeamA





Dijiste:
en formato md 


ChatGPT dijo:
Aquí tienes el contenido completo del README.md en formato Markdown listo para copiar y usar:

markdown
Copiar
Editar
# ⚙️ Sistema de Carga y Búsqueda de Jugadas de Fútbol Americano

Este proyecto en Python permite cargar datos desde archivos `.csv`, procesarlos con una función hash personalizada y almacenarlos en archivos individuales. Además, proporciona un menú interactivo para buscar jugadas a partir de una clave hash calculada.

---

## 📁 Estructura del Proyecto

.
├── main.py # Script principal con el menú interactivo
├── lector_data.py # Lógica para cargar y procesar los archivos CSV
├── file_handler.py # Clase para manejar inserciones y búsquedas de datos
├── hash_function.py # Contiene la función personalizada 'calculate_hash'
├── data/ # Carpeta con archivos .csv de entrada
├── output/ # Carpeta donde se guardan archivos por clave hash

yaml
Copiar
Editar

---

## 📦 Requisitos

Este proyecto utiliza únicamente la biblioteca estándar de Python.  
No requiere instalación de paquetes externos.

---

## 🚀 Cómo ejecutar

1. Asegúrate de tener tus archivos `.csv` en la carpeta `data/`.
2. Ejecuta el script principal:

```bash
python main.py
🧭 Menú de Usuario
Al ejecutar main.py, verás el siguiente menú:

markdown
Copiar
Editar
Menú:
1. Cargar datos
2. Buscar datos
3. Salir
1️⃣ Cargar datos
Lee todos los archivos .csv en la carpeta data/.

Procesa cada línea para extraer:

date, qtr, teams

Calcula una clave hash con calculate_hash(date, qtr, teams)

Si la clave está entre 0 y 749:

Inserta los datos en file_handler

Guarda un archivo en output/{key}-col.dat con la jugada formateada

2️⃣ Buscar datos
Solicita al usuario una clave entre 0 y 749

Muestra la jugada correspondiente si existe

3️⃣ Salir
Cierra la aplicación

🧪 Ejemplo de línea válida en CSV
csv
Copiar
Editar
12:00;00:30;12:30;G123;TeamA vs TeamB;35;2;2022-09-01;12:05
