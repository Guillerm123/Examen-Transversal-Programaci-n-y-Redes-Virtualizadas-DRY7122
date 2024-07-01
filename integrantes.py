# Creamos dos listas vacías para nombres y apellidos
nombres = []
apellidos = []

# Preguntamos al usuario cuántos integrantes tiene el grupo
cantidad_integrantes = int(input("¿Cuántos integrantes tiene el grupo? "))

# Pedimos los nombres y apellidos de cada integrante
for i in range(cantidad_integrantes):
    nombre_completo = input(f"Ingrese el nombre y apellido del integrante {i + 1}: ")
    nombre, apellido = nombre_completo.split()  # Dividimos el nombre completo en nombre y apellido
    nombres.append(nombre)
    apellidos.append(apellido)

# Imprimimos los resultados
print("Nombres de los integrantes:")
print(nombres)
print("Apellidos de los integrantes:")
print(apellidos)
