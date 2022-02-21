velocidadAsteroide = 25

tamañoAsteroide = 25

# Ejercicio 1

if velocidadAsteroide >= 25:
    print("\n\n¡¡¡¡Advertencia asteroide se acerca muy rápido!!!\n\n")
else: 
    print("\n\nUffff.... El asteroide se encuentra a menos de 25 km/s\n\n")

# Ejercicio 2

if velocidadAsteroide > 20:
    print("\n\n¡¡¡Mira el rayo de luz del asteroide\n\n")
elif velocidadAsteroide == 20:
    print("\n\n¡¡¡Mira el rayo de luz del asteroide\n\n")
else:
    print("\n\n¡¡¡Hoy no es un buen día para ver asteroides!!!\n\n")


# Ejercicio 3

if  tamañoAsteroide <= 1000 and tamañoAsteroide >= 25:
    print("\n\n¡¡¡El asteroide es muy grande!!!\n")
    if velocidadAsteroide >= 25 and velocidadAsteroide >= 20:
        print("¡¡¡¡Advertencia asteroide se acerca muy rápido!!!\n")
        print("¡¡¡Mira el rayo de luz del asteroide!!!\n")
    elif velocidadAsteroide >= 25:
        print("¡¡¡¡Advertencia asteroide se acerca muy rápido!!!\n")
    elif velocidadAsteroide >= 20: 
        print("¡¡¡Mira el rayo de luz del asteroide!!!\n")
    else:
        print("¡¡¡ Rayos... Hoy no es un buen día para ver asteroides!!!\n")        
else:
    print("\n\nUfff!!! El asteroide es pequeño\n\n")
    if velocidadAsteroide >= 25 and velocidadAsteroide >= 20:
        print("¡¡¡¡Advertencia asteroide se acerca muy rápido!!!\n")
        print("¡¡¡Mira el rayo de luz del asteroide!!!\n")
    elif velocidadAsteroide >= 25:
        print("¡¡¡¡Advertencia asteroide se acerca muy rápido!!!\n")
    elif velocidadAsteroide >= 20: 
        print("¡¡¡Mira el rayo de luz del asteroide!!!\n")
    else:
        print("¡¡¡ Rayos... Hoy no es un buen día para ver asteroides!!!\n") 
