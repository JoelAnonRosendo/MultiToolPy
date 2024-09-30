import tkinter as tk
import subprocess

class UserCreationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("User Creation")

        self.label = tk.Label(master, text="Nombre de usuario:")
        self.label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.create_button = tk.Button(master, text="Crear Usuario", command=self.create_user)
        self.create_button.pack()

        self.messages = tk.Text(master, height=10, width=50)
        self.messages.pack()

    def create_user(self):
        nombre = self.username_entry.get()
        accion = "create_user"

        if accion == "create_user":
            # Ejecutar el comando en CMD usando subprocess
            command = f'powershell Start-Process cmd -ArgumentList "/c net user {nombre} 123 /add" -Verb RunAs'

            # Ejecuta el comando
            subprocess.run(command, shell=True, check=True)
                