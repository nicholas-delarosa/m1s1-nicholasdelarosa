# Función para pedir un entero válido
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

# Función para pedir un flotante válido
def pedir_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingrese un número decimal válido (ejemplo: 10.5).")

# Preguntar cuántos productos en total el usuario desea ingresar
ask_cantidad_ingresar = pedir_entero("¿Cuántos productos desea ingresar?\n")

# Bucle que se ejecuta mientras queden productos por ingresar
while ask_cantidad_ingresar != 0:

    # Solicitar el nombre del producto
    ask_nombre = input("Ingrese el nombre del producto: ")

    # Solicitar el precio del producto
    ask_precio = pedir_flotante("Ingrese el precio del producto: $")

    # Solicitar la cantidad del producto
    ask_cantidad = pedir_entero(f"Ingrese la cantidad de {ask_nombre} que desea ingresar: ")

    # Calcular el costo total del producto
    costo_total = ask_precio * ask_cantidad

    # Mostrar los resultados en pantalla
    print(f"Producto: {ask_nombre} | Precio: ${ask_precio} | Cantidad: {ask_cantidad} | Total: ${costo_total}")

    # Reducir en uno la cantidad de productos restantes
    ask_cantidad_ingresar -= 1

# Este programa permite al usuario ingresar múltiples productos al inventario.
# Para cada producto se solicita el nombre, el precio y la cantidad con validación de errores.
# Luego se calcula el costo total multiplicando el precio por la cantidad y se muestra la información en pantalla.
# El proceso se repite hasta que se haya ingresado la cantidad de productos indicada por el usuario.