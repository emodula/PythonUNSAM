# Ejercicio 3.9

import csv

costo_camion = 0
venta_total = 0


def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for i, line in enumerate(rows):
            record = dict(zip(headers, line))
            camion.append(record)
            print(camion)
        return camion


def leer_precios(nombre_archivo):
    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        precios = {}
        for i, line in enumerate(rows):
            try:
                precios[line[0]] = float(line[1])
            except IndexError:
                print(f"Datos incompletos en linea {i}")
        return precios


lista = leer_camion("../Data/fecha_camion.csv")
consultar_precios = leer_precios("../Data/precios.csv")


for line in lista:
    costo_camion += int(line["cajones"]) * float(line["precio"])
    venta_total += int(line["cajones"]) * consultar_precios[line["nombre"]]

diferencia = round((venta_total - costo_camion), 2)
if diferencia > 0:
    print(f"El balance fue positivo con una ganancia de ${diferencia}")
else:
    print(f"El balance fue negativo con una perdida de ${diferencia}")
