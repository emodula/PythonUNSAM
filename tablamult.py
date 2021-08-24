# Ejercicio 3.17

# Imprime el espacio hasta que comienza la fila de numeros
print(f"{'':>6}", end="")

# Imprime la fila de numeros del 0 al 9
for i in range(10):
    print(f"{i:>4d}", end="")
print()  # Salto de linea

# Imprime separador
print("-" * 47)

# Imprime la tabla del 0
print(f"{'0:':<8}", end="")  # Imprime el 0: de la columna de numeros
for i in range(10):
    print(f"{(i-i):^4d}", end="")
print()  # Imprime salto de linea

# Imprime el resto de las tablas
for i in range(1, 10):
    print(f"{str(i)+':':<6}", end="")  # Imprime la columna del 1: al 9:
    z = 0
    for j in range(10):
        if i and j != 0:  # Si ninguno de los 2 numeros es el 0 imprime el resultado
            z += i
            print(f"{z:>4d}", end="")
        else:
            print(
                f"{'0':>4}", end=""
            )  # Si alguno de los 2 numeros es 0 imprime 0 como resultado
    print()  # Imprime salto de linea
