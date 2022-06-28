'''
Creado por Quizaira Rodriguez
'''

import random
import string

intentos = 7
contraseña_ajustes = "ajustes"
categorias = {
    "MEDICINA": ["ARTICULACION", "MUSCULO", "CRANEO", "ESTOMAGO"],
    "PAISES": ["ARGENTINA", "COLOMBIA", "ALEMANIA", "INGLATERRA"],
    "COMIDA": ["AREPA", "PIZZA", "EMPANADA", "MILANESA"]
}

vidas_graficos = [
     """
         ___________
        | /        | 
        |/        \☻/
        |          |
        |        ./ \.
        |
    """,
    """
         ___________
        | /        | 
        |/         ☻
        |          |
        |        ./ \.
        |
    """,
    """
         ___________
        | /        | 
        |/         ☻
        |          |
        |          
        |
    """,
    """
         ___________
        | /        | 
        |/         ☻
        |          
        |          
        |
    """,
    """
         ___________
        | /        | 
        |/        
        |          
        |          
        |
    """,
    """
         ___________
        | /        
        |/        
        |          
        |          
        |
    """,
    """
        |
        |
        |
        |
        |
    """,
    "",
]

def verificar(dato):
    while dato == "":
        dato= input("\nOpps!! Ha ocurrido un error. Ingrese el dato nuevamente: >>> ")
    return dato

def crear_categoria_palabras():
    categoria = input("\nIngrese el nombre de la nueva categoría de palabras: >>> ")
    categoria = verificar(categoria)
    categoria = categoria.upper()
    continuar = True
    palabras = []
       
    while continuar:
        palabra = input("\nIngrese la palabra que desea agregar a la categoría.\nDeje vacío y presione Enter si quiere terminar: >>> ")
        if palabra == "":
            continuar = False
            break
        palabras.append(palabra.upper())
    
    categorias[categoria] = palabras
    print("\n¡¡La categoría de palabras se ha creado correctamente!!.")
    return categorias

def ver_categorias(categorias):
    if categorias == {}:
        print("\nNo existen categorias de palabras creadas.\n")
    elif len(categorias) == 1:
        print("\nExiste "+ str(len(categorias)) +" categoría de palabras:\n")
        for categoria in categorias:
            print("◙ {}: {}\n".format(categoria, categorias[categoria]))
    else:
        print("\nExisten "+ str(len(categorias)) +" categorías de palabras:\n")
        for categoria in categorias:
            print("◙ {}: {}\n".format(categoria, categorias[categoria]))

def eliminar_categoria():
    if categorias == {}:
        print("\nNo existen categorias de palabras creadas.\n")
    else:
        print("Las categorías de palabras existentes son:\n")
        for categoria in categorias:
            print("◙ {}\n".format(categoria))

    categoria_eliminar = input("Ingrese el nombre de la categoría a eliminar:\n>>> ")
    categoria_eliminar= verificar(categoria_eliminar)
    categoria_eliminar = categoria_eliminar.upper()
    del categorias[categoria_eliminar]
    print("\n¡¡La categoría de palabras se ha eliminado correctamente!!.")


def instrucciones():
    print(
        '''
        ◙Instrucciones◙
        El objetivo de este juego es descubrir una palabra adivinando las letras, 
        que la componen. Para ello:
        1. Debes seleccionar la categoría a la cual pertenece la palabra. 
        2. Inicias con  ''' + str(intentos) + " vidas ♥." + ''' 
        3. Ingresa una letra que creas se encuentre en la palabra a adivinar.
        4. Si la letra no se encuentra en la palabra, perderás una vida.
        5. Para ganar, debes adivinar la palabra antes de perder todas tus vidas. 
        ¡¡Suerte con el juego!!.
        '''
        )

def obtener_palabra(categorias):
    if categorias == {}:
        print("\nNo existen categorias de palabras creadas.")
    else:
        print("\nCategorías:")
        for categoria in categorias:
            print("◙ {}.\n".format(categoria))
        categoria_seleccionada = input("Ingresa el nombre de la categoría de palabras con la que quieres jugar: >>> ")
        categoria_seleccionada = verificar(categoria_seleccionada)
        categoria_seleccionada = categoria_seleccionada.upper()
        lista_palabras = categorias[categoria_seleccionada]
        palabra = random.choice(lista_palabras)
        return palabra


