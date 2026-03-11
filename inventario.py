# Solicitar el nombre del producto
ask_nombre = input("Ingrese el nombre del producto: ")

# Validar precio
while True:
    try:
        ask_precio = float(input("Ingrese el precio del producto: $"))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número decimal válido (ejemplo: 10.5).")

# Validar cantidad
while True:
    try:
        ask_cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# Calcular el costo total del producto
costo_total = ask_precio * ask_cantidad