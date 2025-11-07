# biblioteca

PARTICIPANTES:

1. Adeel Fiaz
2. José Salazar

CONTRIBUCIONES:

- modelo.py -> José Salazar
- menu.py y fx agregar_libro -> Adeel Fiaz

MÓDULOS UTILIZADOS:

1. pathlib
2. json
3. os

PROMPT CHATGPT(JOSÉ SALAZAR):

def mostrar_libros(self, diccionario_datos):
""" Se muestra formateado para consola los libros registradas en la base de datos. """
print('-' * 80)
print('BIBLIOTECA DE LIBROS')
print('-' * 80)
print(f"{'TÍTULO'.ljust(30)}{'AUTOR'.ljust(25)}{'AÑO'.ljust(8)}{'GÉNERO'.ljust(18)}{'ESTATUS'}")
print('-' * 80)
for elemento in diccionario_datos: estatus = "Disponible" if elemento["disponible"] else f"Prestado a {elemento['usuario']}"
print(f"{elemento['titulo'].ljust(25)}{elemento['autor'].ljust(20)}{str(elemento['anio']).ljust(5)}{elemento['genero'].ljust(10)}{estatus}")
rint('-' * 80)

ayudame a formatear los valores de ljust para obtener una salida en consola ordenada y simetrica
tomando como referencia valores estandares para cada campo. No modifiques el codigo, solo necesito ajustar
los valores de ljust. Si tienes alguna sugerencia lo haces por separado

RESPUESTA:

Perfecto 👍.
Tu código está bien estructurado, solo necesita un mejor ajuste de los valores de ljust para que las columnas queden alineadas visualmente en consola.
Aquí te paso una propuesta con valores más equilibrados para los anchos de columna:
print(f"{'TÍTULO'.ljust(35)}{'AUTOR'.ljust(25)}{'AÑO'.ljust(6)}{'GÉNERO'.ljust(20)}{'ESTATUS'}")
...
print(f"{elemento['titulo'].ljust(35)}{elemento['autor'].ljust(25)}{str(elemento['anio']).ljust(6)}{elemento['genero'].ljust(20)}{estatus}")
📏 Justificación de los valores:
TÍTULO → 35: Los títulos suelen ser los textos más largos. Un ancho de 35 evita que se solapen con el autor.
AUTOR → 25: Espacio suficiente para nombres compuestos o largos.
AÑO → 6: Aunque solo tiene 4 dígitos, se deja un poco de margen para la separación visual.
GÉNERO → 20: Adecuado para géneros más extensos (p. ej. Ciencia Ficción o Literatura Fantástica).
ESTATUS: No necesita ljust porque suele ir al final y tiene longitud variable.

PROMPT CHATGPT(JOSÉ SALAZAR):
utilizando los mismos formatos de salida para consola refactoriza esta funcion para obtener un resultado similar con
las coincidencias de busqueda def busqueda_autor(diccionario_datos, autor_buscado):
""" Se muestran las coincidencias
que existan para la búsqueda por nombre de autor. Se simplifica el código usando lista de comprensión. """
return [item for item in diccionario_datos if autor_buscado.lower() in item["autor"].lower()]

RESPUESTA:
Perfecto ✅
Vamos a refactorizar tu función busqueda_autor para que no solo devuelva la lista de coincidencias,
sino que muestre en consola los resultados formateados de forma idéntica a las funciones mostrar_libros y mostrar_revistas.
Aquí tienes la versión refactorizada:
def busqueda_autor(diccionario_datos, autor_buscado):
    """
    Muestra las coincidencias que existan para la búsqueda por nombre de autor,
    formateadas en consola con el mismo estilo que las funciones de listado.
    """
    coincidencias = [item for item in diccionario_datos if autor_buscado.lower() in item["autor"].lower()]

    print('-' * 100)
    print(f"RESULTADOS DE BÚSQUEDA - AUTOR: {autor_buscado.upper()}")
    print('-' * 100)
    print(f"{'TÍTULO'.ljust(35)}{'AUTOR'.ljust(25)}{'AÑO'.ljust(6)}{'GÉNERO/ÁREA'.ljust(20)}{'ESTATUS'}")
    print('-' * 100)

    if coincidencias:
        for elemento in coincidencias:
            estatus = "Disponible" if elemento["disponible"] else f"Prestado a {elemento['usuario']}"
            # Si el elemento tiene "genero" (libros) o "area" (revistas), se muestra el campo correspondiente
            categoria = elemento.get("genero", elemento.get("area", "N/A"))
            print(f"{elemento['titulo'].ljust(35)}{elemento['autor'].ljust(25)}{str(elemento['anio']).ljust(6)}{categoria.ljust(20)}{estatus}")
    else:
        print("No se encontraron coincidencias para ese autor.")

    print('-' * 100)

PROMPT CHATGPT (JOSE):

def devolver(self, titulo):
        """
        Se valida si el libro esta disponible o
        ha sido prestado. Se modifican los valores
        correspondientes
        """
        for elemento in self._biblioteca:
            if elemento["titulo"].lower() == titulo.lower():
                if elemento["disponible"]:
                    print(f"'{titulo}' ya estaba disponible.")
                    return
                elemento["disponible"] = True
                elemento["usuario"] = None
                print(f"'{titulo}' ha sido devuelto correctamente.")
                self.actualizar_biblioteca(self._biblioteca)
                return
        print("No se encontró el título.")

Quiero que la funcion arroje un mensaje al usuario que diga que no hay nada para devolver si todos los articulos de la biblioteca se encuentran en estatus disponible


RESPUESTA:

Perfecto 👍

Podemos agregar una verificación **antes del bucle** que revise si **todos los elementos** de la biblioteca están ya disponibles.

Si ese es el caso, la función mostrará el mensaje:

> "No hay nada para devolver. Todos los artículos están disponibles."

Aquí tienes el código modificado:

def devolver(self, titulo):
    """
    Se valida si el libro está disponible o
    ha sido prestado. Se modifican los valores
    correspondientes.
    """
    # ✅ Verificamos si todos los elementos están disponibles
    if all(elemento["disponible"] for elemento in self._biblioteca):
        print("No hay nada para devolver. Todos los artículos están disponibles.")
        return

    # 🔍 Buscamos el título en la biblioteca
    for elemento in self._biblioteca:
        if elemento["titulo"].lower() == titulo.lower():
            if elemento["disponible"]:
                print(f"'{titulo}' ya estaba disponible.")
                return
            elemento["disponible"] = True
            elemento["usuario"] = None
            print(f"'{titulo}' ha sido devuelto correctamente.")
            self.actualizar_biblioteca(self._biblioteca)
            return

    print("No se encontró el título.")
