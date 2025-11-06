from pathlib import Path
import json

class Formato: 
    """ 
    Esta será la super clase que engloba todos 
    los tipos de items disponibles en la biblioteca. 
    """ 
    def __init__(self, titulo, autor, disponible = True, usuario = None): #Asignamos por defecto que el item se encuentra disponible y el valor de usuario vacío.
        self.titulo = titulo 
        self.autor = autor 
        self._disponible = disponible 
        self._usuario = usuario

    @property 
    def disponible(self): #controlamos el acceso al estado del libro.
        return self._disponible    

    @property #Controlamos el acceso al nombre del usuario.
    def usuario(self): 
        return self._usuario
    
    def prestar(self, usuario): 
        """ 
        Validamos si se encuentra disponible 
        en la biblioteca o ha sido prestado. 
        Asignamos el nombre del usuario que 
        tiene el libro. Se modifican los valores 
        correspondientes 
        """ 
        if not self._disponible: 
            print(f' {self.titulo} no se encuentra disponible, se ha prestado a {self._usuario}') 
        else: 
            self._disponible = False 
            self._usuario = usuario

    def devolver(self): 
        """ 
        Se valida si el libro esta disponible o 
        ha sido prestado. Se modifican los valores 
        correspondientes 
        """ 
        if self._disponible: 
            print(f"El recurso '{self.titulo}' ya ha sido devuelto.") 
        else: 
            self._disponible = True 
            self._usuario = None

    def diccionario_datos(self): 
        """ Se crea un diccionario con los datos 
        correspondientes a la clase. 
        """ 
        return { 
            "titulo": self.titulo, 
            "autor" : self.autor, 
            "disponible": self._disponible, 
            "usuario" : self._usuario 
            }

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
                # Si el elemento tiene "genero" (libros) o "area" (revistas), se muestra el campo correspondiente.
                categoria = elemento.get("genero", elemento.get("area", "N/A"))
                print(f"{elemento['titulo'].ljust(35)}{elemento['autor'].ljust(25)}{str(elemento['anio']).ljust(6)}{categoria.ljust(20)}{estatus}")
        else:
            print("No se encontraron coincidencias para ese autor.")
        print('-' * 100)

class Libro(Formato):
    """
    Esta clase hija añade nuevos elementos
    a los datos (año y genero)
    Además de mostrar sus elementos 
    en consola con comportamiento propio.
    """
    def __init__(self, titulo, autor, anio, genero, disponible = True, usuario = None):
        super().__init__(titulo, autor, disponible, usuario)
        self.anio = anio
        self.genero = genero
       
    def diccionario_datos(self):
        """
        Se agregan los nuevos datos
        al diccionario creado en la 
        clase padre.
        """
        dato = super().diccionario_datos()
        dato["anio"] = self.anio
        dato["genero"] = self.genero
        return dato
    
    def mostrar_libros(self, diccionario_datos):
        """
        Se muestra formateado para consola los libros
        registradas en la base de datos.
        """
        print('-' * 105)
        print('BIBLIOTECA DE LIBROS')
        print('-' * 105)
        print(f"{'TÍTULO'.ljust(35)}{'AUTOR'.ljust(25)}{'AÑO'.ljust(6)}{'GÉNERO'.ljust(20)}{'ESTATUS'}")
        print('-' * 105)
        for elemento in diccionario_datos: #Mostramos el libro como "disponible" o en caso de que este prestada se indica el nombre del usuario.
            estatus = "Disponible" if elemento["disponible"] else f"Prestado a {elemento['usuario']}"
            print(f"{elemento['titulo'].ljust(35)}{elemento['autor'].ljust(25)}{str(elemento['anio']).ljust(6)}{elemento['genero'].ljust(20)}{estatus}")
        print('-' * 105)


