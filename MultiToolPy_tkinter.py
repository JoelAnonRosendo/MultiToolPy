# Importing necessary libraries
import sys
import subprocess


# List of packages to install
packages = ["requests", "cryptography"]

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install each package in the list
for package in packages:
    install(package)

# # Install from requirements.txt
# install('-r requirements.txt')

print("All dependencies installed successfully.")


import os
import json
import random
import string
import requests
import tkinter as tk
from datetime import datetime
from tkinter import scrolledtext
from cryptography.fernet import Fernet
from tkinter import ttk, simpledialog, messagebox, filedialog


API_KEY = '03461bb35e9c5fccbb7f7db5'
FECHA_ACTUAL = datetime.now()
FORMATO = FECHA_ACTUAL.strftime("%Y-%m-%d-%H-%M")


class MultiToolPy(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MultiToolPy")
        self.geometry("600x400")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_calculator_tab()
        self.create_email_generator_tab()
        self.create_password_generator_tab()
        self.create_conversions_tab()
        self.create_save_keys_tab() 
        self.create_chat_ia_tab() 

    def create_calculator_tab(self):
        calculator_frame = ttk.Frame(self.notebook)
        self.notebook.add(calculator_frame, text="Calculadora")
        self.calculator = Calculator(calculator_frame)

    def create_email_generator_tab(self):
        email_frame = ttk.Frame(self.notebook)
        self.notebook.add(email_frame, text="Generador de Correos")
        self.email_generator = EmailGenerator(email_frame)

    def create_password_generator_tab(self):
        password_frame = ttk.Frame(self.notebook)
        self.notebook.add(password_frame, text="Generador de Contraseñas")
        self.password_generator = GeneradorDeContraseñas(password_frame)

    def create_conversions_tab(self):
        conversions_frame = ttk.Frame(self.notebook)
        self.notebook.add(conversions_frame, text="Conversions")
        self.conversion_app = ConversionApp(conversions_frame)
    
    def create_save_keys_tab(self):
        save_keys_frame = ttk.Frame(self.notebook)
        self.notebook.add(save_keys_frame, text="Save Keys")
        self.save_keys = SaveKeysManager(save_keys_frame)
    
    def create_chat_ia_tab(self):
        chat_frame = ttk.Frame(self.notebook)
        self.notebook.add(chat_frame, text="Chat con Wit.ai")
        self.chat_app = WitAIChat(chat_frame)


class Calculator:
    def __init__(self, master):
        self.master = master
        self.history = []
        self.contador_history = 0
        self.create_widgets()

    def create_widgets(self):
        self.entrada = tk.Entry(self.master, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entrada.grid(row=0, column=0, columnspan=4)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        fila = 1
        col = 0
        for boton in botones:
            tk.Button(self.master, text=boton, width=4, height=2, font=('Arial', 18),
                      command=lambda b=boton: self.click_boton(b)).grid(row=fila, column=col)
            col += 1
            if col > 3:
                col = 0
                fila += 1

        self.history_button = tk.Button(self.master, text='Historial', command=self.mostrar_history)
        self.history_button.grid(row=1, column=4, columnspan=4, pady=30)

        self.help_button = tk.Button(self.master, text='Ayuda', command=self.help_calcul)
        self.help_button.grid(row=4, column=4, columnspan=4, pady=10)
        
        self.copy_button = tk.Button(self.master, text='Copia de seguridad', command=self.copia_de_seguridad_calculadora)
        self.copy_button.grid(row=2, column=4, columnspan=4, pady=10)

        self.restore_button = tk.Button(self.master, text='Restaurar', command=self.restauracion_copias_calculadora)
        self.restore_button.grid(row=3, column=4, columnspan=4, pady=10)

    def click_boton(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.entrada.get())
                self.history.append(self.entrada.get() + " = " + str(resultado))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)
            except Exception as e:
                messagebox.showerror("Error", "Operación no válida.")
        elif valor == "C":
            self.entrada.delete(0, tk.END)
        else:
            self.entrada.insert(tk.END, valor)

    def mostrar_history(self):
        if self.history:
            history_str = "Historial de Operaciones:\n"
            for operation in self.history:
                history_str += f"{operation}\n"
            messagebox.showinfo("Historial", history_str)
        else:
            messagebox.showinfo("Historial", "No hay operaciones registradas.")

    def copia_de_seguridad_calculadora(self):
        ruta = os.path.join(os.path.expanduser('~'), 'C:/Users/J.anon/Downloads/python/copias/calculadora/historial', f"historial-{FORMATO}.txt")
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w") as archivo:
            json.dump(self.history, archivo, indent=4)
        messagebox.showinfo("Copia de Seguridad", "Copia de seguridad realizada con éxito.")

    def restauracion_copias_calculadora(self):
        ruta = filedialog.askopenfilename(title="Selecciona un archivo de copia de seguridad", filetypes=[("Text Files", "*.txt")])
        if ruta:
            with open(ruta, "r") as archivo:
                self.history = json.load(archivo)
                self.contador_history = len(self.history)
            messagebox.showinfo("Restauración", "Restauración completada con éxito.")

    def help_calcul(self):
        text = (
            "|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|"
            "|                                 Guia de ayuda                               |"
            "|_____________________________________________________________________________|"
            "|                                                                             |"
            "|   help  or  -h   -->    Muestra una guia de ayuda para el usuario           |"
            "|                         facilitando el uso del programa.                    |"
            "|                                                                             |"
            "|   1.Insertar     -->    Se le pide al usuario que ponga un numero           |"
            "|     valores             cualquiera para guardarlo y poder operar            |"
            "|                         con ellos.                                          |"
            "|                                                                             |"
            "|   2.Operacion    -->    Al preguntar al usuario que tipo de                 |"
            "|     con todos           operacion quiere ralizar escoje todos los           |"
            "|     los valores         valores insertados y realiza la operacion           |"
            "|                         seleccionada con todos.                             |"
            "|                                                                             |"
            "|   3.Especificar  -->    Pregunta al usuario que cantidad de valores         |"
            "|     cantidad de         que quiere utilizar de los valores insertados       |"
            "|     valores             para luego ir preguntando que tipo de operacion     |"
            "|                         quiere hacer en los diferentes valores              |"
            "|                         escoguidos previamente.                             |"
            "|                                                                             |"
            "|   4.Mostrar      -->    Muestra todos los valores que ha añadido el         |"
            "|     valores             usuario para facilitar la decision de operaciones   |"
            "|                         que desee hacer.                                    |"
            "|                                                                             |"
            "|   5.Mostrar      -->    Muestra un historial de todas las operaciones       |"
            "|     historial           realizadas por el usuario.                          |"
            "|                                                                             |"
            "|   6.Eliminar     -->    Elimina el historial entero                         |"
            "|     historial                                                               |"
            "|                                                                             |"
            "|   7.Eliminar     -->    Elimina todos los valores inertado por el           |"
            "|     valores             usuario.                                            |"
            "|                                                                             |"
            "|   8.Copia de     -->    El usuario tiene que eleguir si hacer una           |"
            "|     seguridad           copia de el historial, de los valores o de          |"
            "|                         ambas.                                              |"
            "|                                                                             |"
            "|   9.Restauracion -->    El usuario tiene que eleguir si hacer una           |"
            "|     de copia de         restauracion completa o especifica, si elige        |"
            "|     seguridad           la especifica tendra que eleguir entra restaurar    |"
            "|                         el historial o los valores.                         |"
            "|_____________________________________________________________________________|"
        )
        messagebox.showinfo("Ayuda", text)


class EmailGenerator:
    def __init__(self, master):
        self.master = master
        self.history = {}
        self.contador_history = 0
        self.dominio = simpledialog.askstring("Dominio", "Que dominio quieres usar como por ejemplo 'gmail.com'?,", initialvalue='gmail.com')
        self.create_widgets()

    def create_widgets(self):
        self.menu_label = tk.Label(self.master, text="Seleccione una opción:", font=('Arial', 16))
        self.menu_label.pack(pady=10)

        self.create_button = tk.Button(self.master, text="Crear Correo", command=self.crear_correo)
        self.create_button.pack(pady=5)

        self.change_domain_button = tk.Button(self.master, text="Cambiar Dominio", command=self.cambiar_dominio)
        self.change_domain_button.pack(pady=5)

        self.show_history_button = tk.Button(self.master, text="Mostrar Historial", command=self.mostrar_historial_correos)
        self.show_history_button.pack(pady=5)

        self.delete_email_button = tk.Button(self.master, text="Eliminar Correo", command=self.eliminar_correos)
        self.delete_email_button.pack(pady=5)

        self.backup_button = tk.Button(self.master, text="Copia de Seguridad", command=self.copia_de_seguridad_correos)
        self.backup_button.pack(pady=5)

        self.restore_button = tk.Button(self.master, text="Restaurar Copia", command=self.restauracion_copias_correos)
        self.restore_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.quit_button.pack(pady=5)

    def crear_correo(self):
        nombre = simpledialog.askstring("Nombre", "Cual es tu nombre:")
        apellido = simpledialog.askstring("Apellido", "Cual es tu apellido:")
        if nombre and apellido:
            apellido = apellido.replace('ñ', 'n').lower()
            correo = f"{nombre[0].lower()}.{apellido}@{self.dominio}"
            self.history[self.contador_history + 1] = correo
            self.contador_history += 1
            messagebox.showinfo("Correo Creado", f"Se ha creado el correo: {correo}")
        else:
            messagebox.showwarning("Advertencia", "Nombre y apellido son requeridos.")

    def cambiar_dominio(self):
        nuevo_dominio = simpledialog.askstring("Cambiar Dominio", "Por cual lo quieres cambiar?")
        if nuevo_dominio:
            self.dominio = nuevo_dominio
            messagebox.showinfo("Dominio Cambiado", f"Dominio cambiado a: {self.dominio}")

    def mostrar_historial_correos(self):
        if self.history:
            historial_str = "Historial de correos:\n"
            for clave, valor in self.history.items():
                historial_str += f"{clave}: {valor}\n"
            messagebox.showinfo("Historial", historial_str)
        else:
            messagebox.showinfo("Historial", "No hay correos creados.")

    def eliminar_correos(self):
        if self.history:
            historial_str = "Historial de correos:\n"
            for clave, valor in self.history.items():
                historial_str += f"{clave}: {valor}\n"
            messagebox.showinfo("Historial", historial_str)
            clave = simpledialog.askinteger("Eliminar Correo", "Cual deseas eliminar:")
            if clave in self.history:
                del self.history[clave]
                messagebox.showinfo("Correo Eliminado", "Correo eliminado con éxito.")
            else:
                messagebox.showwarning("Advertencia", "Correo no encontrado.")
        else:
            messagebox.showinfo("Advertencia", "No hay correos para eliminar.")

    def copia_de_seguridad_correos(self):
        ruta = os.path.join(os.path.expanduser('~'), 'C:/Users/J.anon/Downloads/python/copias/correos/historial', f"historial-{FORMATO}.txt")
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w") as archivo:
            json.dump(self.history, archivo, indent=4)
        messagebox.showinfo("Copia de Seguridad", "Copia de seguridad realizada con éxito.")

    def restauracion_copias_correos(self):
        ruta = filedialog.askopenfilename(title="Selecciona un archivo de copia de seguridad", filetypes=[("Text Files", "*.txt")])
        if ruta:
            with open(ruta, "r") as archivo:
                self.history = json.load(archivo)
                self.contador_history = len(self.history)
            messagebox.showinfo("Restauración", "Restauración completada con éxito.")


class GeneradorDeContraseñas:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.menu_label = tk.Label(self.master, text="Generador de Contraseñas", font=('Arial', 18))
        self.menu_label.pack(pady=10)

        self.auto_button = tk.Button(self.master, text="Generar Contraseña Automáticamente", command=self.contraseña_automatica)
        self.auto_button.pack(pady=10)

        self.definir_button = tk.Button(self.master, text="Definir Cantidad de Caracteres", command=self.contraseña_definir)
        self.definir_button.pack(pady=10)

        self.help_button = tk.Button(self.master, text="Ayuda", command=self.help_contraseñas)
        self.help_button.pack(pady=10)

    def contraseña_automatica(self):
        caracteres = 10
        combinacion = string.ascii_letters + string.digits
        contraseña = ''.join(random.choice(combinacion) for _ in range(caracteres))
        messagebox.showinfo("Contraseña Generada", f"{contraseña}")

    def contraseña_definir(self):
        def generar():
            try:
                caracteres = int(entry.get())
                combinacion = string.ascii_letters + string.digits
                contraseña = ''.join(random.choice(combinacion) for _ in range(caracteres))
                messagebox.showinfo("Contraseña Generada", f"{contraseña}")
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un número válido.")

        dialog = tk.Toplevel(self.master)
        dialog.title("Definir Cantidad de Caracteres")
        tk.Label(dialog, text="De cuántos caracteres quieres que sea la contraseña:").pack(pady=10)
        entry = tk.Entry(dialog)
        entry.pack(pady=10)
        tk.Button(dialog, text="Generar", command=generar).pack(pady=10)

    def help_contraseñas(self):
        help_text = ("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|" 
                     "|                                 Guía de ayuda                               |" 
                     "|_____________________________________________________________________________|" 
                     "|                                                                             |" 
                     "|   help  or  -h   -->    Muestra una guía de ayuda para el usuario           |" 
                     "|                         facilitando el uso del programa.                    |" 
                     "|                                                                             |" 
                     "|   1.Generar      -->    Genera automáticamente una contraseña de            |" 
                     "|     contraseñas         10 caracteres.                                      |" 
                     "|     automáticas                                                             |" 
                     "|                                                                             |" 
                     "|   2.Generar      -->    Genera automáticamente una contraseña de            |" 
                     "|     contraseñas         la cantidad de caracteres especificados             |" 
                     "|     por el usuario.                                     |" 
                     "|_____________________________________________________________________________|")
        messagebox.showinfo("Ayuda", help_text)


class ConversionApp:
    def __init__(self, master):
        self.master = master
        self.history = {}
        self.numero_history = 0
        self.create_widgets()

    def create_widgets(self):
        self.menu_label = tk.Label(self.master, text="Menú de Conversiones", font=('Arial', 16))
        self.menu_label.pack(pady=10)

        self.convert_button = tk.Button(self.master, text="Hacer Conversión", command=self.hacer_conversiones)
        self.convert_button.pack(pady=5)

        self.show_history_button = tk.Button(self.master, text="Mostrar Historial", command=self.mostrar_historial)
        self.show_history_button.pack(pady=5)

        self.backup_button = tk.Button(self.master, text="Copia de Seguridad", command=self.copia_de_seguridad_conversiones)
        self.backup_button.pack(pady=5)

        self.restore_button = tk.Button(self.master, text="Restaurar", command=self.restauracion_conversiones)
        self.restore_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.quit_button.pack(pady=5)

    def hacer_conversiones(self):
        conversion_type = simpledialog.askinteger("Tipo de Conversión", "Selecciona el tipo de conversión:\n1. Longitud\n2. Peso\n3. Temperatura\n4. Moneda")
        if conversion_type == 1:
            self.convert_length()
        elif conversion_type == 2:
            self.convert_weight()
        elif conversion_type == 3:
            self.convert_temperature()
        elif conversion_type == 4:
            self.convert_currency()

    def convert_length(self):
        conversion_choice = simpledialog.askinteger("Conversión de Longitud", "Selecciona:\n1. Metros a Kilómetros\n2. Kilómetros a Metros")
        if conversion_choice == 1:
            meters = simpledialog.askfloat("Entrar Metros", "Cuantos metros?")
            kilometers = meters / 1000
            messagebox.showinfo("Resultado", f"{meters} metros son {kilometers} kilómetros.")
            self.add_to_history(f"{meters}m = {kilometers}km")
        elif conversion_choice == 2:
            kilometers = simpledialog.askfloat("Entrar Kilómetros", "Cuantos kilómetros?")
            meters = kilometers * 1000
            messagebox.showinfo("Resultado", f"{kilometers} kilómetros son {meters} metros.")
            self.add_to_history(f"{kilometers}km = {meters}m")

    def convert_weight(self):
        conversion_choice = simpledialog.askinteger("Conversión de Peso", "Selecciona:\n1. Gramos a Kilogramos\n2. Kilogramos a Gramos")
        if conversion_choice == 1:
            grams = simpledialog.askfloat("Entrar Gramos", "Cuantos gramos?")
            kilograms = grams / 1000
            messagebox.showinfo("Resultado", f"{grams} gramos son {kilograms} kilogramos.")
            self.add_to_history(f"{grams}g = {kilograms}kg")
        elif conversion_choice == 2:
            kilograms = simpledialog.askfloat("Entrar Kilogramos", "Cuantos kilogramos?")
            grams = kilograms * 1000
            messagebox.showinfo("Resultado", f"{kilograms} kilogramos son {grams} gramos.")
            self.add_to_history(f"{kilograms}kg = {grams}g")

    def convert_temperature(self):
        conversion_choice = simpledialog.askinteger("Conversión de Temperatura", "Selecciona:\n1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius")
        if conversion_choice == 1:
            celsius = simpledialog.askfloat("Entrar Celsius", "Cuantos grados Celsius?")
            fahrenheit = (celsius * 9/5) + 32
            messagebox.showinfo("Resultado", f"{celsius}°C son {fahrenheit}°F.")
            self.add_to_history(f"{celsius}°C = {fahrenheit}°F")
        elif conversion_choice == 2:
            fahrenheit = simpledialog.askfloat("Entrar Fahrenheit", "Cuantos grados Fahrenheit?")
            celsius = (fahrenheit - 32) * 5/9
            messagebox.showinfo("Resultado", f"{fahrenheit}°F son {celsius}°C.")
            self.add_to_history(f"{fahrenheit}°F = {celsius}°C")

    def convert_currency(self):
        conversion_choice = simpledialog.askinteger("Conversión de Moneda", "Selecciona:\n1. Euro a Dólar\n2. Dólar a Euro")
        if conversion_choice == 1:
            euros = simpledialog.askfloat("Entrar Euros", "Cuantos euros?")
            rate = self.get_exchange_rate('EUR', 'USD')
            dollars = euros * rate
            messagebox.showinfo("Resultado", f"{euros}€ son {dollars}$.\nTasa de cambio: {rate}.")
            self.add_to_history(f"{euros}€ = {dollars}$")
        elif conversion_choice == 2:
            dollars = simpledialog.askfloat("Entrar Dólares", "Cuantos dólares?")
            rate = self.get_exchange_rate('USD', 'EUR')
            euros = dollars * rate
            messagebox.showinfo("Resultado", f"{dollars}$ son {euros}€.\nTasa de cambio: {rate}.")
            self.add_to_history(f"{dollars}$ = {euros}€")

    def get_exchange_rate(self, from_currency, to_currency):
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        return data['conversion_rates'][to_currency]

    def add_to_history(self, conversion):
        self.numero_history += 1
        self.history[f"Historial número {self.numero_history}"] = conversion

    def mostrar_historial(self):
        if self.history:
            history_str = "Historial de Conversiones:\n"
            for key, value in self.history.items():
                history_str += f"{key}: {value}\n"
            messagebox.showinfo("Historial", history_str)
        else:
            messagebox.showinfo("Historial", "No hay conversiones registradas.")

    def copia_de_seguridad_conversiones(self):
        path = os.path.join("C:/Users/J.anon/Downloads/python/copias/conversiones/completas", f"completa-{FORMATO}.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as file:
            json.dump({"historial": self.history, "numero_historial": self.numero_history}, file)
        messagebox.showinfo("Copia de Seguridad", "Copia de seguridad realizada con éxito.")

    def restauracion_conversiones(self):
        ruta = filedialog.askopenfilename(title="Selecciona un archivo de copia de seguridad", filetypes=[("Text Files", "*.txt")])
        if ruta:
            with open(ruta, "r") as archivo:
                self.history = json.load(archivo)
                self.contador_history = len(self.history)
            messagebox.showinfo("Restauración", "Restauración completada con éxito.")


class SaveKeysManager:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        self.generate_key()  # Generar clave solo una vez

    def generate_key(self):
        self.key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        return open('key.key', 'rb').read()

    def encrypt_password(self, password):
        key = self.load_key()
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        key = self.load_key()
        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password

    def save_to_file(self, site, encrypted_password):
        try:
            with open('credentials.json', 'r') as file:
                credentials = json.load(file)
        except FileNotFoundError:
            credentials = {}

        credentials[site] = encrypted_password.decode()

        with open('credentials.json', 'w') as file:
            json.dump(credentials, file)

    def load_credentials(self):
        try:
            with open('credentials.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_password(self):
        site = simpledialog.askstring("Nombre del sitio", "Nombre del sitio:")
        password = simpledialog.askstring("Contraseña", "Contraseña:")
        if site and password:
            encrypted_password = self.encrypt_password(password)
            self.save_to_file(site, encrypted_password)
            messagebox.showinfo('Exito', 'Contraseña guardada con éxito!')
        else:
            messagebox.showwarning('Advertencia', 'Por favor, complete todos los campos.')

    def retrieve_password(self):
        site = simpledialog.askstring("Nombre del sitio", "Nombre del sitio:")
        if site:
            credentials = self.load_credentials()
            if site in credentials:
                password = self.decrypt_password(credentials[site].encode())
                messagebox.showinfo('Contraseña', f'Contraseña para {site}: {password}')
            else:
                messagebox.showwarning('Advertencia', 'No se encontró ninguna contraseña para este sitio.')
        else:
            messagebox.showwarning('Advertencia', 'Por favor, ingrese el nombre del sitio.')

    def create_widgets(self):
        self.menu_label = tk.Label(self.master, text="Gestor de Contraseñas", font=('Arial', 16))
        self.menu_label.pack(pady=10)

        self.save_button = tk.Button(self.master, text="Guardar Contraseña", command=self.save_password)
        self.save_button.pack(pady=5)

        self.retrieve_button = tk.Button(self.master, text="Recuperar Contraseña", command=self.retrieve_password)
        self.retrieve_button.pack(pady=5)


class WitAIChat:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.messages = scrolledtext.ScrolledText(self.master, state='disabled', width=50, height=20, bg='white', fg='black')
        self.messages.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.master, width=40)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.master, text='Send', command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.WIT_AI_TOKEN = '5RW5APRAWCEW6B5545H2IQY2FH4MMGXA'

    def send_message(self, event=None):
        message = self.entry.get()
        if message.strip() == '':
            return

        self.messages.config(state='normal')
        self.messages.insert(tk.END, f'User: {message}\n')
        self.messages.config(state='disabled')

        # Clear the entry box
        self.entry.delete(0, tk.END)

        # Get response from Wit.ai
        self.get_wit_response(message)

    def get_wit_response(self, message):
        url = f'https://api.wit.ai/message?v=20210320&q={message}'
        headers = {'Authorization': f'Bearer {self.WIT_AI_TOKEN}'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            wit_response = response.json()
            self.display_response(wit_response)
        except requests.exceptions.RequestException as e:
            self.display_response({'error': str(e)})

    def display_response(self, response):
        self.messages.config(state='normal')
        if 'error' in response:
            self.messages.insert(tk.END, f'Bot: Error fetching response from Wit.ai.\n')
        else:
            self.messages.insert(tk.END, f'Bot: {response}\n')
            
            for entity_type, entity_list in response["entities"].items():
                    for entity in entity_list:
                        print( f"Entidad: {entity_type}, Valor: {entity['value']}")
                        nombre = entity['value']
                        
            # Recorrer los intents y buscar "create_user"
            for intent in response['intents']:
                if intent['name'] == 'create_user':
                    accion = intent['name']
                    confidence = intent['confidence']
                            
            if accion == "create_user":
                try:
                    # Ejecutar el comando en CMD usando subprocess
                    comando = f"Start-Process powershell -Verb runAs -ArgumentList 'net user {nombre} 123 /add'"
                    # Ejecutar el comando en PowerShell
                    subprocess.run(["powershell", "-Command", comando])
                    self.messages.insert(tk.END, f'Bot: Usuario \'{nombre}\' creado correctamente. \n')
                except subprocess.CalledProcessError as e:
                    self.messages.insert(tk.END, f"Ocurrió un error al ejecutar el comando: {e}")

            # elif accion == "view_all_users":
            #     try:
            #         self.messages.insert(tk.END, f'Bot: Lista usuarios dentro del equipo:\n')
            #         resultado = subprocess.run(["net", "user"], capture_output=True, text=True)

            #         # Verifica si el comando se ejecutó correctamente
            #         if resultado.returncode == 0:
            #             # Divide la salida en líneas y recorre con un bucle for
            #             for linea in resultado.stdout.splitlines():
            #                 self.messages.insert(tk.END, f'{linea}\n')
            #         else:
            #             print("Error al ejecutar el comando 'net user'")
            #     except:
            #         self.messages.insert(tk.END, f"Ocurrió un error al ejecutar el comando: {e}")
            else:
                self.messages.insert(tk.END, f"Operación cancelada.")
                
        self.messages.config(state='disabled')


if __name__ == "__main__":
    app = MultiToolPy()
    app.mainloop()
