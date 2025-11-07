
import os
from modelo import *
if os.name == 'nt':
    os.system('cls')

biblioteca_json = BibliotecaJSON(ruta, biblioteca_base)

print('Bienvenido al sistema de gestión de biblioteca...')

def main():
    continuar = True
    biblioteca = biblioteca_json.cargar_biblioteca()

    while continuar:
        print(
        '''
        1. Ver Biblioteca 
        2. Agregar a la biblioteca
        3. Prestamos
        4. Devoluciones
        5. Buscar por nombre de autor
        6. Salir del programa
        '''
        )
        print('-' * 80)
        try:
            opcion = int(input('Escoge una opción del menú...'))
        except ValueError:
            print('Opción inválida...')
            continue

        match opcion:
            case 1:
                Libro.mostrar_libros(Libro, biblioteca)
                Revista.mostrar_revistas(Revista, biblioteca)
            case 2:
                biblioteca_json.agregar()
                biblioteca_json.actualizar_biblioteca(biblioteca)
            case 3:
                biblioteca_json.prestar()
            case 4:
                biblioteca_json.devolver()
            case 5:
                autor = input('Escribe el autor a buscar: ').strip().title()
                Formato.busqueda_autor(Formato, biblioteca, autor)
            case 6:
                print('Gracias por usar el programa...')
                continuar = False            
            case _:
                print('Debes escoger una opción del 1 al 6')

if __name__ == '__main__':
    main()
    

