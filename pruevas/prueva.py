import os
import subprocess

# Ruta para guardar temporalmente el archivo batch
batch_file_path = "temp_admin_command.bat"

# Contenido del archivo batch (comando para agregar el usuario)
with open(batch_file_path, 'w') as batch_file:
    batch_file.write('net user player 123 /add\n')

# Comando para ejecutar el archivo batch con permisos de administrador
command = f'powershell -Command "Start-Process cmd -ArgumentList \'/c {batch_file_path}\' -Verb RunAs"'

# Ejecutar el comando
subprocess.run(command, shell=True)

# Eliminar el archivo batch después de su ejecución (opcional)
if os.path.exists(batch_file_path):
    os.remove(batch_file_path)
                