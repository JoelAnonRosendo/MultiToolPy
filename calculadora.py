#!/usr/bin/python
# -*- coding: utf -8 -*-

#

author = "Joel Añón"

import os
import json
from datetime import datetime

FECHA_ACTUAL = datetime.now()
FORMATO = FECHA_ACTUAL.strftime("%Y-%m-%d-%H-%M")

def clear():
    input("Presione enter para continuar.")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("-----------------------------------------------------------------------")
    print("\t1.-  Calculadora")
    print("\t2.-  Generador de Números Primos")
    print("\t3.-  Generador de correos")
    print("\t4.-  Generador de contraseñas de seguridad")
    print("\t5.-  ")
    print("\t6.-  ")
    print("\t7.-  ")
    print("\t8.-  ")
    print("\t9.-  ")
    print("\t10.- ")
    print("\t0.-  Adios.")
    print("\thelp or -h  .- Muestra un listado de ayuda")
    print("-----------------------------------------------------------------------")

def selecion_menu():
    respuesta = input("Que opcion escoges? ")
    return respuesta

def mostrar_opcion(res):
    respuesta = res
    if respuesta == "1":
        calculadora()
    elif respuesta == "2":
        numeros_primos()
    elif respuesta == "3":
        generador_de_correos()

def calculadora():

    # Inicio Calculadora
    def menu_calculadora():
        print("-----------------------------------------------------------------------")
        print("\t1.-  Insertar valores")
        print("\t2.-  Operacion con todos valores")
        print("\t3.-  Operacion con solo la cantidad de valores especificados")
        print("\t4.-  Mostrar valores")
        print("\t5.-  Mostrar historial")
        print("\t6.-  Eliminar historial")
        print("\t7.-  Eliminar valores")
        print("\t8.-  Copia de seguridad")
        print("\t9.-  Restauracion de copia de seguridad")
        print("\t10.- Eliminar copias de seguridad")
        print("\t0.-  Adios.")
        print("\thelp or -h  .- Muestra un listado de ayuda")
        print("-----------------------------------------------------------------------")


    # Aqui el codigo le pregunta al usuario que opcion desea y el usuario le responde

    def seleccionar_opcion_calculadora():
        respuesta = input("Que opcion escoges? ")
        return respuesta

    # Aqui el codigo determina a partir de la opcion del usuario que camino elige

    def mostrar_opcion_calculadora(respuesta, lista, history, numero_h, cifra):
        res = respuesta
        if res == "1":
            lista = insertar_variables(lista)
        elif res == "2":
            lista, history, numero_h = operacion_todo(lista, history, numero_h)
        elif res == "3":
            cifra = preguntar_cantidad_operacion(cifra, lista)
            lista, history, numero_h = operacion_de_cifra(lista,history,numero_h,cifra)
        elif res == "4":
            mostrar_variables(lista)
        elif res == "5":
            mostrar_historial_calculadora(history)
        elif res == "6":
            history = eliminar_historial_calculadora(history)
        elif res == "7":
            lista = eliminar_valores(lista)
        elif res == "8":
            copia_seguridad_calculadora(lista,history)
        elif res == "9":
            lista, history = restauracion_calculadora(lista,history)
        elif res == "help" or res == "-h":
            descripcion_help_calculadora()

        return lista, history, numero_h


    def insertar_variables(list):
        lista = list[:]
        valores = input("Que valores quieres añadir? ")
        lista.append(int(valores))
        return lista 


    def operacion_todo(list, historial, numero_historial):
        lista = []
        lista = list[:]
        history = historial
        total = 0
        operacion = None
        operacion = preguntar_operacion()
        if operacion == "*":
            total = 1
        for x in lista:
            if operacion == "+":
                total = total + x
            elif operacion == "-":
                total = total - x
            elif operacion == "*":
                total = total * x
            elif operacion == "/":
                total = total / x
            clear()

        numero_historial = numero_historial + 1
        history[f" Historial_{numero_historial}"] = f"{lista} = {total}"

        for index in range(len(lista)):
            lista.pop()

        print(f"El resultado de la suma es: {total}")

        lista.append(int(total))
        return lista, history, numero_historial


    def operacion_de_cifra(list, historial, numero_historial, cantidad):
        lista = []
        lista = list[:]
        history = historial
        total = 0
        cifra = int(cantidad)
        segunda_lista = []
        numero_historial = numero_historial + 1
        for i in range(cifra):
            segunda_lista.append(lista[i])
            print(f"{total} ? {lista[i]}")
            operacion = preguntar_operacion()
            if operacion == "+":
                total = total + lista[i]
            elif operacion == "-":
                total = total - lista[i]
            elif operacion == "*":
                total = total * lista[i]
            elif operacion == "/":
                total = total / lista[i]
            clear()
        print(total)
        
        history[f" Historial_{numero_historial}"] = f"{segunda_lista} = {total}"
        
        for x in segunda_lista:
            if x in lista:
                lista.remove(x)
        print(f"El resultado de la suma de {cifra} numeros que es es: {segunda_lista} = {total}")
        
        return lista, history, numero_historial

    """
        def suma():

        def resta():

        def multiplicar():

        def division():
    """

    def preguntar_operacion():
        print("Que operacion quieres hacer de estas opciones: + - * / % ** ")
        respuesta = input()
        return respuesta


    def preguntar_cantidad_operacion(cantidad, list):
        cifra = cantidad
        lista = list[:]
        caracteres_lista = int(len(lista))
        cifra = int(input("Cuantas cantidades de operaciones quieres hacer? "))
        while cifra > caracteres_lista or cifra == 0:
            cifra = int(input(f"La cantidad seleccionada es major o menor a la que se puede solo puedes del 1 hasta el {len(lista)} "))
        return cifra


    def mostrar_variables(list):
        print(list)

    # Modificar
    def mostrar_historial_calculadora(historial):
        print(f"----------------------------------------------------")
        for clave, valor in historial.items():
            valor_str = valor.replace(","," +").replace("[","").replace("]","")
            print(f"{clave}\n ________________\n  {valor_str}")
            print()
        print(f"----------------------------------------------------")


    def descripcion_help_calculadora():
        clear()
        print()
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("|                                 Guia de ayuda                               |")
        print("|_____________________________________________________________________________|")
        print("|                                                                             |")
        print("|   help  or  -h   -->    Muestra una guia de ayuda para el usuario           |")
        print("|                         facilitando el uso del programa.                    |")
        print("|                                                                             |")
        print("|   1.Insertar     -->    Se le pide al usuario que ponga un numero           |")
        print("|     valores             cualquiera para guardarlo y poder operar            |")
        print("|                         con ellos.                                          |")
        print("|                                                                             |")
        print("|   2.Operacion    -->    Al preguntar al usuario que tipo de                 |")
        print("|     con todos           operacion quiere ralizar escoje todos los           |")
        print("|     los valores         valores insertados y realiza la operacion           |")
        print("|                         seleccionada con todos.                             |")
        print("|                                                                             |")
        print("|   3.Especificar  -->    Pregunta al usuario que cantidad de valores         |")
        print("|     cantidad de         que quiere utilizar de los valores insertados       |")
        print("|     valores             para luego ir preguntando que tipo de operacion     |")
        print("|                         quiere hacer en los diferentes valores              |")
        print("|                         escoguidos previamente.                             |")
        print("|                                                                             |")
        print("|   4.Mostrar      -->    Muestra todos los valores que ha añadido el         |")
        print("|     valores             usuario para facilitar la decision de operaciones   |")
        print("|                         que desee hacer.                                    |")
        print("|                                                                             |")
        print("|   5.Mostrar      -->    Muestra un historial de todas las operaciones       |")
        print("|     historial           realizadas por el usuario.                          |")
        print("|                                                                             |")
        print("|   6.Eliminar     -->    Elimina el historial entero                         |")
        print("|     historial                                                               |")
        print("|                                                                             |")
        print("|   7.Eliminar     -->    Elimina todos los valores inertado por el           |")
        print("|     valores             usuario.                                            |")
        print("|                                                                             |")
        print("|   8.Copia de     -->    El usuario tiene que eleguir si hacer una           |")
        print("|     seguridad           copia de el historial, de los valores o de          |")
        print("|                         ambas.                                              |")
        print("|                                                                             |")
        print("|   9.Restauracion -->    El usuario tiene que eleguir si hacer una           |")
        print("|     de copia de         restauracion completa o especifica, si elige        |")
        print("|     seguridad           la especifica tendra que eleguir entra restaurar    |")
        print("|                         el historial o los valores.                         |")
        print("|_____________________________________________________________________________|")
        print()
        clear()


    def eliminar_historial_calculadora(historial):
        history = historial
        history.clear()
        return history


    def eliminar_valores(list):
        lista = list[:]
        lista.clear()
        return lista


    def copia_seguridad_calculadora(list, history):
        lista = list[:]
        historial = history
        ruta = None
        print("De que deseas hacer copia:")
        print("\t1.- Completa (tanto el historial como los valores)")
        print("\t2.- Solo historial")
        print("\t3.- Solo los valores")
        respuesta = input()
        if respuesta == "1":

            ruta = os.path.join("C:/Users/J.anon/Downloads/python/copias/calculadora/completas",f"completa-{FORMATO}.txt")
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            
            with open(ruta, "w") as archivo:
                json.dump({"historial": historial, "lista": lista}, archivo)
        elif respuesta == "2":
            ruta = os.path.join("C:/Users/J.anon/Downloads/python/copias/calculadora/historial",f"historial-{FORMATO}.txt")
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open (ruta, "w") as archivo:
                json.dump(historial, archivo, indent=4)
        elif respuesta == "3":
            ruta = os.path.join("C:/Users/J.anon/Downloads/python/copias/calculadora/valores",f"valores-{FORMATO}.txt")
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open (ruta, "w") as archivo:
                json.dump(lista, archivo)
        print("La copia de seguridad se ha realizado con exito.")


    def restauracion_calculadora(list, history):
        lista = list[:]
        historial = history
        posicion = 1
        contador = 0
        contenido_restaurar = None
        print("De que deseas hacer la restauracion:")
        print("\t1.- Completa (tanto el historial como los valores)")
        print("\t2.- Solo historial")
        print("\t3.- Solo los valores")
        respuesta = input()
        if respuesta == "1":
            ruta = "C:/Users/J.anon/Downloads/python/copias/calculadora/completas"
            contenido = os.listdir(ruta)
            for elemento in contenido:
                print(f"\n|   {posicion}.- {elemento} \t\t\t |")
                posicion = posicion + 1
            respuesta = int(input("Cual quieres restaurar: "))
            for x in contenido:
                contador += 1  
                if contador == respuesta:  
                    contenido_restaurar = x 
            ruta = f"C:/Users/J.anon/Downloads/python/copias/calculadora/completas/{contenido_restaurar}"
            with open(ruta, "r") as archivo:
                datos_restaurados = json.load(archivo)
            historial = datos_restaurados["historial"]
            lista = datos_restaurados["lista"]

        elif respuesta == "2":

            ruta = "C:/Users/J.anon/Downloads/python/copias/calculadora/historial"
            contenido = os.listdir(ruta)
            for elemento in contenido:
                print(f"\n|   {posicion}.- {elemento} \t\t\t |")
                posicion = posicion + 1
            respuesta = int(input("Cual quieres restaurar: "))
            for x in contenido:
                contador += 1  
                if contador == respuesta:  
                    contenido_restaurar = x 
            ruta = f"C:/Users/J.anon/Downloads/python/copias/calculadora/historial/{contenido_restaurar}"

            with open (ruta, "r") as archivo:
                historial = json.load(archivo)
        elif respuesta == "3":

            ruta = "C:/Users/J.anon/Downloads/python/copias/calculadora/valores"
            contenido = os.listdir(ruta)
            for elemento in contenido:
                print(f"\n|   {posicion}.- {elemento} \t\t\t |")
                posicion = posicion + 1
            respuesta = int(input("Cual quieres restaurar: "))
            for x in contenido:
                contador += 1  
                if contador == respuesta:  
                    contenido_restaurar = x 
            ruta = f"C:/Users/J.anon/Downloads/python/copias/calculadora/valores/{contenido_restaurar}"

            with open (ruta, "r") as archivo:
                lista = json.load(archivo)
        print("La copia de seguridad se ha realizado con exito.")
        return lista, historial
    # Fin calculadora

    respuesta_menu_calculadora = None
    lista_variables = []
    historial = {}
    cantidad = 0
    numero_historial = 0
    while respuesta_menu_calculadora != "0":
        clear()
        menu_calculadora()
        respuesta_menu_calculadora = seleccionar_opcion_calculadora()
        if respuesta_menu_calculadora != "0": 
            lista_variables, historial, numero_historial = mostrar_opcion_calculadora(respuesta_menu_calculadora, lista_variables,historial,numero_historial, cantidad)
    print("Adios")

