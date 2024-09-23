#!/usr/bin/python
# -*- coding: utf -8 -*-


author = "Joel Añón"


import os
import json
from datetime import datetime
import random
import string
import requests # type: ignore


FECHA_ACTUAL = datetime.now()
FORMATO = FECHA_ACTUAL.strftime("%Y-%m-%d-%H-%M")
API_KEY = '03461bb35e9c5fccbb7f7db5'


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
    print("\t5.-  Conversiones")
    print("\t6.-  Save keys")
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
    elif respuesta == "4":
        generador_de_contraseñas()
    elif respuesta == "5":
        conversiones()


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
        elif respuesta == "-h" or respuesta == "help":
            help_correos()
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
        ruta = None
        ruta = os.path.join("C:/Users/J.anon/Downloads/python/copias/correos/historial",f"historial-{FORMATO}.txt")
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open (ruta, "w") as archivo:
            json.dump(history, archivo, indent=4)
        print("La copia de seguridad se ha realizado con exito.")


    def restauracion_copias_correos(historial):
        history = historial
        posicion = 1
        contador = 0
        contenido_restaurar = None
        ruta = "C:/Users/J.anon/Downloads/python/copias/correos/historial"
        contenido = os.listdir(ruta)
        for elemento in contenido:
            print(f"\n|   {posicion}.- {elemento} \t\t\t |")
            posicion = posicion + 1
        respuesta = int(input("Cual quieres restaurar: "))
        for x in contenido:
            contador += 1  
            if contador == respuesta:  
                contenido_restaurar = x 
        ruta = f"C:/Users/J.anon/Downloads/python/copias/correos/historial/{contenido_restaurar}"

        with open (ruta, "r") as archivo:
            history = json.load(archivo)
        return history
    

    def help_correos():
        clear()
        print()
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("|                                 Guia de ayuda                               |")
        print("|_____________________________________________________________________________|")
        print("|                                                                             |")
        print("|   help  or  -h   -->    Muestra una guia de ayuda para el usuario           |")
        print("|                         facilitando el uso del programa.                    |")
        print("|                                                                             |")
        print("|   1.Crear        -->    Crea correos a partir de la primera letra           |")
        print("|     correos             del nombre a continuacion un \".\" y luego          |")
        print("|                         el aellido @ el dominio.                            |")
        print("|                                                                             |")
        print("|   2.Cambiar      -->    Le pregunta al usuario por que dominio quiere       |")
        print("|     el dominio          cambiarlo como por ejemplo gmail.com.               |")
        print("|                                                                             |")
        print("|   3.Mostrar      -->    Muestra un historial de todos los correos           |")
        print("|     historial           creados por el usuario.                             |")
        print("|                                                                             |")
        print("|   4.Eliminar     -->    Muestra al usuario todos los correos creados        |")
        print("|     correos             enumerados para que el usuario decida cual          |")
        print("|                         quiere eliminar, pero tambien tiene una opcion      |")
        print("|                         de eliminarlo todo de una sentada.                  |")
        print("|                                                                             |")
        print("|   5.Copias       -->    Crea una copia de seguridad de todos los            |")
        print("|     de seguridad        correos creados por el usuario.                     |")
        print("|                                                                             |")
        print("|   6.Restauracion -->    Se le muestra al usuario todas las copias de        |")
        print("|                         seguridad para que eliga cual quiere restaurar.     |")
        print("|_____________________________________________________________________________|")
        print()
        clear()


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


def generador_de_contraseñas():
    # Inicio contraseñas
    def menu_contraseñas():
        print("-----------------------------------------------------------------------")
        print("\t1.-  Generar contraseña automaticamente.")
        print("\t2.-  Generar contraseña definiendo la cantidad de caracteres.")
        print("\t0.-  Adios.")
        print("\thelp or -h  .- Muestra un listado de ayuda")
        print("-----------------------------------------------------------------------")


    def preguntar_opcion_menu_contraseñas():
        respuesta = None
        respuesta = input("Que opcion escoges? ")
        return respuesta


    def mostrar_opcion_menu_contraseñas(respuesta):
        respuesta_menu =respuesta

        if respuesta_menu == "1":
            contraseña_automatica()
        elif respuesta_menu == "2":
            contraseña_definir()
        elif respuesta_menu == "-h" or respuesta_menu == "help":
            help_contraseñas()


    def contraseña_automatica():
        caracteres = 10
        combinacion = string.ascii_letters + string.digits
        contraseña = ''.join(random.choice(combinacion) for _ in range(caracteres))
        print(contraseña)


    def contraseña_definir():
        caracteres = None
        combinacion = string.ascii_letters + string.digits
        caracteres = int(input("De cuantos caracteres quieres que sea la contraseña: "))
        contraseña = ''.join(random.choice(combinacion) for _ in range(caracteres))
        print(contraseña)

    # Falta acabar
    def help_contraseñas():
        clear()
        print()
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("|                                 Guia de ayuda                               |")
        print("|_____________________________________________________________________________|")
        print("|                                                                             |")
        print("|   help  or  -h   -->    Muestra una guia de ayuda para el usuario           |")
        print("|                         facilitando el uso del programa.                    |")
        print("|                                                                             |")
        print("|   1.Generar      -->    Genera automaticamente una contraseña de            |")
        print("|     contraseñas         10 caracteres.                                      |")
        print("|     automaticas                                                             |")
        print("|                                                                             |")
        print("|   2.Generar      -->    Genera automaticamente una contraseña de            |")
        print("|     contraseñas         la cantidad de caracteres especificados             |")
        print("|     caracteres          por el usuario.                                     |")
        print("|_____________________________________________________________________________|")
        print()
        clear()


    respuesta_menu = None
    while respuesta_menu != "0":
        clear()
        menu_contraseñas()
        respuesta_menu = preguntar_opcion_menu_contraseñas()
        mostrar_opcion_menu_contraseñas(respuesta_menu)
    # Fin contraseñas


