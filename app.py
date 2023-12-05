import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()

    while eleccion_usuario not in opciones:
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()

    eleccion_maquina = random.choice(opciones)

    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La máquina eligió: {eleccion_maquina}")

    if eleccion_usuario == eleccion_maquina:
        print("Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

jugar_piedra_papel_tijera()
