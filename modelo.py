from pathlib import Path
import json

class Formato: 
    """ 
    Esta será la super clase que engloba todos 
    los tipos de items disponibles en la biblioteca. 
    """ 
    def __init__(self, titulo, autor, disponible = True, usuario = None): 
        self.titulo = titulo 
        self.autor = autor 
        self._disponible = disponible 
        self._usuario = usuario

    @property 
    def disponible(self): #controlamos el acceso al estado del libro
        return self._disponible    

    @property #Controlamos el acceso al nombre del usuario
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

class Libro(Formato):
    """
    Esta clase hija añade nuevos elementos
    a los datos (año y genero)
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

class Revista(Formato):
    """
    Esta clase hija añade nuevos elementos
    a los datos (año y área, por ejemplo: 
    Biología, Informática)
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