# Falta por acabar
def numeros_primos():

    def menu_numeros_primos():
        print("-----------------------------------------------------------------------")
    print("\t1.-  Cantidad de numeros primos a imprimir")
    print("\t2.-  ")
    print("\t3.-  ")
    print("\t4.-  ")
    print("\t5.-  ")
    print("\t6.-  ")
    print("\t7.-  ")
    print("\t8.-  ")
    print("\t9.-  ")
    print("\t10.- ")
    print("\t0.-  Adios.")
    print("\thelp or -h  .- Muestra un listado de ayuda")
    print("-----------------------------------------------------------------------")

    def preguntar_opcion_menu_primos(opcion):
        respuesta = opcion
        respuesta = input("Que opcion escoges? ")
        return respuesta



    def preguntar_cantidad(cantidad):
        respuesta = cantidad
        respuesta = int(input("Cuantos numeros primos quieres que te muestre: "))

        return respuesta

    def encontrar_numeros_primos(cantidad):
        cantidad_primos = cantidad

        def es_primo(cantidad_primos):
            if cantidad_primos < 2:
                return False
            for i in range(2, int(cantidad_primos ** 0.5) + 1):
                if cantidad_primos % i == 0:
                    return False
            return True
        primos = []
        for num in range(cantidad_primos + 1):
            if es_primo(num):
                primos.append(num)
        print(primos)

    cantidad_de_numeros_primos = None
    opcion_menu_numeros_primos = None
    while opcion_menu_numeros_primos != "0":
        menu_numeros_primos()
        opcion_menu_numeros_primos = preguntar_opcion_menu_primos(opcion_menu_numeros_primos)
        cantidad_de_numeros_primos = preguntar_cantidad(cantidad_de_numeros_primos)

        while cantidad_de_numeros_primos == 0:
            print("La cantidad deseada tiene que ser superior a 0.")
            cantidad_de_numeros_primos = preguntar_cantidad(cantidad_de_numeros_primos)
        encontrar_numeros_primos(cantidad_de_numeros_primos)

