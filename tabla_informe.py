# Ejercicio 3.16

import csv

costo_camion = 0
venta_total = 0

# funcion que crea lista de diccionarios con el contenido del camion
def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for i, line in enumerate(rows):
            record = dict(zip(headers, line))
            camion.append(record)
        return camion


# funcion que crea diccionario con los precios de cada fruta
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


# Funcion que crea lista de tuplas con el informe (Nombre, cajones, precio, cambio)
def hacer_informe(camion, precios):
    informe = []
    for i, line in enumerate(camion):
        precio_venta_cajon = precios[camion[i]["nombre"]]
        cambio = float(precio_venta_cajon) - float(camion[i]["precio"])
        registro = (
            camion[i]["nombre"],
            int(camion[i]["cajones"]),
            float(camion[i]["precio"]),
            cambio,
        )
        informe.append(registro)
    return informe


# Funcion que imprime informe con formato de tabla
def imprimir_informe(tabla):
    headers = ("Nombre", "Cajones", "Precio", "Cambio")
    print()

    for i in headers:  # Imprime encabezados
        print(f"{i:^12s}", end="")
    print()

    for i in headers:  # Imprime separador
        print(f"{'-' * 11:^12}", end="")
    print()

    for nombre, cajones, precio, cambio in tabla:  # Imprime datos
        print(f"{nombre:<10s} {cajones:>10d} {'$' + str(precio):>10s} {cambio:>10.2f}")
    print()


camion = leer_camion("../Data/camion.csv")
precios = leer_precios("../Data/precios.csv")
informe = hacer_informe(camion, precios)
imprimir_informe(informe)

for line in camion:
    costo_camion += int(line["cajones"]) * float(line["precio"])
    venta_total += int(line["cajones"]) * precios[line["nombre"]]

diferencia = round((venta_total - costo_camion), 2)
if diferencia > 0:
    print(f"El balance fue positivo con una ganancia de ${diferencia}")
else:
    print(f"El balance fue negativo con una perdida de ${diferencia}")
