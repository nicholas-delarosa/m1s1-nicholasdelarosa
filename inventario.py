# Función para pedir un entero válido
def ask_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

# Función para pedir un flotante válido
def ask_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Por favor, ingrese un número decimal válido (ejemplo: 10.5).")

# Preguntar cuántos productos en total el usuario desea ingresar
ask_quantity_insert = ask_integer("¿Cuántos productos desea ingresar?\n")

# Bucle que se ejecuta mientras queden productos por ingresar
while ask_quantity_insert != 0:

    # Solicitar el nombre del producto
    ask_name = input("Ingrese el nombre del producto: ")

    # Solicitar el precio del producto
    ask_price = ask_float("Ingrese el precio del producto: $")

    # Solicitar la cantidad del producto
    ask_quantity = ask_integer(f"Ingrese la cantidad de {ask_name} que desea ingresar: ")

    # Calcular el costo total del producto
    total_cost = ask_price * ask_quantity

    # Mostrar los resultados en pantalla
    print(f"Producto: {ask_name} | Precio: ${ask_price} | Cantidad: {ask_quantity} | Total: ${total_cost}")

    # Reducir en uno la cantidad de productos restantes
    ask_quantity_insert -= 1

# Este programa permite al usuario ingresar múltiples productos al inventario.
# Para cada producto se solicita el nombre, el precio y la cantidad con validación de errores.
# Luego se calcula el costo total multiplicando el precio por la cantidad y se muestra la información en pantalla.
# El proceso se repite hasta que se haya ingresado la cantidad de productos indicada por el usuario.
