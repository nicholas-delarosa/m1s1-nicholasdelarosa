
# Inventario Simple en Python

Script en Python para registrar productos en un inventario desde la terminal.  
El programa solicita al usuario el **nombre**, **precio** y **cantidad** de cada producto, valida los datos ingresados y calcula el **costo total por producto**.

## Características

- Entrada de datos desde la terminal.
- Validación de errores para números enteros (`int`) y decimales (`float`).
- Registro de múltiples productos en una sola ejecución.
- Cálculo automático del costo total (`precio × cantidad`).
- Salida clara y formateada en pantalla.

## Requisitos

- Python 3.x

No se requieren librerías externas.

## Uso

1. Guarda el código en un archivo llamado `inventario.py`.
2. Ejecuta el script desde la terminal:


python inventario.py


3. Ingresa los datos solicitados por el programa.

Ejemplo:


¿Cuántos productos desea ingresar?
2

Ingrese el nombre del producto: Manzana
Ingrese el precio del producto: $1.5
Ingrese la cantidad de Manzana que desea ingresar: 10
Producto: Manzana | Precio: $1.5 | Cantidad: 10 | Total: $15.0

Ingrese el nombre del producto: Pan
Ingrese el precio del producto: $2
Ingrese la cantidad de Pan que desea ingresar: 3
Producto: Pan | Precio: $2.0 | Cantidad: 3 | Total: $6.0


## Funcionamiento

El programa utiliza dos funciones auxiliares para validar la entrada del usuario:

* `pedir_entero(mensaje)`
  Solicita un número entero y repite la pregunta hasta que el usuario ingrese un valor válido.

* `pedir_flotante(mensaje)`
  Solicita un número decimal y valida que la entrada sea correcta.

Flujo general del programa:

1. Se pregunta cuántos productos se desean ingresar.
2. Mientras queden productos por registrar:

   * Se solicita el nombre del producto.
   * Se solicita el precio (decimal).
   * Se solicita la cantidad (entero).
3. Se calcula el costo total (`precio × cantidad`).
4. Se muestra la información del producto en pantalla.
5. El proceso se repite hasta completar la cantidad de productos indicada.

## Estructura del programa

```
inventario.py
 ├─ pedir_entero()     # Validación de números enteros
 ├─ pedir_flotante()   # Validación de números decimales
 └─ Bucle principal    # Registro de productos y cálculo de totales
```

## Autor

Nicholas De la Rosa
GitHub: [https://github.com/nicholas-delarosa](https://github.com/nicholas-delarosa)
