
import os
if os.name == 'nt':
    os.system('cls')


print('Bienvenido a Library_Wizard 1.0, biblioteca personal...')

def main():
    continuar = True

    while continuar:
        print(
        '''
        1. Ver Biblioteca 
        2. Agregar libro
        3. Prestar libro
        4. Devolver libro
        5. Buscar libro
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
                pass
            case 2:
                pass 
            case 3:
                pass            
            case 4:
                pass   
            case 5:
                pass
            case 6:
                print('Gracias por usar el programa.')
                continuar = False            
            case _:
                print('Debes escoger una opción del 1 al 6')

if __name__ == '__main__':
    main()
    

