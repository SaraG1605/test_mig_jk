# Este es el script python_fake.py

import sys

def start():
    print("Hello world!")

def middle():
    print("Estás en el medio.")

def finish(message):
    print(message)
    print("Adiós!")

def reject(error_message):
    print(error_message)
    sys.exit(1)

# Verificar el nombre del stage actual pasado como argumento
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python python_fake.py <nombre del stage>")
        sys.exit(1)

    stage = sys.argv[1]

    if stage == "start":
        start()
    elif stage == "middle":
        middle()
    elif stage == "finish":
        finish("Tarea finalizada exitosamente.")
    elif stage == "reject":
        if len(sys.argv) < 3:
            print("Uso: python python_fake.py reject <mensaje de error>")
            sys.exit(1)
        error_message = "Error: " + sys.argv[2]
        reject(error_message)
    else:
        print("Stage desconocido:", stage)

