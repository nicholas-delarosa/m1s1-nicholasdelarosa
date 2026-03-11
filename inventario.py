# Solicitar el nombre del producto
ask_nombre = input("Ingrese el nombre del producto: ")

# Validar que el precio sea un número decimal válido
while True:
    try:
        # Solicitar el precio del producto
        ask_precio = float(input("Ingrese el precio del producto: $"))
        break
    except ValueError:
        # Mensaje de error si el valor no es válido
        print("Error: Por favor, ingrese un número decimal válido (ejemplo: 10.5).")

# Validar que la cantidad sea un número entero válido
while True:
    try:
        # Solicitar la cantidad del producto
        ask_cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        # Mensaje de error si el valor no es válido
        print("Error: Por favor, ingrese un número entero válido.")