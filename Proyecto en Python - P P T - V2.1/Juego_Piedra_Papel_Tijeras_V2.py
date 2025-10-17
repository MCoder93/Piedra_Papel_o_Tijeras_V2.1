# 🧩 Programación en Python
'Juego de Piedra, Papel o Tijeras V2.0.'

import os
import random
import re   # Usaremos expresiones regulares para validar el nombre del jugador

CARPETA = 'save_partida/' # Carpeta donde se almacenarán los archivos

def app():
    crear_directorio()

# Revisa si la carpeta existe de lo contrario la crea
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear carpeta
        os.makedirs(CARPETA)
        print(f'Carpeta "{CARPETA}" creada correctamente.\n')
    else:
        print(f'La carpeta "{CARPETA}" ya existe.\n')

app()


# función para solicitar y validar el nombre de jugador
def obtener_nombre_jugador():
    nombre = input('Bienvenido al juego de Piedra, Papel o Tijeras! Presiona Enter para comenzar\n')
    while True:
        nombre = input('Por favor, ingresa tu nombre de jugador: ').strip()

        # Validar que el nombre no esté vacío y contenga solo letras y espacios
        if not nombre:
            print("❌ El nombre no puede estar vacío. Intenta nuevamente.\n")
        elif not re.match("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre):
            print("❌ El nombre solo puede contener letras y espacios. No se permiten números ni símbolos.\n")
        else:
            print('✅ Nombre creado correctamente!')
            print(f"\n¡Hola, {nombre}! Empecemos a jugar 🎮\n")
            return nombre


# Función para guardar los resultados en un archivo personalizado
def guardar_resultados(nombre, puntos_jugador, puntos_computadora, resultado):
    # Reemplaza espacios en el nombre por guiones bajos para el nombre del archivo
    nombre_archivo = nombre.replace(" ", "_").lower() + ".txt"
    ruta_archivo = os.path.join(CARPETA, nombre_archivo)    # Guardar dentro de la carpeta

    with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write(f'Jugador: {nombre} | Puntos jugador: {puntos_jugador} | 'f'Puntos computadora: {puntos_computadora} | Resultado: {resultado}\n')
    print(f'\n💾 Resultados guardados en: {ruta_archivo}')


lista = ['piedra', 'papel', 'tijeras']

# Llamamos a la función antes de comenzar
nombre_jugador = obtener_nombre_jugador()

# Marcadores iniciales
puntos_jugador = 0
puntos_computadora = 0

while True:
    computadora = random.choice(lista)
    jugador = None

    while jugador not in lista:
        jugador = input('\r\n Elige una opción: piedra, papel o tijeras?: ').lower()

        print(f'\nComputadora: {computadora}')
        print(f'{nombre_jugador}: {jugador}')

    if jugador == computadora:
        print('Empate! ')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Perdiste! ')
            puntos_computadora += 1
        elif computadora == 'tijeras':
            print('Ganaste! ')
            puntos_jugador += 1
    elif jugador == 'papel':
        if computadora == 'tijeras':
            print('Perdiste! ')
            puntos_computadora += 1
        elif computadora == 'piedra':
            print('Ganaste! ')
            puntos_jugador += 1
    elif jugador == 'tijeras':
        if computadora == 'piedra':
            print('Perdiste! ')
            puntos_computadora += 1
        elif computadora == 'papel':
            print('Ganaste! ')
            puntos_jugador += 1

    # Mostrar Marcador
    print(f'\nMarcador Actual: ')
    print(f'{nombre_jugador}: {puntos_jugador} puntos')
    print(f'Computadora: {puntos_computadora} puntos')

    # Función preguntar si deseas seguir jugando o abandonar la partida
    jugar_de_nuevo = input('\r\n Quieres jugar de nuevo? (si/no):').lower()

    if jugar_de_nuevo != 'si':
        # Mensaje de despedida.
        print(f'\r\n GAME OVER, ¡Adios {nombre_jugador}! \r\n')
        break


# Resultado Final
print(f'\n Marcador Final: ')
print(f"{nombre_jugador}: {puntos_jugador} puntos")
print(f"Computadora: {puntos_computadora} puntos")

if puntos_jugador > puntos_computadora:
    resultado_final = "Ganó el jugador"
    print(f'\n🎉 ¡Felicitaciones {nombre_jugador}, ganaste la partida! 🏆')
elif puntos_jugador < puntos_computadora:
    resultado_final = "Ganó la computadora"
    print(f'\n💻 La computadora ganó esta vez. ¡Suerte para la próxima, {nombre_jugador}!')
else:
    resultado_final = "Empate"
    print(f'\n🤝 Empate total entre {nombre_jugador} y la computadora. 🤝')


# Guardar los resultados en un archivo personalizado
guardar_resultados(nombre_jugador, puntos_jugador, puntos_computadora, resultado_final)
print(f'\n Fin de la partida, ¡Adios {nombre_jugador}! Vuelve más tarde para volver a jugar! 👋\n')


print('\n Última Actualización Aplicada: 17-10-2025 \n')
print('By: MBusterCodeWolf-DevOps93')