def generador_de_correos():
    def menu_generador_de_correos():

        print("-----------------------------------------------------------------------")
        print("\t1.-  Crear correo")
        print("\t2.-  Cambiar dominio del correo")
        print("\t3.-  Historial de correos creados")
        print("\t4.-  Eliminar correo")
        print("\t5.-  Crear copia de seguridad")
        print("\t6.-  Restauracion de copias de seguridad")
        print("\t0.-  Adios.")
        print("\thelp or -h  .- Muestra un listado de ayuda")
        print("-----------------------------------------------------------------------")

    def preguntar_opcion_menu_correos():
        respuesta = input("Que opcion escoges? ")
        return respuesta
    
    def mostrar_opcion_correos(respuesta_opcion, nombre_dominio, nombre_usuario, historial, contador_historial):
        respuesta = respuesta_opcion
        dominio = nombre_dominio
        nombre = nombre_usuario
        history = historial
        contador_history = contador_historial

        if respuesta == "1":
            history, contador_history = crear_correo(dominio, nombre, history, contador_history)
        elif respuesta == "2":
            dominio = cambiar_dominio(dominio)
        elif respuesta == "3":
            mostrar_historial_correos(history)
        elif respuesta == "4":
            history = eliminar_correos(history)
        elif respuesta == "5":
            copia_de_seguridad_correos(history)
        elif respuesta == "6":
            history = restauracion_copias_correos(history)
        return dominio, history, contador_history
    
    def crear_correo(nombre_dominio, nombre_usuario, historial, contador_historial):
        dominio = nombre_dominio
        nombre = nombre_usuario
        history = historial
        apellido = None
        correo = None
        primera_letra_nombre = None
        acentos = "áéíóúÁÉÍÓÚ"
        contador_letra = 0
        localizador_accentos = False
        contador_history = contador_historial

        nombre = input("Cual es tu nombre: ")
        apellido = input("Cual es tu apellido: ")
        apellido = apellido.replace('ñ','n')
        for x in apellido:
            if x in acentos:
                localizador_accentos = True
        while localizador_accentos == True:
            print("Los accentos no son validos, porfavor ingrese uno sin accentos.")
            apellido = input("Cual es tu apellido: ")
            for x in apellido:
                if x in acentos:
                    localizador_accentos = True
                    break
                else:
                    localizador_accentos = False
        apellido = apellido.replace('ñ','n')
        nombre = nombre.lower()
        apellido = apellido.lower()
        for i in nombre:
            if contador_letra == 0:
                contador_letra += 1
                primera_letra_nombre = i 
        correo = f"{primera_letra_nombre}.{apellido}@{dominio}"
        print(f"Se ha creado el correo {correo}.")
        contador_history += 1
        history[contador_history] = correo
    
        return history, contador_history

    def cambiar_dominio(nombre_dominio):
        dominio = nombre_dominio
        respuesta = None
        print(f"Tu dominio ahora es {dominio}, quieres cambiarlo? si o no ")
        respuesta = input()
        respuesta = respuesta.lower()
        if respuesta == "si":
            dominio = input("Por cual lo quieres cambiar? ")
            print(f"Se a cambiado el dominio de {nombre_dominio} a {dominio}.")
        else:
            return dominio
        return dominio

    def mostrar_historial_correos(historial):
        history = historial
        print(f"----------------------------------------------------")
        for clave, valor in history.items():
            valor_str = valor.replace("[","").replace("]","")
            print(f"{clave}\n\n{valor_str}")
            print()
        print(f"----------------------------------------------------")

    # falta refinar
    def eliminar_correos(historial):
        history = historial
        respuesta = None
        correo_eliminar = None
        print(f"----------------------------------------------------")
        for clave, valor in history.items():
            valor_str = valor.replace("[","").replace("]","")
            print(f"{clave}\n\n{valor_str}")
            print()
        print(f"----------------------------------------------------")
        respuesta = input("Deseas eliminar todos? si o no ")
        if respuesta == "si":
            history = {}
        elif respuesta == "no":
            correo_eliminar = int(input("Cual deseas eliminar: "))
            valores = list(history.values())
            correo_eliminado = valores[correo_eliminar -1]
            del history[correo_eliminar]
            print(f"Se ha eliminado el correo {correo_eliminado}.")
        return history

    def copia_de_seguridad_correos(historial):
        history = historial

    def restauracion_copias_correos(historial):
        history = historial
        return history
    
    respuesta_menu = None
    nombre = None
    history = {}
    contador_history = 0

    dominio = input("Que dominio quieres usar como por ejemplo \"gmail.com\": ")
    if dominio == "":
        dominio = "gmail.com"
    while respuesta_menu != "0":
        clear()
        menu_generador_de_correos()
        respuesta_menu = preguntar_opcion_menu_correos()
        dominio, history, contador_history = mostrar_opcion_correos(respuesta_menu, dominio, nombre, history, contador_history)

def main():
    
    respuesta_menu = None
    while respuesta_menu != "0":
        clear()
        menu()
        respuesta_menu = selecion_menu()
        if respuesta_menu != "0":
            mostrar_opcion(respuesta_menu)
    print("Adios")

if __name__ == "__main__":
    main()