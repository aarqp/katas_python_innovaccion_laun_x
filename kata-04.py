#Ejercicio 1

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
data = ""

#Primero, divide el texto en cada oración para trabajar con su contenido

sentences = text.split(". ")
print(*sentences, sep = ("\n"), end = ("\n\n\n"))

#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho. average, temperature y distance

k_words = ["temperature","distance","average"]

# Ciclo for para recorrer la cadena imprimir solo datos sobre la Luna que estén relacionados con las palabras clave
for data in sentences:
    for word in k_words:
        if word in data:
            print(data)

#Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsius

for data in sentences:
    for word in k_words:
        if word in data:
            print(data.replace("C", "Celsius")) 

#ejercicio 2

# Datos con los que vas a trabajar
from pydoc import stripid

name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

# Creamos el título

title = f"Gravity Facts about:  {name} and {planet}"

# cadena multilínea para contener el resto de la información convertir la distancia a metros * 1000

facts = f"\n{ '-' * 80}\nPlanet: {planet} \nName: {name}\nGravity: {gravity * 1000:.2f} m/s^2"

#Unión de ambas cadenas plantillas

template = f"{title.title()} {facts}" 
print(facts, end = ("\n\n"))

#Ahora usa información de una luna diferente comprobar
name = "Ganímedes"
gravity = 0.00143 # in kms
planet = "Mars"

#Comprobación plantilla
print(template, end = ("\n\n"))

stripes = "-" * 80
# Nueva plantilla
new_template = """Gravity Facts about:  {name} and {planet}\n%s\nPlanet: {planet}\nName: {name}\nGravity: {gravity} m/s^2""" % (stripes)
print(new_template.format(name=name, planet=planet, gravity=round(gravity*1000,2)))