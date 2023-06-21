import itertools
import os
import time

# Función para generar el diccionario y mostrar el progreso
def generar_diccionario(opcion, longitud):
    caracteres = ""

    # Definir los caracteres según la opción seleccionada
    if opcion == 1:
        caracteres = "abcdefghijklmnopqrstuvwxyz"
    elif opcion == 2:
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif opcion == 3:
        caracteres = "0123456789"
    elif opcion == 4:
        caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
    elif opcion == 5:
        caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
        simbolos = input("Ingresa los símbolos que deseas incluir: ")
        caracteres += simbolos
    elif opcion == 6:
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif opcion == 7:
        nombre = input("Ingrese el nombre: ")
        numeros1 = input("Ingrese el número inicial: ")
        numeros2 = input("Ingrese el número final: ")
        simbolos = input("Ingresa los símbolos que deseas incluir: ")
        combinaciones = [f"{nombre}{numero}{simbolo}" for numero in range(int(numeros1), int(numeros2) + 1) for simbolo in simbolos]
        total_combinaciones = len(combinaciones)
        progreso = 0

        with open("diccionario.txt", "w") as archivo:
            inicio = time.time()

            for combinacion in combinaciones:
                archivo.write(combinacion + "\n")

                progreso += 1
                porcentaje = (progreso / total_combinaciones) * 100
                carga = int(porcentaje / 2)
                barra = "[" + "<" * carga + "-" * (50 - carga) + "]"
                print(f"\rGenerando diccionario: {porcentaje:.2f}% {barra}", end="")

            tiempo_transcurrido = time.time() - inicio
            tiempo_estimado = tiempo_transcurrido * (total_combinaciones / progreso)
            print(f"\n\nTiempo estimado para ataque (basado en el diccionario generado): {tiempo_estimado:.2f} segundos")

        ruta_diccionario = os.path.abspath("diccionario.txt")
        print(f"\nDiccionario generado exitosamente en: {ruta_diccionario}")
        return

    elif opcion == 8:
        letras = input("Ingresa las letras que deseas incluir: ")
        numeros = input("Ingresa los números que deseas incluir: ")
        simbolos = input("Ingresa los símbolos que deseas incluir: ")
        caracteres = letras + numeros + simbolos

        # Generar todas las combinaciones de longitud deseada
        combinaciones = itertools.product(caracteres, repeat=longitud)
        total_combinaciones = len(caracteres) ** longitud
        progreso = 0

        # Crear el diccionario
        with open("diccionario.txt", "w") as archivo:
            inicio = time.time() # Tiempo de inicio

            for combinacion in combinaciones:
                clave = "".join(combinacion)
                archivo.write(clave + "\n")

                # Mostrar el progreso
                progreso += 1
                porcentaje = (progreso / total_combinaciones) * 100
                carga = int(porcentaje / 2)
                barra = "[" + "<" * carga + "-" * (50 - carga) + "]"
                print(f"\rGenerando diccionario: {porcentaje:.2f}% {barra}", end="")

            tiempo_transcurrido = time.time() - inicio
            tiempo_estimado = tiempo_transcurrido * (total_combinaciones / progreso)
            print(f"\n\nTiempo estimado para ataque (basado en el diccionario generado): {tiempo_estimado:.2f} segundos")

        # Mostrar la ruta del diccionario generado
        ruta_diccionario = os.path.abspath("diccionario.txt")
        print(f"\nDiccionario generado exitosamente en: {ruta_diccionario}")
        return

    elif opcion == 9:
        nombre = input("Ingrese el nombre: ")
        numeros1 = input("Ingrese el número inicial: ")
        numeros2 = input("Ingrese el número final: ")
        simbolos = input("Ingresa los símbolos que deseas incluir: ")
        combinaciones = [f"{nombre[:i].lower()}{nombre[i].upper()}{nombre[i+1:].lower()}{numero}{simbolo}"
                         for i in range(len(nombre)) for numero in range(int(numeros1), int(numeros2) + 1) for simbolo in simbolos]
        total_combinaciones = len(combinaciones)
        progreso = 0

        with open("diccionario.txt", "w") as archivo:
            inicio = time.time()

            for combinacion in combinaciones:
                archivo.write(combinacion + "\n")

                progreso += 1
                porcentaje = (progreso / total_combinaciones) * 100
                carga = int(porcentaje / 2)
                barra = "[" + "<" * carga + "-" * (50 - carga) + "]"
                print(f"\rGenerando diccionario: {porcentaje:.2f}% {barra}", end="")

            tiempo_transcurrido = time.time() - inicio
            tiempo_estimado = tiempo_transcurrido * (total_combinaciones / progreso)
            print(f"\n\nTiempo estimado para ataque (basado en el diccionario generado): {tiempo_estimado:.2f} segundos")

        ruta_diccionario = os.path.abspath("diccionario.txt")
        print(f"\nDiccionario generado exitosamente en: {ruta_diccionario}")
        return

    else:
        print("Opción inválida")
        return

    # Generar todas las combinaciones de longitud deseada
    combinaciones = itertools.product(caracteres, repeat=longitud)
    total_combinaciones = len(caracteres) ** longitud
    progreso = 0

    # Crear el diccionario
    with open("diccionario.txt", "w") as archivo:
        inicio = time.time() # Tiempo de inicio

        for combinacion in combinaciones:
            clave = "".join(combinacion)
            archivo.write(clave + "\n")

            # Mostrar el progreso
            progreso += 1
            porcentaje = (progreso / total_combinaciones) * 100
            carga = int(porcentaje / 2)
            barra = "[" + "<" * carga + "-" * (50 - carga) + "]"
            print(f"\rGenerando diccionario: {porcentaje:.2f}% {barra}", end="")

        tiempo_transcurrido = time.time() - inicio
        tiempo_estimado = tiempo_transcurrido * (total_combinaciones / progreso)
        print(f"\n\nTiempo estimado para ataque (basado en el diccionario generado): {tiempo_estimado:.2f} segundos")

    # Mostrar la ruta del diccionario generado
    ruta_diccionario = os.path.abspath("diccionario.txt")
    print(f"\nDiccionario generado exitosamente en: {ruta_diccionario}")


