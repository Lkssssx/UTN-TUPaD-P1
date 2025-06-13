# Ejercicio 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300


# Ejercicio 2)
print(precios_frutas)

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800


# Ejercicio 3) 
print(precios_frutas)

frutas = precios_frutas.keys()

print(frutas)

# Ejercicio 4)
def nums_tel():
    numeros_telefonicos = {}
    for i in range(5):
        temp_num = list(map(str, input(f"Ingrese el nombre del contacto {i + 1} y el número (separado por espacio): ").split()))
        numeros_telefonicos[temp_num[0]] = int(temp_num[1])
    return numeros_telefonicos
    
contactos = nums_tel()

contacto = input("Ingrese el nombre del contacto que busca: ")

if contacto in contactos:
    print(f"El número de {contacto} es: {contactos[contacto]}")
else:
    print("El contacto solicitado no existe.")



# Ejercicio 5)

def recuento(oracion):
    contador = {}
    for palabra in oracion:
        contador[palabra] = oracion.count(palabra)
    return contador

oracion = list(map(str, input("Ingrese una oración: ").split()))

palabras_unicas = set(oracion)
recuento = recuento(oracion)

print(f"Palabras únicas: {palabras_unicas} \nRecuento: {recuento}")


# Ejercicio 6)

def notas_alumnos():
    notas = {}
    for i in range(3):
        temp_nota = list(map(str, input(f"Ingrese el nombre del alumno {i + 1} y sus TRES calificaciones (separado por espacio): ").split()))
        notas[temp_nota[0]] = int(temp_nota[1]), int(temp_nota[2]), int(temp_nota[3])
    return notas

notas = notas_alumnos()

print("Alumnos: ")
for alumno, nota in notas.items():
    print(f"{alumno}: {nota}")

for alumno, nota in notas.items():
    print(f"El promedio de {alumno} es de: {sum(nota) / 3}")


# Ejercicio 7)

parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {104, 105, 106, 107}

def alumnos_aprobados():
    for alumno_1 in parcial_1:
        if alumno_1 in parcial_2:
            print(f"El alumno {alumno_1} aprobo los dos parciales")
        else:
            print(f"El alumno {alumno_1} aprobo el primer parcial")
        
    for alumno_2 in parcial_2:
        if not(alumno_2 in parcial_1):
            print(f"El alumno {alumno_2} aprobo el segundo parcial")
        
alumnos_aprobados()


# Ejercicio 8)
productos = {"banana": 2, "atun": 4, "crema para los pies": 2, "caramelo": 10}

def consultar_stock():
    buscado = input("Ingrese el producto que busca: ")

    for producto, stock in productos.items():
        if buscado == producto:
            print(f"El stock de '{producto}' es de: {stock}")
            reponer = input("Le gustaría agregar stock (y/n)? ")
            match reponer:
                case "y":
                    productos[producto] += int(input("Ingrese el stock que desea agregar: "))
                case "n":
                    continue

    if not(buscado in productos):
        agregar = input("Ese producto no esta en la lista. Le gustaría agregarlo (y/n)? ")
        match agregar:
            case "y":
                productos[buscado] = int(input("Ingrese el stock que desea agregar: "))
            case "n":
                return print(productos)
            
    print(productos)
    
consultar_stock()


# Ejercicio 9)
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "11:00"): "Clases",
    ("Miercoles", "12:00"): "Juntada"
}

dia = input("Ingrese el dia que desea consultar: ")
hora = input("Ingrese la hora que desea consultar: ")

print(f"El dia {dia} a las {hora} está agendado: {agenda[(dia, hora)]}")


# Ejercicio 10)

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

def invertir():
    nuevo_diccionario = {}
    for pais, capital in original.items():
        nuevo_diccionario[capital] = pais
    return nuevo_diccionario

print("Original: ", original)
print("Invertido: ", invertir())