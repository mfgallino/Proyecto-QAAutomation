import csv
import pathlib # Librería para poder llamar al path del archivo 


def leer_csv_login(ruta_archivo):
    ruta = pathlib.Path(ruta_archivo)
    datos = []
    with open(ruta, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            # Comparar el dato del parámetro "debe_funcionar" y asignar el resultado (booleano) a la variable. 
            debe_funcionar = fila["debe_funcionar"].lower() == "true"
            """ (Esto es un recurso para convertir el valor del parámetro 'debe_funcionar' de 'str' a 'bool') """
            

            datos.append((fila["usuario"], fila["password"], debe_funcionar))
    return datos