# Función principal
def main():
    print(r"""
 _______  _______  _______  _______  _______  _______  _______  _______  _______ 
(  ____ \(  ___  )(       )(  ____ \(  ____ )(  ____ )(  ____ \(  ____ \(  ____ \
| (    \/| (   ) || () () || (    \/| (    )|| (    )|| (    \/| (    \/| (    \/
| (_____ | |   | || || || || (_____ | (____)|| (____)|| (__    | (____  | (_____ 
(_____  )| |   | || |(_)| |(_____  )(_____ )|  _____)|  __)   (_____ \ (_____  )
      ) || |   | || |   | |      ) |      ) || (      | (            ) )      ) |
/\____) || (___) || )   ( |/\____) |/\____) || )      | (____/\/\____) )/\____) |
\_______)(_______)|/     \|\_______)\_______)|/       (_______/\______/ \_______)
                                                                                
""")
    print("By Anonimo501\n")

    print("Opciones:")
    print("1) Minúsculas a-z")
    print("2) Mayúsculas A-Z")
    print("3) Numérico 0-9")
    print("4) Minúsculas a-z con números 0-9")
    print("5) Minúsculas a-z con números 0-9 y símbolos")
    print("6) Minúsculas a-z y mayúsculas A-Z con números 0-9")
    print("7) Personalizado (nombre2020#)")
    print("8) Ultra personalizado (todos los caracteres)")
    print("9) Personalizado (NomBrE2020#)")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 7 or opcion == 9:
        generar_diccionario(opcion, 0)
    else:
        longitud = int(input("Ingresa la longitud de las contraseñas a generar: "))
        generar_diccionario(opcion, longitud)


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
