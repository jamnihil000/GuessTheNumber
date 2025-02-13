import random

x, y, counter = 0, 0, 1 # Variables y = input de usuario, counter = contador de intentos.

print("Bienvenido a Adivina el número. ¿Cuál dificultad deseas?\n\t 1-Fácil (1-10)\n\t 2-Medio (1-50)\n\t 3-Difícil (1-100)\n\t 4-GOAT (1-1.000.000)")

while True: # Bucle para verificar que la seleccion de dificultad se hace correctamente.
    try:    # Intenta convertir el input del usuario a numero entero.
        difficulty = int(input())
        break                       # Si se cumple, el bucle se rompe.
    except ValueError:              # Si no, se reinicia.
        print("Por favor, selecciona la dificultad ingresando uno de los números correspondientes a cada cual")

# Una suite de condicionales que evaluan el valor de la dificultad y generan un numero al azar basado en ella.
if difficulty == 1: 
    x = random.randint(1, 10)
elif difficulty == 2:
    x = random.randint(1, 50)
elif difficulty == 3:
    x = random.randint(1, 100)
elif difficulty == 4:
    x = random.randint(1, 1_000_000)     

print("¡Intenta adivinar el número!")

while True:
    try:
        y = int(input())
        break
    except ValueError:
        print("Por favor, introduce un número entero válido")

    
while y != x: # Evalúa si el input del usuario es diferente al numero secreto, si es True, se inicia el bucle
    counter = counter + 1   # Aumenta el contador de retroalimentacion con el usuario
    if y < x:               # Compara el input con el numero secreto para brindar una pista al usuario de si es menor o mayor el numero secreto.
        print("¡Ops!, estás equivocado. El número secreto es mayor. Inténtalo de nuevo")
    else:
        print("¡Ops!, estás equivocado. El número secreto es menor. Inténtalo de nuevo")  
    try:
        y = int(input())
        continue # Aqui uso continue para reiniciar el bucle y evaluar la condicion. (yo solo me di cuenta de que no podia usar break porque si no me sacaba del bucle jeje :)
    except ValueError:
        print("Por favor, introduce un número entero válido")

print("¡Has acertado el número!")        

if counter == 1 and difficulty == 1:
    print("Wow, ¡a la primera! a eso le llamo yo tener suerte")
elif counter < 5 and difficulty == 1:
    print(f"Genial, solo has tenido {counter} intentos")
elif counter > 5 and difficulty == 1:
    print(f"{counter} intentos, mmm, juega a otra cosa")

elif counter == 1 and difficulty == 2:
    print("Wow, ¡a la primera! a eso le llamo yo tener suerte")
elif counter < 5 and difficulty == 2:
    print(f"Genial, solo has tenido {counter} intentos")
elif counter > 10 and difficulty == 2:
    print(f"{counter} intentos, mmm, juega a otra cosa")

elif counter == 1 and difficulty == 3:
    print("WHAAAAAAAAAAAAAAT!")
elif counter < 10 and difficulty == 3:
    print(f"Genial, solo has tenido {counter} intentos")
elif counter > 20 and difficulty == 3:
    print(f"{counter} intentos, mmm, juega a otra cosa")

elif counter == 1 and difficulty == 4:
    print("IMPOSSIBLE!!! (Las probabilidades de que este mensaje aparezca son 1 en 1.000.000)")
elif counter < 100 and difficulty == 4:
    print(f"Genial, solo has tenido {counter} intentos")
elif counter > 100 and difficulty == 4:
    print(f"{counter} intentos, no tienes nada mejor que hacer?")