class Revista(Formato):
    """
    Esta clase hija añade nuevos elementos
    a los datos (año y área, por ejemplo: 
    Biología, Informática).
    Además de mostrar sus elementos 
    en consola con comportamiento propio.
    """
    def __init__(self, titulo, autor, anio, area, disponible = True, usuario = None):
        super().__init__(titulo, autor, disponible, usuario)
        self.anio = anio
        self.area = area
        
    def diccionario_datos(self):
        """
        Se agregan los nuevos datos
        al diccionario creado en la 
        clase padre.
        """
        dato = super().diccionario_datos()
        dato["anio"] = self.anio
        dato["area"] = self.area
        return dato
    
    def mostrar_revistas(self, diccionario_datos):
        """
        Se muestra formateado para consola las revistas
        registradas en la base de datos.
        """
        print('-' * 100)
        print('BIBLIOTECA DE REVISTAS')
        print('-' * 100)
        print(f"{'TÍTULO'.ljust(30)}{'AUTOR'.ljust(25)}{'AÑO'.ljust(8)}{'ÁREA'.ljust(18)}{'ESTATUS'}")
        print('-' * 100)
        for elemento in diccionario_datos: #Mostramos la revista como "disponible" o en caso de que este prestada se indica el nombre del usuario.
            estatus = "Disponible" if elemento["disponible"] else f"Prestado a {elemento['usuario']}"
            print(f"{elemento['titulo'].ljust(30)}{elemento['autor'].ljust(25)}{str(elemento['anio']).ljust(8)}{elemento['area'].ljust(18)}{estatus}")
        print('-' * 100)


ruta = 'biblioteca/biblioteca.json' #Establecemos el directorio y el nombre del archivo json.

#Generamos una biblioteca base para pruebas. En vez de usar una lista de diccionarios utilizamos las subclases y sus atributos para generar objetos.
biblioteca_base = [
    Libro('El Conde de Montecristo', 'Alexandre Dumas', 1845, 'Novela').diccionario_datos(),
    Libro('Así habló Zaratustra', 'Friedrich Nietzsche', 1883, 'Novela/Poesía').diccionario_datos(),
    Libro('Los hermanos Karamazov', 'Fiódor Dostoyevski', 1880, 'Novela').diccionario_datos(),
    Libro('Walden', 'Henry David Thoreau', 1845, 'Autobiografía').diccionario_datos(),
    Revista('National Geographic', 'Varios', 2023, 'Ciencia').diccionario_datos(),
    Revista('Nature', 'Varios', 2023, 'Ciencia').diccionario_datos(),
    Revista('Der Spiegel', 'Varios', 2023, 'Semanario').diccionario_datos()
    ]

class BibliotecaJSON:
    """
    Creación y gestión de la biblioteca
    para trabajar con ella en memoria
    y guardarla en un archivo json.
    """

    def __init__(self, ruta, biblioteca_base):
        """
        Se encapsulan los atributos para 
        indicar que no deben ser modificados.
        """
        self._ruta = Path(ruta)
        self._ruta.parent.mkdir(exist_ok=True)
        self._biblioteca_base = biblioteca_base
        self._biblioteca = []

    def cargar_biblioteca(self):
        """
        Carga la biblioteca desde el archivo JSON.
        Si no existe, crea el archivo con la biblioteca base.
        """
        if self._ruta.exists():
            try:
                with self._ruta.open('r', encoding='utf-8') as f:
                    self._biblioteca = json.load(f)
                return self._biblioteca
            except FileNotFoundError:
                print('Error: archivo no encontrado.')
            except PermissionError:
                print('Error: no tienes permisos para leer el archivo.')
            except Exception as e:
                print('Error inesperado:', type(e).__name__, e)
        else:
            print('No se encontró el archivo. Creando biblioteca base...')
            self.actualizar_biblioteca(self._biblioteca_base)
            self._biblioteca = self._biblioteca_base
            return self._biblioteca

    def actualizar_biblioteca(self, biblioteca):
        """
        Sobrescribe el json con la información actualizada.
        """
        try:
            with self._ruta.open('w', encoding='utf-8') as f:
                json.dump(biblioteca, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print('Error: no tienes permisos para escribir en el archivo.')
        except Exception as e:
            print('Error inesperado:', type(e).__name__, e)