def jugar():
    palabra = obtener_palabra(categorias)
    letras_por_adivinar = set(palabra)
    letras_adivinadas = list()
    abecedario = list(string.ascii_uppercase)
    abecedario.append("Ñ")
    vidas = intentos  

    while len(letras_por_adivinar) > 0 and vidas > 0:

        palabra_del_jugador = []
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_del_jugador.append(letra)
            else:
                palabra_del_jugador.append('_')

        print("#"*90)
        if vidas == 1:
            print("\nTe queda {} vida\n".format(vidas))
        else:
            print("\nTe quedan {} vidas\n".format(vidas))
        print(vidas_graficos[vidas])

        if len(letras_adivinadas) != 0:
            letras_utilizadas = []
            for letra in letras_adivinadas:
                letras_utilizadas.append(letra)
            print("Has utilizado estas letras: {} ".format(' '.join(letras_utilizadas)))
            
        print("\nPalabra: {}\n".format(' '.join(palabra_del_jugador)))
        print("#"*90)
        letra_del_usuario = input("\nEscoge una letra: >>> ").upper()
        
        if letra_del_usuario in abecedario and letra_del_usuario not in letras_adivinadas:
            letras_adivinadas.append(letra_del_usuario)
            if letra_del_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_del_usuario)
                print('')
            else:
                vidas =  vidas - 1
                print("\nTu letra: ({}) no está en la palabra".format(letra_del_usuario))
        elif letra_del_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.\n")
        else:
            print("\nEsta letra no es válida.")

    if vidas == 0:
        print(vidas_graficos[vidas])
        print("¡Ahorcado! Perdiste. Lo sentimos mucho. La palabra era: {}. Intenta nuevamente.\n".format(palabra))
    else:
        print("¡¡Felicidades, adivinaste la palabra!!. Adivina una nueva palabra.\n")

def ajustes():
    contraseña = input("\nIngrese la contraseña para realizar ajustes al juego: >>> ")
    contraseña = verificar(contraseña)
    if contraseña != contraseña_ajustes:
        print("La contraseña es incorrecta\n")
        menu_principal()
    else: 
        while True:
            print("\n" + "♦"*50)
            print("♦ 1- Ver las categorías de palabras existentes →")
            print("♦ 2- Crear categoría de palabras ◘")
            #print("- Modificar categoría de palabras ‼")
            print("♦ 3- Eliminar categoría de palabras ×")
            print("♦ 4- Volver al menú principal ←")
            print("♦"*50+"\n")
            opcion = input("Ingrese el número de la acción que desea ejecutar: >>> ")
            opcion = verificar(opcion)
            if opcion == "1":
                ver_categorias(categorias)
            elif opcion == "2":
                crear_categoria_palabras()
            elif opcion == "3":
                eliminar_categoria()
            elif opcion == "4":
                menu_principal()
            else:
                print("La opción ingresada no es correcta, vuelva a intentarlo.")

def menu_principal():
    print("♦"*25)
    print("♦ 1- Jugar ►")
    print("♦ 2- Instrucciones ¶")
    print("♦ 3- Ajustes ☼")
    print("♦ 4- Salir ←")
    print("♦"*25+"\n")
    opcion = input("Ingrese el número de la acción que desea ejecutar: >>> ")
    opcion = verificar(opcion)
    if opcion == "1":
        jugar()
    elif opcion == "2":
        instrucciones()
    elif opcion == "3":
        ajustes()
    elif opcion == "4":
        print("\n"+"¡Gracias por jugar!. Esperamos que vuelvas pronto.")
        quit()
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")

def main():
    print("#"*90)
    print("#"*31+" ☺ ☻ Juego del Ahorcado ☻ ☺ "+"#"*31)
    print("#"*90)
    nombre_del_jugador = input("\nPor favor ingrese su nombre para comenzar el juego: >>> ")
    nombre_del_jugador = verificar(nombre_del_jugador)
    print("\n"+"░"*90)
    print(" Bienvenid@ "+ nombre_del_jugador)
    print("░"*90+"\n")
    while True:
        menu_principal()

main()   