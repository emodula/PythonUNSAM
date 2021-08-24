# Ejercicio 3.18

from collections import Counter
import csv

archivo = "../Data/arbolado-en-espacios-verdes.csv"

# Si se quiere analizar para toda la ciudad dejar la variable vacia ("")
parque_elegido = "CENTENARIO"

especie_elegido = "Jacarandá"


# Genera lista de diccionarios con la informacion
def leer_parque(nombre_archivo, parque_elegido):

    if parque_elegido != "":  # Si no se elige parque analiza para toda la ciudad

        with open(nombre_archivo) as f:
            rows = csv.reader(f)
            headers = next(rows)
            arboles_parque = []
            for line in rows:
                registro = {}
                registro = dict(zip(headers, line))
                if registro["espacio_ve"] == parque_elegido:
                    arboles_parque.append(registro)
        return arboles_parque
    else:
        with open(nombre_archivo) as f:
            rows = csv.reader(f)
            headers = next(rows)
            arboles_ciudad = []
            for line in rows:
                registro = {}
                registro = dict(zip(headers, line))
                arboles_ciudad.append(registro)
        return arboles_ciudad


# Genera un conjunto (set) de las especies de arboles
def especies(lista_arboles):
    set_especies = set()
    for line in lista_arboles:
        set_especies.add(line["nombre_com"])
    return set_especies


# Genera un contador con la cantidad de ejemplares por especie
def contar_ejemplares(lista_arboles):
    cantidad_ejemplares = Counter()
    for line in lista_arboles:
        cantidad_ejemplares[line["nombre_com"]] += 1
    return cantidad_ejemplares


# Genera una lista con las alturas de la especie elegida
def obtener_alturas(lista_arboles, especie_elegido):
    altura_arbol = []
    for line in lista_arboles:
        if line["nombre_com"] == especie_elegido:
            altura = float(line["altura_tot"])
            altura_arbol.append(altura)
    return altura_arbol


# Genera una lista con las inclinaciones de la especie elegida
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for line in lista_arboles:
        if line["nombre_com"] == especie:
            inclinaciones.append(float(line["inclinacio"]))
    return inclinaciones


# Genera un diccionario con la especie y los grados del arbol mas inclinado
def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    mas_inclinados = {}
    for especie in lista_especies:
        mas_inclinados[especie] = max(obtener_inclinaciones(lista_arboles, especie))
    maximo = max(mas_inclinados, key=mas_inclinados.get)
    arbol_mas_inclinado = (maximo, mas_inclinados[maximo])
    return arbol_mas_inclinado


# Genera un diccionario con la especie y los grados de la especie con mas inclinacion en promedio
def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = especies(lista_arboles)
    inclinaciones_promedio = {}
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        promedio = float(sum(inclinaciones) / len(inclinaciones))
        inclinaciones_promedio[especie] = promedio

    # Obtiene la key del diccionario con mayor value
    maximo = max(inclinaciones_promedio, key=inclinaciones_promedio.get)

    arbol_mas_inclinado_promedio = (maximo, inclinaciones_promedio[maximo])
    return arbol_mas_inclinado_promedio


# Genera una tupla con latitud y longitud del arbol
def obtener_lat_long(lista_arboles, arbol):
    for line in lista_arboles:
        if line["nombre_com"] == arbol:
            lat_long = (line["lat"], line["long"])
    return lat_long


lista_arboles = leer_parque(archivo, parque_elegido)
lista_especies = especies(lista_arboles)
cantidad_ejemplares = contar_ejemplares(lista_arboles)
mas_comunes = cantidad_ejemplares.most_common(5)
alturas_especie = obtener_alturas(lista_arboles, especie_elegido)
altura_promedio_especie = sum(alturas_especie) / len(alturas_especie)
altura_max_especie = max(alturas_especie)
arbol_mas_inclinado = especimen_mas_inclinado(lista_arboles)
arbol_mas_inclinado_promedio = especie_promedio_mas_inclinada(lista_arboles)
lat_long = obtener_lat_long(lista_arboles, arbol_mas_inclinado[0])
print(
    f"El arbol mas inclinado es de la especie {arbol_mas_inclinado[0]} con una inclinacion de {arbol_mas_inclinado[1]} grados. Se encuentra en LAT {lat_long[0]} y LONG {lat_long[1]}"
)
print(
    f"El arbol mas inclinado en promedio es de la especie {arbol_mas_inclinado_promedio[0]} con una inclinacion de {arbol_mas_inclinado_promedio[1]} grados"
)
