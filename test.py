import random

def ruleta_rusa():
    # Simulamos 6 cámaras: 5 vacías (0) y 1 con "bala" (1)
    camaras = [0] * 5 + [1]
    random.shuffle(camaras)

    input("Presiona Enter para girar el tambor y jugar a la ruleta rusa...")

    # Seleccionamos una cámara al azar
    resultado = random.choice(camaras)
    if resultado == 1:
        print("tonto")
    else:
        print("Has sobrevivido. ¡Suerte la próxima vez!")

if __name__ == "__main__":
    ruleta_rusa()
