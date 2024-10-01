import subprocess

def listar_usuarios():
    try:
        # Ejecuta el comando 'net user' y captura la salida
        resultado = subprocess.run(["net", "user"], capture_output=True, text=True)

        # Verifica si el comando se ejecutó correctamente
        if resultado.returncode == 0:
            # Divide la salida en líneas y recorre con un bucle for
            for linea in resultado.stdout.splitlines():
                print(linea)
        else:
            print("Error al ejecutar el comando 'net user'")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llamada a la función
listar_usuarios()