def conversiones():
    # Inicio conversiones
    def menu_conversiones():
        print("-----------------------------------------------------------------------")
        print("\t1.-  Combersion.")
        print("\t2.-  Mostrar historial.")
        print("\t3.-  Copias de seguridad.")
        print("\t4.-  Restauracion.")
        print("\t0.-  Adios.")
        print("\thelp or -h  .- Muestra un listado de ayuda")
        print("-----------------------------------------------------------------------")
    

    def preguntar_opcion_menu_conversiones():
        respuesta = None
        respuesta = input("Que opcion escoges? ")
        return respuesta
    

    def mostrar_opcion_menu_conversiones(respuesta, historial, numero_historial):
        respuesta_menu =respuesta
        numero_history = numero_historial
        history = historial
        if respuesta_menu == "1":
            history, numero_history = hacer_conversiones(history, numero_history)
        elif respuesta_menu == "2":
            mostrar_historial(history)
        elif respuesta_menu == "3":
            copia_de_seguridad_conversiones(history, numero_history)
        elif respuesta_menu == "4":
            history, numero_history = restauracion_conversiones(history, numero_history)
        return history, numero_history


    def hacer_conversiones(historial, numero_historial):
        respuesta = None
        respuesta_comvertir = None
        history = historial
        numero_history =numero_historial
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
        def mini_menu_conversiones():
            print("-----------------------------------------------------------------------")
            print("\t1.-  Longitud")
            print("\t2.-  Peso")
            print("\t3.-  Temperatura")
            print("\t4.-  Moneda")
            print("-----------------------------------------------------------------------")
        mini_menu_conversiones()
        respuesta = int(input("Que opcion: "))

        if respuesta == 1:
            print("-----------------------------------------------------------------------")
            print("\t1.-  Comvertir de metros a kilometros.")
            print("\t2.-  Comvertir de kilometros a metros.")
            print("-----------------------------------------------------------------------")
            respuesta_comvertir = int(input(""))
            if respuesta_comvertir == 1:
                metros = float(input("Dime los metros que quieres pasar a kilometros: "))
                kilometros = metros / 1000
                print(f"los {metros} metros son {kilometros} kilometros.")
                numero_history += 1
                history[f"Histrorial numero {numero_history}"] = f"{metros}m = {kilometros}km"
                print(f"{metros}m = {kilometros}km")
            elif respuesta_comvertir == 2:
                kilometros = float(input("Dime los kilometros que quieres pasar a metros: "))
                metros = kilometros * 1000
                print(f"los {kilometros} kilometros son {metros} metros.")
                numero_history += 1
                history[f"Histrorial numero {numero_history}"] = f"{kilometros}km = {metros}m"
                print(f"{kilometros}km = {metros}m")
        elif respuesta ==2:
            print("-----------------------------------------------------------------------")
            print("\t1.-  Comvertir de gramos a kilogramos.")
            print("\t2.-  Comvertir de kilogramos a gramos.")
            print("-----------------------------------------------------------------------")
            respuesta_comvertir = int(input(""))
            if respuesta_comvertir == 1:
                gramos = float(input("Cuantos gramos quieres pasar a kilogramos? "))
                kilogramos = gramos / 1000
                print(f"los {gramos} gramos son {kilogramos} kilogramos.")
                numero_history += 1
                history[f"Histrorial numero {numero_history}"] = f"{gramos}g = {kilogramos}kg"
                print(f"{gramos}g = {kilogramos}kg")
            elif respuesta_comvertir == 2:
                kilogramos = float(input("Cuantos kilogramos quieres pasar a gramos? "))
                gramos = kilogramos * 1000
                print(f"los {kilogramos} kilogramos son {gramos} gramos.")
                numero_history += 1
                history[f"Histrorial numero {numero_history}"] = f"{kilogramos}kg = {gramos}g"
                print(f"{kilogramos}kg = {gramos}g")
        elif respuesta == 3:
            print("-----------------------------------------------------------------------")
            print("\t1.-  Comvertir de Celsius a Fahrenheit.")
            print("\t2.-  Comvertir de Fahrenheit a Celsius.")
            print("-----------------------------------------------------------------------")
            respuesta_comvertir = int(input(""))
            if respuesta_comvertir == 1:
                celsius = float(input("Dime los celsius que quieres pasar a fahrenheit: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"los {celsius} celsius son {fahrenheit} fahrenheit.")
                numero_history += 1
                history[f"Histrorial numero {numero_history}"] = f"{celsius}°C = {fahrenheit}°F"
                print(f"{celsius}°C = {fahrenheit}°F")
            elif respuesta_comvertir == 2:
                fahrenheit = float(input(""))
                celsius = (fahrenheit - 32) * 5/9
                print(f"los {celsius} celsius son {fahrenheit} fahrenheit.")
                numero_history += 1
                history[f"Histrorial numero {numero_history}"] = f"{celsius}°C = {fahrenheit}°F"
                print(f"{celsius}°C = {fahrenheit}°F")
        elif respuesta == 4:
            print("-----------------------------------------------------------------------")
            print("\t1.-  Comvertir de Euro € a Dolar $.")
            print("\t2.-  Comvertir de Dolar $ a Euro €.")
            print("-----------------------------------------------------------------------")
            respuesta_comvertir = int(input(""))
            if respuesta_comvertir == 1:
                url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
                response = requests.get(url)
                data = response.json()
                tasa_cambio = data['conversion_rates']['USD']
                euro = float(input("Cuantos euros quieres pasar a dolares? "))
                print(f"La tasa de cambio de € a DOLAR = {tasa_cambio}")
                dolares = euro * tasa_cambio
                history[f"Histrorial numero {numero_history}"] = f"{euro}€ = {dolares}$"
                print(f"{euro}€ = {dolares}$")
            elif respuesta_comvertir == 2:
                url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
                response = requests.get(url)
                data = response.json()
                tasa_cambio = data['conversion_rates']['EUR']
                dolares = float(input("Cuantos euros quieres pasar a dolares? "))
                print(f"La tasa de cambio de $ a EURO = {tasa_cambio}")
                euro = dolares * tasa_cambio
                history[f"Histrorial numero {numero_history}"] = f"{dolares}$ = {euro}€"
                print(f"{dolares}$ = {euro}€")
        
        return history, numero_history


    def mostrar_historial(historial):
        history = historial
        print(f"----------------------------------------------------")
        for clave, valor in history.items():
            valor_str = valor.replace(","," +").replace("[","").replace("]","")
            print(f"{clave}\n ________________\n\n  {valor_str}")
            print()
        print(f"----------------------------------------------------")


    def copia_de_seguridad_conversiones(historial, numero_historial):
        history = historial
        numero_history = numero_historial
        ruta = None

        ruta = os.path.join("C:/Users/J.anon/Downloads/python/copias/conversiones/completas",f"completa-{FORMATO}.txt")
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
        with open(ruta, "w") as archivo:
            json.dump({"historial": history, "numero_historial": numero_history}, archivo)


    def restauracion_conversiones(historial, numero_historial):
        history = historial
        numero_history = numero_historial
        posicion = 1
        contador = 0
        contenido_restaurar = None
        ruta = "C:/Users/J.anon/Downloads/python/copias/conversiones/completas"
        contenido = os.listdir(ruta)
        for elemento in contenido:
            print(f"\n|   {posicion}.- {elemento} \t\t\t |")
            posicion = posicion + 1
        respuesta = int(input("Cual quieres restaurar: "))
        for x in contenido:
            contador += 1  
            if contador == respuesta:  
                contenido_restaurar = x 
        ruta = f"C:/Users/J.anon/Downloads/python/copias/conversiones/completas/{contenido_restaurar}"
        with open(ruta, "r") as archivo:
            datos_restaurados = json.load(archivo)
        history = datos_restaurados["historial"]
        numero_history = datos_restaurados["numero_historial"]
        return history, numero_history


    respuesta_menu = None
    history = {}
    numero_history = 0
    while respuesta_menu != "0":
        clear()
        menu_conversiones()
        respuesta_menu = preguntar_opcion_menu_conversiones()
        history, numero_history = mostrar_opcion_menu_conversiones(respuesta_menu, history, numero_history)
    # Fin conversiones


def save_keys():
    # Start save_keys
    def menu_save_keys():
        print("-----------------------------------------------------------------------")
        print("\t1.-  Agregar Entrada.")
        print("\t2.-  Mostrar Entradas.")
        print("\t3.-  Copias de seguridad.")
        print("\t4.-  Restauracion.")
        print("\t0.-  Adios.")
        print("\thelp or -h  .- Muestra un listado de ayuda")
        print("-----------------------------------------------------------------------")


    def seleccionar_opcion_save_keys():
        respuesta = input("Que opcion escoges? ")
        return respuesta


    def mostrar_opcion_save_keys(respuesta):
        res = respuesta
        if res == "1":
            agregar_entrada()
        elif res == "help" or res == "-h":
            descripcion_help_save_keys()

    def agregar_entrada():
        print()


    def descripcion_help_save_keys():
        print()
    respuesta_menu_save_keys = None
    while respuesta_menu_save_keys == "0":
        clear()
        menu_save_keys()
        respuesta_menu_save_keys = seleccionar_opcion_save_keys(respuesta_menu_save_keys)
        mostrar_opcion_save_keys(respuesta_menu_save_keys)

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

