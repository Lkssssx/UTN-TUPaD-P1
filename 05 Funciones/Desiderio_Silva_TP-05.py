import math as mt

# Utils

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))

    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n


# Ejercicio 1)
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio 2)
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

saludar_usuario(input("Ingrese su nombre: "))

# Ejercicio 3)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = leer_entero_validado("Ingrese su edad"); 
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4)
def calcular_area_circulo(radio):
    area = mt.pi * radio**2
    print(f"El area es {area}")


def calcular_perimetro_circulo(radio):
    perimetro = 2 * mt.pi * radio
    print(f"El perimetro es {perimetro}")

radio = leer_entero_validado("Ingrese el radio del circulo")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


# Ejercicio 5)
def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    print(f"{segundos} segundos son {horas:.2f} horas.")

segundos = leer_entero_validado("Ingrese una cantidad de segundos")
segundos_a_horas(segundos)


# Ejercicio 6)
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")

num_tabla = leer_entero_validado("Ingrese un número entero")
tabla_multiplicar(num_tabla)


# Ejercicio 7)
def operaciones_basicas(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

num1 = leer_entero_validado("Ingrese un número entero")
num2 = leer_entero_validado("Ingrese otro número entero")

operaciones_basicas(num1, num2)


# Ejercicio 8)
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    print(f"Su IMC es: {imc}")

peso = leer_entero_validado("Ingrese su peso")
altura = leer_entero_validado("Ingrese su altura (en metros)")

calcular_imc(peso, altura)


# Ejercicio 9)
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")

celsius = leer_entero_validado("Ingrese los grados celsius que desea convertir en fahrenheit")

celsius_a_fahrenheit(celsius)

# Ejercicio 10)
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio entre {a}, {b}, {c} es: {promedio}")

num1 = leer_entero_validado("Ingrese un número entero")
num2 = leer_entero_validado("Ingrese otro número entero")
num3 = leer_entero_validado("Ingrese un último número entero")

calcular_promedio(num1, num2, num3)