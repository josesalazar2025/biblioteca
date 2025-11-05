
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